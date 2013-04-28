# vim: set fileencoding=utf-8 :
"""overlay: Merging directories like a champ!

Usage:
    overlay.py (-h | --help)
    overlay.py build [--config=FILES] [--clean]

Options:
    -h --help          Show this screen
    --config=FILE      Comma-separated list of config-files[default: None]
    --clean            Clean build

"""
from __future__ import absolute_import, division

import os
import shutil
from jinja2 import (
    Environment,
    FileSystemLoader,
    StrictUndefined,
    UndefinedError
)

__version__ = (0, 1, 0)

DEFAULT_CONFIG = {'template_suffix': '.otpl'}
"""Default config options"""


class ConfigError(Exception):
    pass


class TemplateError(Exception):
    pass


def build(config, clean=False):
    """Build based on config

    :raises: :class:`ConfigParser.NoSectionError` - If a section is missing
    :raises: :class:`ConfigParser.NoOptionError` - If an option is missing
    :raises: :class:`ConfigError` - If an option is invalid
    :raises: :class:`TemplateError` - If a template uses an undefined variable

    :returns: Path to build directory
    """

    dest_dir = config.get('build', 'dest')
    src_dir = config.get('build', 'src')
    overlay_dir = config.get('build', 'overlay')
    if os.path.exists(src_dir) and not os.path.isdir(src_dir):
        exit('src dir {0} exists but not a directory'.format(src_dir))

    if os.path.exists(dest_dir):
        if clean:
            shutil.rmtree(dest_dir)
        else:
            raise ConfigError("Destination dir '{0}' exists - remove it"
                              .format(dest_dir))

    if not os.path.isdir(overlay_dir):
        raise ConfigError("Overlay dir '{0}' doesn't exist"
                          .format(overlay_dir))

    # Copy src dir
    shutil.copytree(src_dir, dest_dir)
    assert os.path.isdir(dest_dir)

    # Add overlay
    template_vars = (dict(config.items('template_vars'))
                     if config.has_section('template_vars') else {})
    env = Environment(loader=FileSystemLoader(overlay_dir),
                      undefined=StrictUndefined)
    abs_overlay = os.path.abspath(overlay_dir)
    template_suffix = config.get('build', 'template_suffix')
    for root, dirs, files in os.walk(overlay_dir):
        abs_root = os.path.abspath(root)
        template_base = abs_root[len(abs_overlay) + 1:]
        for f in files:
            if f.endswith(template_suffix):
                src = os.path.join(template_base, f)
                dest = os.path.join(dest_dir,
                                    template_base,
                                    f[0:-len(template_suffix)])

                # Get contents before truncating the file
                try:
                    contents = env.get_template(src).render(**template_vars)
                except UndefinedError, e:
                    raise TemplateError("{0} (in '{1}')".format(e, src))

                with open(dest, 'w') as fh:
                    fh.write(contents)
            else:
                src = os.path.join(root, f)
                dest = os.path.join(dest_dir, template_base, f)
                shutil.copyfile(src, dest)

    return dest_dir

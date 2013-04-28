Overlay
~~~~~~~

Merges a source directory and an overlay directory into a destination directory. Files in the overlay direcotory will be treated as jinja templates if they end with the configuration option `[build] template_suffix` (defaults to '.otpl').

Usage::

    overlay.py (-h | --help)
    overlay.py build [--config=FILES] [--clean]
    overlay.py build <src> <overlay> <dest> [--config=FILES] [--clean]

Options::

    -h --help          Show help
    --config=FILE      Comma-separated list of config-files[default: ]
    --clean            Clean build

Jinja templates
===============

Template variables can be set in the configuration section `[template_vars]`.

Configuration file
==================

The configuration files will have a default interpolated value, `here`, which is the directory that overlay.py was run from.

Sections
--------

build
^^^^^

src
    Path to the original directory
overlay
    Path to overlay directory
dest
    Path to the build directory
template_suffix
    Template suffix [default='.otpl']

template_vars
^^^^^^^^^^^^^

Contains key=value jinja template variables.


Source
------

The source is hosted at `http://github.com/danielholmstrom/overlay <http://github.com/danielholmstrom/overlay>`_.


License
=======

Overlay is MIT licensed.

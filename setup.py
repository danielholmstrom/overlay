"""
~~~~~~~
Overlay
~~~~~~~

Read more in the source or on github
<https://github.com/danielholmstrom/overlay>.
"""

import os
import sys
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

# Requirements for the package
install_requires = [
    'jinja2',
    'docopt'
]

# Requirement for running tests
test_requires = install_requires

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='overlay',
      version='0.1.0b1',
      description="Overlays a directory with templates",
      long_description=README,
      url='http://github.com/danielholmstrom/overlay/',
      license='MIT',
      author='Daniel Holmstrom',
      author_email='holmstrom.daniel@gmail.com',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: '],
      py_modules=['overlay'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=test_requires,
      test_suite='tests',
      scripts=['scripts/overlay'],
      **extra
      )

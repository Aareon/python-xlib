# Distutils script for python-xlib

from setuptools import setup
import sys

if sys.version < '2.3.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.download_url = None

import Xlib

setup(name='python-xlib',
        version=Xlib.__version_string__,

        description='Python X Library',
        download_url='https://github.com/python-xlib/python-xlib/releases',
        url='https://github.com/python-xlib/python-xlib',
        license='GPL',

        author='Peter Liljenberg',
        author_email='petli@ctrl-c.liu.se',

        install_requires=['six>=1.10.0'],

        packages=[
            'Xlib',
            'Xlib.ext',
            'Xlib.keysymdef',
            'Xlib.protocol',
            'Xlib.support',
            'Xlib.xobject'
            ],
        )


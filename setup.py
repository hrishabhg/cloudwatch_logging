#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

requires = [
    'django>=1.8.0,<1.10.0',
    'boto3>=1.4.0'
]


def get_version():
    init = open(os.path.join(ROOT, '', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='cloudwatch_logging',
    version=get_version(),
    description='Cloudwatch logging for Django',
    long_description=open('README.md').read(),
    author='Hrishabh Gupta',
    url='https://github.com/hrishabhg/cloudwatch_logging',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={
    },
    include_package_data=True,
    install_requires=requires,
    license="",
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
)

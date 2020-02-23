import os
import sys

from setuptools import setup

if sys.version_info < (2, 7):
    tests_require = ['unittest2']
else:
    tests_require = []


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='docassemblekvsession',
    version='0.1',
    url='https://github.com/jhpyle/flask-kvsession',
    license='MIT',
    author='Marc Brinkmann and Jonathan Pyle',
    author_email='jhpyle@gmail.com',
    description='Transparent server-side session support for flask',
    long_description=read('README.rst'),
    packages=['docassemblekvsession'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.8', 'simplekv>=0.9.2', 'werkzeug', 'itsdangerous>=0.20',
        'six',
    ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)

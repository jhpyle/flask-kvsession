import os
import sys

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='docassemblekvsession',
    version='0.9',
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
        'Flask',
        'simplekv',
        'Werkzeug',
        'itsdangerous',
        'six'
    ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)

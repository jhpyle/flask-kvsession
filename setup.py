import os
import sys

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='docassemblekvsession',
    version='0.6',
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
        'Flask==1.1.2', 'simplekv==0.14.1', 'Werkzeug==2.0.0', 'itsdangerous==2.0.0',
        'six==1.16.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)

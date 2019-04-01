# _*_ coding: utf-8 _*_

from os import path
from setuptools import find_packages, setup
from codecs import open

name = "nmc_vf_tools"
author = __import__(name).__author__
version = __import__(name).__version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,

    version=version,

    description=("A collections of function for making verification products"
                 "for meteorological verification."),
    long_description=long_description,

    # author
    author=author,
    author_email='liucouhua@163.com',

    # LICENSE
    license='GPL3',

    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],

    packages=find_packages(exclude=['docs', 'tests', 'build', 'dist']),
    include_package_data=True,
    exclude_package_data={'': ['.gitignore']},

    install_requires=['numpy>=1.12.1',
                      'scipy>=0.19.0',
                      'pandas>=0.20.0',
                      'scikit_learn >=0.19.2',
                      'matplotlib >=2.2.3',
                      'cartopy>=0.16.0',
                      'nmc_met_graphics>=0.1.0',
                      'nmc_vf_base>=0.1.0'
                      ]
)


#!/usr/bin/env python 
# coding=utf-8
        
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    with open('README.rst', 'r') as fp:
        readme = fp.read()
except :
    readme = ''
try:
    with open('README.md', 'r') as fp:
        readme = fp.read()
except :
    pass

try:
    with open('HISTORY.rst', 'r') as fp:
        history = fp.read()
except :
    history = ''
        

setup(
    name = 'BdMusic',
    version = '0.0.5',
    description = 'Baidu Music Download Helper',
    long_description = readme + history,
    author = 'Cole Smith',
    author_eamil = 'uniquecolesmith@gmail.com',
    url = '',
    packages = ['BdMusic'],
    package_dir = {"BdMusic": "BdMusic"},
    include_package_data = True,
    install_requires = ['requests'],
    license = "Apache 2.0",
    zip_safe = False,
    classifiers = ('Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers', 'Natural Language :: English', 'License :: OSI Approved :: Apache Software License', 'Programming Language :: Python', 'Programming Language :: Python :: 2.6', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4'),
    entry_points = {"console_scripts": ["BdMusic = BdMusic:main"]},

)

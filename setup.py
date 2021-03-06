#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name="element",
    version="0.0.1",
    description="Element: a node based cms",
    author="Thomas Rabaix",
    author_email="thomas.rabaix@gmail.com",
    url="https://github.com/rande/python-element",
    packages = find_packages(),
    install_requires=["markdown"],
    include_package_data = True,
)
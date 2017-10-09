#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='esociallib',
    version='0.1',
    author='Raphael Valyi',
    author_email='raphael.valyi@akretion.com',
    url='https://github.com/akretion/esociallib',
    description='esociallib: Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial) for Brazil',
    long_description=open('README.rst').read(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    keywords='eSocial ERP Odoo',
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    zip_safe=False,
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'numpy', 'pynwb', 'nwbext_ecog', 'ndx-spectrum']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Luiz Tauffer",
    author_email='luiz_tauffer@hotmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Copy nwb files.",
    entry_points={
        'console_scripts': [
            'nwb_copy=nwb_copy.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='nwb_copy',
    name='nwb_copy',
    packages=find_packages(include=['nwb_copy']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/luiztauffer/nwb_copy',
    version='0.1.0',
    zip_safe=False,
)

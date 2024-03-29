#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

from setuptools import setup, find_packages

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Read version from app
with open("bot/__init__.py", "rb") as f:
    VERSION = str(re.search('__version__ = "(.+?)"',
                            f.read().decode("utf-8")).group(1))

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme_file:
    readme = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), "HISTORY.md")) as history_file:
    history = history_file.read().replace(".. :changelog:", "")

if sys.argv[-1] == "tag":
    os.system("git tag -a v{} -m 'tagging v{}'".format(VERSION, VERSION))
    os.system("git push --tags && git push origin main")
    sys.exit()

setup(
    name="bot",
    version=VERSION,
    description="""Scraper Bot""",
    long_description=readme + "\n\n" + history,
    author="Raul Diaz",
    author_email="raukateromadness@gmail.com",
    url="https://github.com/Raukdv/bot_scraper",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'homoglyphs',
        'phonenumbers',
        'python-dotenv',
        'requests',
        'selenium'
    ],
    entry_points={
        'console_scripts': ['bot=bot.command_line:main'],
    },
    license="Apache License 2.0",
    zip_safe=False,
    keywords="bot",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment"
    ],
)

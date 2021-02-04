#! /usr/bin/env python
from os import path

from setuptools import find_packages, setup

version = "1.0.0"

with open("README.md") as f:
    long_description = f.read()

install_requires = [
    "acme>=0.31.0",
    "certbot>=0.31.0",
    "setuptools",
    "zope.interface",
    "dns-lexicon",
    "tldextract>=3.1.0",
]

here = path.abspath(path.dirname(__file__))

setup(
    name="certbot-dns-nextlayer",
    version=version,
    description="nextlayer DNS Authenticator plugin for Certbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nextlayergmbh/certbot-dns-nextlayer.git",
    author="Alexander Holzapfel",
    author_email="alexander.holzapfel@nextlayer.at",
    license="MIT License",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "certbot.plugins": [
            "dns-nextlayer = certbot_dns_nextlayer.dns_nextlayer:Authenticator",
        ],
    },
)

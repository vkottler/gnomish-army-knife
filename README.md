<!--
    =====================================
    generator=datazen
    version=3.1.4
    hash=e22742fe4b276449dd885b449fc22323
    =====================================
-->

# gnomish-army-knife ([0.1.0](https://pypi.org/project/gnomish-army-knife/))

[![python](https://img.shields.io/pypi/pyversions/gnomish-army-knife.svg)](https://pypi.org/project/gnomish-army-knife/)
![Build Status](https://github.com/vkottler/gnomish-army-knife/workflows/Python%20Package/badge.svg)
[![codecov](https://codecov.io/gh/vkottler/gnomish-army-knife/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/gnomish-army-knife)
![PyPI - Status](https://img.shields.io/pypi/status/gnomish-army-knife)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/gnomish-army-knife)

*Software tools for WoW arena analysis.*

## Documentation

### Generated

* By [sphinx-apidoc](https://vkottler.github.io/python/sphinx/gnomish-army-knife)
(What's [`sphinx-apidoc`](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)?)
* By [pydoc](https://vkottler.github.io/python/pydoc/gnomish_army_knife.html)
(What's [`pydoc`](https://docs.python.org/3/library/pydoc.html)?)

## Python Version Support

This package is tested with the following Python minor versions:

* [`python3.8`](https://docs.python.org/3.8/)
* [`python3.9`](https://docs.python.org/3.9/)
* [`python3.10`](https://docs.python.org/3.10/)
* [`python3.11`](https://docs.python.org/3.11/)

## Platform Support

This package is tested on the following platforms:

* `ubuntu-latest`
* `macos-latest`
* `windows-latest`

# Introduction

# Command-line Options

```
$ ./venv3.11/bin/gak -h

usage: gak [-h] [--version] [-v] [-q] [--curses] [--no-uvloop] [-C DIR]
           {noop} ...

Software tools for WoW arena analysis.

options:
  -h, --help         show this help message and exit
  --version          show program's version number and exit
  -v, --verbose      set to increase logging verbosity
  -q, --quiet        set to reduce output
  --curses           whether or not to use curses.wrapper when starting
  --no-uvloop        whether or not to disable uvloop as event loop driver
  -C DIR, --dir DIR  execute from a specific directory

commands:
  {noop}             set of available commands
    noop             command stub (does nothing)

```

# Internal Dependency Graph

A coarse view of the internal structure and scale of
`gnomish-army-knife`'s source.
Generated using [pydeps](https://github.com/thebjorn/pydeps) (via
`mk python-deps`).

![gnomish-army-knife's Dependency Graph](im/pydeps.svg)

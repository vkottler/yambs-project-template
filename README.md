<!--
    =====================================
    generator=datazen
    version=3.1.4
    hash=a525b8130896da2dbb2d08938179573b
    =====================================
-->

# yambs-project-template

![Build Status](https://github.com/vkottler/yambs-project-template/actions/workflows/create-project.yml/badge.svg)

The [yambs](https://github.com/vkottler/yambs) project implements a C/C++
build-system.

*This is a template intended to be used with
[Cookiecutter](https://github.com/cookiecutter/cookiecutter).*

# Usage

Invoke `cookiecutter` and fill out information about your project:

```
cookiecutter git@github.com:vkottler/yambs-project-template.git
```

Example output (interactive):

```
name [Vaughn Kottler]: <Your Name>
email [vaughnkottler@gmail.com]: <your@email.com>
...
```

## Structure

```
$ tree -a -I venv*|__pycache__|dist|*cov*|*-out|config|ninja|.ninja*|build|*.egg-info|tags|mklocal|.git*|.*cache*|third-party|docs|toolchains -- project-name

project-name
├── build.ninja
├── .clang-format
├── compile_commands.json
├── .isort.cfg
├── LICENSE
├── local
│   ├── configs
│   │   ├── license.yaml
│   │   └── project.yaml
│   └── yambs.yaml
├── Makefile
├── manifest.yaml
├── mypy.ini
├── project_name
│   ├── __init__.py
│   └── requirements.txt
├── README.md
├── src
│   ├── apps
│   │   └── test_file.cc
│   └── example
│       ├── sample.cc
│       └── sample.h
├── tasks
│   └── conf.py
└── yambs.yaml

7 directories, 19 files

```

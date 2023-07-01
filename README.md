<!--
    =====================================
    generator=datazen
    version=3.1.2
    hash=d5e7b8cd7f739aa2074d0c98ffa13cb0
    =====================================
-->

# yambs-project-template

The [yambs](https://github.com/vkottler/yambs) project implements a C/C++
build-system.

*This is a template intended to be used with
[Cookiecutter](https://github.com/cookiecutter/cookiecutter).*

# Usage

Invoke `cookiecutter` and fill out information about your project:

```
$ cookiecutter git@github.com:vkottler/yambs-project-template.git
name [Vaughn Kottler]: <Your Name>
email [vaughnkottler@gmail.com]: <your@email.com>
...
```

## Structure

```
$ tree -a -I venv*|__pycache__|dist|*cov*|*-out|config|ninja|.ninja*|build|*.egg-info|tags|mklocal|.git*|.*cache* -- project-name

project-name
├── build.ninja
├── compile_commands.json
├── .isort.cfg
├── LICENSE
├── local
│   ├── configs
│   │   └── license.yaml
│   └── templates
│       └── README.md.j2
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

8 directories, 17 files

```

<!--
    =====================================
    generator=datazen
    version=3.1.2
    hash=15766cda0ec5725e886fb56850066eb8
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
$ tree -a -I venv*|__pycache__|dist|*cov*|*-out|config|build|*.egg-info|tags|.git*|.*cache* -- project-name

project-name
├── LICENSE
├── local
│   ├── configs
│   │   └── license.yaml
│   └── templates
│       └── README.md.j2
├── Makefile
├── manifest.yaml
├── project_name
│   └── dev_requirements.txt
├── README.md
├── src
│   ├── apps
│   │   └── test_file.cc
│   └── example
│       ├── sample.cc
│       └── sample.h
├── tasks
│   ├── conf.py
│   └── __init__.py
└── yambs.yaml

8 directories, 13 files

```

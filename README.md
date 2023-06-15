<!--
    =====================================
    generator=datazen
    version=3.1.2
    hash=f454b4b9b3c630d7e016ac7fe82492e4
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
├── src
│   ├── apps
│   │   └── test_file.cc
│   └── example
│       ├── sample.cc
│       └── sample.h
└── yambs.yaml

3 directories, 4 files

```

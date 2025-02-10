# Treee

This package was created to help me visualize directory structures in my coding tutorials.

Example:

```
treee/
├── dist/
│   ├── treee-0.0.3-py3-none-any.whl
│   └── treee-0.0.3.tar.gz
├── src/
│   └── treee/
│       └── tree.py
├── .gitignore
├── LICENSE.txt
├── README.md
└── pyproject.toml
```

## Install

```
pip install -i https://test.pypi.org/simple/ treee-CodersBringChange
```

Visit project on [PyPI](https://test.pypi.org/project/treee-CodersBringChange/)

## Features

- Shows ASCII tree of current folder and beyond
- Sorts by type (folders on top), then by name

## Import in existing code

```
from treee import tree

tree.print_tree()
```

## Run from command line

```
treee
```

# apydoc
Dead simple automatic python api documentation generation

This project came out as a result of a frustration from the lack of **simple** api documentation tools for python. It uses the `inspect` library to get the names, signatures and docstrings and the `jinja2` to produce the disired format. It fits into my workflow, which is: write simple library (tool, snippet), generate documentation in markdown (or other language supported by gitlab) and put it on company gitlab and forgot... 

This tool is heavy inspired by the Christian Medina [artice](https://medium.com/python-pandemonium/python-introspection-with-the-inspect-module-2c85d5aa5a48).

## Installation

- requirements
    - Python 3.3 and later
    - [jinja2](http://jinja.pocoo.org/docs/2.10/)
    - [docopt](http://docopt.org/)

- using `pip`

```
pip install git+https://github.com/liborw/apydoc.git
```

- from source

```
git clone git@github.com:liborw/apydoc.git
cd apydoc
pip install .
```

## Usage

How the [api documentation](docs/pyapidoc.md) for this tool is show bellow, it is supposed to be run in the `bin` directory of this repository:

```
$ apydoc -f apydoc -t script.md.jinja -o ../docs apydoc
```

## Templates

```
module
  .name
  .doc
  .classes
    .name
    .doc
    .functions
      .name
      .signature
      .doc
  .functions
    .name
    .signature
    .doc
```
## Limitations

- no support for inheritance and such
- and many more...

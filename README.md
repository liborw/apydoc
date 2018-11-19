# pyapidoc
Dead simple automatic python api documentation generation

This project came out as a result of a frustration from the lack of **simple** api documentation tools for python. It uses the `inspect` library to get the names, signatures and docstrings and the `jinja2` to produce the disired format. It fits into my workflow, which is: write simple library (tool, snippet), generate documentation in markdown (or other language supported by gitlab) and put it on company gitlab and forgot... 

## Installation

```shell

```

## Usage

```shell
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

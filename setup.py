
from setuptools import setup

setup(name='pyapidoc',
      version='0.1',
      description='Dead simple python API documentation generation tool',
      author='Libor Wagner',
      author_email='libor.wagner@cvut.cz',
      url='https://github.com/liborw/pyapidoc/blob/master/README.md',
      scripts=['bin/pyapidoc'],
      install_requires=[
          'jinja2',
          'docopt'
      ],
      )


from setuptools import setup

setup(name='apydoc',
      version='0.1',
      description='Dead simple python API documentation generation tool',
      author='Libor Wagner',
      author_email='libor.wagner@cvut.cz',
      url='https://github.com/liborw/apydoc/blob/master/README.md',
      scripts=['bin/apydoc'],
      install_requires=[
          'jinja2',
          'docopt'
      ],
      )

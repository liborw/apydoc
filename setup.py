
from setuptools import setup

setup(name='apydoc',
      version='0.1',
      description='Simple python API documentation generation tool',
      author='Libor Wagner',
      author_email='libor.wagner@cvut.cz',
      url='https://github.com/liborw/apydoc/blob/master/README.md',
      scripts=['bin/apydoc'],
      packages=['apydoc'],
      install_requires=[
          'jinja2',
          'docopt'
      ],
      include_package_data=True
      )

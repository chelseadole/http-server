"""Setup module for server.py."""

from setuptools import setup

setup(
    name='http server',
    description='Some http servers',
    author='Chelsea Dole, Kavdi Hodgson',
    author_email='chelseadole@gmail, kavdyjh@gmail.com',
    package_dir={' ': 'src'},
    py_modules=['server'],
    install_requires=[],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']})

#!/usr/bin/env python
# coding=utf-8

import os
import sys

from distutils.core import setup, Command
from setuptools.command.test import test as TestCommand
from setuptools import find_packages

import python_bootstrap


class BootstrapTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


class BootstrapClean(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./.cache ./.eggs ./build ./dist')
        os.system('rm -vrf ./*.tgz ./*.egg-info')
        os.system('find . -name "*.pyc" -exec rm -vrf {} \;')
        os.system('find . -name "__pycache__" -exec rm -rf {} \;')

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme_file:
    README = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as license_file:
    LICENSE = license_file.read()

if __name__ == "__main__":
    setup(name='python-project-bootstrap',
          version=python_bootstrap.__version__,
          description="Start your new python project with a ready to install"
                      "directory and scripts structure",
          author='Ricardo Oyarzun',
          author_email="royarzun@gmail.com",
          license=LICENSE,
          long_description=README,
          test_suite="tests",
          tests_require=['pytest'],
          cmdclass={
              'test': BootstrapTest,
              'clean': BootstrapClean,
          },
          packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*"]),
          package_dir={"python-bootstrap": "python-bootstrap"},
          classifiers=(
              'Development Status :: 5 - Production/Stable',
              'Environment:: Console',
              'Intended Audience :: Developers',
              'Natural Language :: English',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
          )
    )

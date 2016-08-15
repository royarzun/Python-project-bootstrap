# coding=utf-8

import getpass
import os
import shutil

from jinja import Environment, PackageLoader

from python_bootstrap.utils.decorators import verify_creation


env = Environment(loader=PackageLoader("python_bootstrap", "res/templates"))


@verify_creation
def copy_folder(origin_path, destination_path):
    # Check if destination folder exists
    current_dir = os.path.dirname(__file__)
    origin_path = os.path.join(current_dir, origin_path)
    if not os.path.isdir(destination_path):
        shutil.copytree(origin_path, destination_path)


@verify_creation
def create_file_from_string(file_path, content_string=""):
    file_object = open(file_path, "w")
    file_object.write(content_string)
    file_object.close()


@verify_creation
def create_file_from_template(file_path, template, **kwargs):
    """Creates files from python Jinja templates. Available templates:

    - templates/python_class
    - templates/python_setup
    - templates/python_test

    Each template can render custom variable, to do so, use keyword arguments
    """
    file_object = open(file_path, "w")
    service_template = env.get_template(template)
    file_object.write(service_template.render(kwargs))
    file_object.close()


@verify_creation
def create_folder(folder_name):
    """Create any folder"""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def get_username():
    """Returns the active username"""
    return getpass.getuser()


def make_executable(file_location):
    """Makes file in given location executable"""
    mode = os.stat(file_location).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(file_location, mode)
    print "executable:\t" + file_location



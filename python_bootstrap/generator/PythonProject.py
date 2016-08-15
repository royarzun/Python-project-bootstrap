# coding=utf-8

from python_bootstrap.utils.SystemUtils import create_folder


class PythonProject(object):

    def __init__(self, project_name, **kwargs):
        self.project_name = project_name
        self._root_folder = project_name
        self._main_package = project_name + "/" + project_name
        self._test_package = project_name + "/tests/"
        pass

    def _create_directories(self):
        """Creates the directories required for the project:

         - project_name
         - project_name/project_name
         - project_name/tests
        """
        create_folder(self._root_folder)
        create_folder(self._main_package)
        create_folder(self._test_package)

    def _create_project_setup(self):
        pass

    def _create_project_tests(self):
        pass

    def _create_main_package(self):
        pass

    def create(self):
        self._create_directories()
        self._create_project_setup()
        self._create_main_package()
        self._create_project_tests()

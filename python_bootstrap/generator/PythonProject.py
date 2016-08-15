# coding=utf-8

from python_bootstrap.utils.SystemUtils import create_folder,\
    create_file_from_template, make_executable, get_username

TEMPLATE_SETUP = "python_setup.txt"
TEMPLATE_CLASS = "python_class.txt"
TEMPLATE_INIT = "python_init.txt"
TEMPLATE_TESTS = "python_test.txt"


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
        create_file_from_template(self._main_package + "/__init__.py",
                                  TEMPLATE_INIT, author=get_username())
        create_folder(self._test_package)

        create_file_from_template(self._test_package + "/__init__.py",
                                  TEMPLATE_INIT, author=get_username())

    def _create_project_setup(self):
        setup_file_path = self._root_folder + "/setup.py"

        # Create setup.py
        create_file_from_template(setup_file_path,
                                  TEMPLATE_SETUP,
                                  project_name=self.project_name)
        make_executable(setup_file_path)

    def _create_project_tests(self):
        pass

    def create(self):
        self._create_directories()
        self._create_project_setup()
        self._create_project_tests()

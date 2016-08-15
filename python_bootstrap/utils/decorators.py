# coding=utf-8

import os


def verify_creation(file_creation_function):
    def checking_creation(*args, **kwargs):
        file_creation_function(*args, **kwargs)
        filename = args[0]
        if os.path.isfile(filename) or os.path.isdir(filename):
            print "created:\t" + filename
        else:
            raise IOError("Could not create file...")

    return checking_creation

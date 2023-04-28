import os
from definition import ROOT_DIR


def resources_path(dir_name, file_name):
    file_path_and_name = os.path.abspath(os.path.join(ROOT_DIR, dir_name, file_name))

    return file_path_and_name
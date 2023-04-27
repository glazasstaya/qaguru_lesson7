import os

def resources_path(file_name):
    current_file_path = os.path.abspath('__file__')
    root_path = os.path.dirname(current_file_path)
    file_path_and_name = os.path.abspath(os.path.join(root_path, '..', 'resources', file_name))

    return file_path_and_name
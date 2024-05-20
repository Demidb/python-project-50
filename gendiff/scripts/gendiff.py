import os


def get_extension(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def get_data(expected_result):
    with open(get_fixtures_path(expected_result), "r") as correct:
        return correct.read()
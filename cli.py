import argparse
def get_args_from_cli():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.'
                                     epilogue="optional arguments")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('h')
    parser.add_argument('--help', help = 'show this help message and exit')
    args = parser.parse_args()

if name == 'main':
    get_args_from_cli()
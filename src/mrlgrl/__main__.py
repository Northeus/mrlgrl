import subprocess

from argparse import ArgumentParser
from typing import NamedTuple

from mrlgrl.quartus import add_path, check_path


class ProjectArgs(NamedTuple):
    name: str = None
    file: str = None


def status(args):
    print('Quartus was ' + ('' if check_path() else 'not ') + 'found.')

    # output = subprocess.run(
    #         'quartus_sh',
    #         stdout=subprocess.DEVNULL,
    #         stderr=subprocess.DEVNULL)

    # p = ProjectArgs(**parser.parse_args().__dict__)


def main():
    parser = ArgumentParser(
            description='CLI tool for quartus DE-1SoC boards.'
                        ' You might need to set up PATHS for quartus folder.'
                        ' Use status command to check,'
                        ' if the quartus is detected correctly.')

    subparsers = parser.add_subparsers(required=True)

    parser_status = subparsers.add_parser(
            'status',
            help='Check quartus binaries',
            description='Check if the Quartus binaries were found.')
    parser_status.set_defaults(func=status)

    parser_project = subparsers.add_parser(
            'project',
            help='Project utilities',
            description='Project utilities.')

    project_operations = parser_project.add_mutually_exclusive_group(
            required=True)

    project_operations.add_argument(
            '-c',
            '--create',
            dest='name',
            help='Create a new project')

    project_operations.add_argument(
            '-a',
            '--add-file',
            dest='file',
            help='Add verilog file to the project')

    parser_testbench = subparsers.add_parser(
            'testbench',
            help='Testbanch utilities',
            description='Testbench utilitires.')

    parser_synthetize = subparsers.add_parser(
            'synthetize',
            help='Synthetize design',
            description='Synthetize design.')

    parser_flash = subparsers.add_parser(
            'flash',
            help='Flash device',
            description='Flash device.')

    args = parser.parse_args()

    add_path()

    if hasattr(args, 'func'):
        args.func(args)


if __name__ == '__main__':
    main()

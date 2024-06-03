from argparse import ArgumentParser

from mrlgrl.project import add_file, clean, create_project, remove_file
from mrlgrl.quartus import add_path, check_path


def status(args):
    print('Quartus was ' + ('' if check_path() else 'not ') + 'found.')


def project(args):
    if args.name is not None:
        create_project(args.name)

    if args.add_file is not None:
        add_file(args.add_file)

    if args.remove_file is not None:
        remove_file(args.remove_file)

    if args.clean:
        clean()


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
    parser_project.set_defaults(func=project)

    project_operations = parser_project.add_mutually_exclusive_group(
            required=True)

    project_operations.add_argument(
            '-n',
            '--new',
            dest='name',
            help='Create a new project in current directory')

    project_operations.add_argument(
            '-a',
            '--add-file',
            dest='add_file',
            help='Add verilog file to the project')

    project_operations.add_argument(
            '-r',
            '--remove-file',
            dest='remove_file',
            help='Remove file from the verilog project')

    project_operations.add_argument(
            '-c',
            '--clean',
            dest='clean',
            help='Clean generated project files',
            action='store_true')

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

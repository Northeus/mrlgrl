from argparse import ArgumentParser

from mrlgrl.testbench import list_testbenches, run_cli, run_gui
from mrlgrl.project import add_file, clean, create_project, remove_file
from mrlgrl.quartus import add_path, check_path, flash, synthesize


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


def testbench(args):
    if args.list_testbenches:
        print('\n'.join(list_testbenches()))

    if args.module_cli is not None:
        run_cli(args.module_cli)

    if args.module_gui is not None:
        run_gui(args.module_gui)


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
    parser_testbench.set_defaults(func=testbench)

    testbench_operations = parser_testbench.add_mutually_exclusive_group(
            required=True)

    testbench_operations.add_argument(
            '-l',
            '--list',
            dest='list_testbenches',
            help='List found testbenches within the project',
            action='store_true')

    testbench_operations.add_argument(
            '-c',
            '--cli',
            dest='module_cli',
            help='Run testbench module in CLI')

    testbench_operations.add_argument(
            '-g',
            '--gui',
            dest='module_gui',
            help='Run testbench module in GUI and'
            ' create "run.do" re-compile script')

    parser_synthesize = subparsers.add_parser(
            'synthesize',
            help='Synthesize design',
            description='Synthesize the project in the current directory.')
    parser_synthesize.set_defaults(func=lambda _: synthesize())

    parser_flash = subparsers.add_parser(
            'flash',
            help='Flash device',
            description='Flash the project in the current directory.')
    parser_flash.set_defaults(func=lambda _: flash())

    args = parser.parse_args()

    add_path()

    if hasattr(args, 'func'):
        args.func(args)


if __name__ == '__main__':
    main()

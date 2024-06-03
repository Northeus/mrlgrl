import re
import subprocess

from pathlib import Path
from typing import Optional


def is_testbench(file: Path) -> bool:
    return file.is_file() and file.read_text().startswith('`timescale')


def find_module_file(module: str) -> Optional[Path]:
    return next(filter(lambda x: x.stem == module,
                       Path().glob(f'**/{module}.v')),
                None)


def list_testbenches() -> list[str]:
    return [x.stem for x in Path().glob('**/*.v') if is_testbench(x)]


def used_modules(file: Path) -> set[str]:
    modules = set()
    regex = re.compile(
            r'^\s*((?!module|reg|wire)\S+)\s+((?!module|reg|wire)\S+)\s*\(')

    with file.open() as f:
        for line in f:
            match = regex.match(line)

            if match is None:
                continue

            modules.add(match.group(1))

    return modules


def find_dependencies(testbench_filename: str) -> Optional[list[str]]:
    testbench_file = Path(testbench_filename)
    module_to_file: dict[str, Path] = {}

    if not is_testbench(testbench_file):
        print('Testbench file does not exist or start with "`timescale". :(')
        return

    queue = list(used_modules(testbench_file))

    while len(queue) > 0:
        module = queue.pop()

        if module in module_to_file:
            continue

        module_file = find_module_file(module)

        if module_file is None:
            print('Could not find file with module "{module}" :/')
            return

        module_to_file[module] = module_file

    return list(map(str, module_to_file.values()))


def run_gui(name: str) -> None:
    ...


def run_cli(name: str) -> None:
    file = find_module_file(name)

    if file is None:
        return

    deps = find_dependencies(file.name)

    if deps is None:
        return

    subprocess.run(['vsim',
                    '-c',
                    '-do',
                    f'vlog {" ".join(deps)} {str(file)}; vsim {name};'
                    'run -all; quit'])

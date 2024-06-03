import subprocess

from pathlib import Path
from typing import Optional


def find_project_file() -> Optional[Path]:
    files = list(Path().glob('*.qsf'))

    if len(files) == 0:
        print('Could not found a project. :(')
        return

    if len(files) > 1:
        print('Multiple projects were found in this directory :(')
        return

    return files[0]


def load_template(filename: str, project: str = '') -> Optional[str]:
    file = Path(__file__).parent / 'templates' / filename

    if not file.is_file():
        return None

    return file.read_text().replace('[project name]', project)


def create_project(name) -> None:
    project_template = load_template('project.tcl', name)
    project_v = load_template('project.v', name)
    segment_v = load_template('segment7.v')
    gitignore = load_template('gitignore.txt')

    if any(x is None for x in (project_template, project_v, segment_v)):
        print('Missing templates, contact lib author. :(')
        return

    if len(list(Path().glob('*.qsf'))) != 0:
        print('There is already some project. :(')
        return

    create_script = Path('create_project.tcl')

    create_script.write_text(project_template)
    Path(f'{name}.v').write_text(project_v)
    Path('segment7.v').write_text(segment_v)
    Path('.gitignore').write_text(gitignore)

    subprocess.run(['quartus_sh', '-t', 'create_project.tcl'])

    # create_script.unlink()

    print('Done')


def add_file(name: str) -> None:
    project_file = find_project_file()

    if project_file is None:
        return

    with project_file.open('a') as f:
        f.writelines(f'\nset_global_assignment -name VERILOG_FILE {name}')


def remove_file(name: str) -> None:
    project_file = find_project_file()

    if project_file is None:
        return

    with project_file.open('r') as f:
        lines = f.readlines()

    with project_file.open('w') as f:
        for line in lines:
            if f'set_global_assignment -name VERILOG_FILE {name}' in line:
                continue

            f.write(line)


def clean() -> None:
    project_file = find_project_file()

    if project_file is None:
        return

    subprocess.run(['quartus_sh', '--clean', str(project_file.stem)])

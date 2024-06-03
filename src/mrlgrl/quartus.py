import os

from pathlib import Path
from typing import Optional


def check_path() -> bool:
    return all(x in os.environ['PATH']
               for x in ('quartus/bin', 'modelsim_ase/bin'))


def find_intel_dir() -> Optional[Path]:
    intel_lite_dir = Path.home() / 'intelFPGA_lite'

    if not intel_lite_dir.is_dir():
        return

    return next(filter(lambda x: x.is_dir(), intel_lite_dir.iterdir()),
                None)


def add_path() -> None:
    if check_path():
        return

    intel_dir = find_intel_dir()

    if intel_dir is None:
        return

    quartus_bin_dir = intel_dir / 'quartus' / 'bin'
    modelsim_bin_dir = intel_dir / 'modelsim_ase' / 'bin'

    if not (quartus_bin_dir.is_dir() and modelsim_bin_dir.is_dir()):
        return

    paths = [str(x.absolute()) for x in (quartus_bin_dir, modelsim_bin_dir)]
    os.environ['PATH'] += os.pathsep + os.pathsep.join(paths)

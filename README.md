# Mrlgrl
CLI for Quartus II project on DE1-SoC boards.
To ensure the application works properly,
names of files must match the names of the module stored in them.

## Installation
Simply run:
```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ mrlgrl
```

For the installation from sources use either `make install-dev` or `make install`.

## Usage
To use the application see `mrlgrl -h` for the help, or `mrlgrl [module] -h`.
You have to execute every command within the project folder.

The Quartus II binaries are automatically detected, use `mrlgrl status` to see,
if the Quartus II was found. If the automatic detection failed, you have to
add the paths manually to your environment PATH. For example use `source env.sh`:
```sh
# Update following paths based on your environment
export QUARTUS_ROOTDIR=~/intelFPGA_lite/20.1/quartus
export MODELSIM_ROOTDIR=~/intelFPGA_lite/20.1/modelsim_ase

export PATH=$QUARTUS_ROOTDIR/bin:$MODELSIM_ROOTDIR/bin:$PATH
```

You have to use all the commands within the folder with the project.

### Project
To create a new Quartus II project for DE1-SoC boards use `mrlgrl project -n [project name]`.

To add or remove files within the project use:
 * `mrlgrl project -a [file to add]`
 * `mrlgrl project -r [file to remove]`

To clean the generated files inside the project call `mrlgrl project -c`.

### Synthesize
To synthesize the project simply use `mrlgrl synthesize`.

### Flash
To upload the binary to DE1-SoC device `mrlgrl flash`.

### Testbench
This tool detects all the testbenches which files starts with '\`timescale'.
You can list available tesbenches in the project via `mrlgrl testbench -l`.

After that, you can run a given testbench either in CLI or GUI mode:
 * CLI: `mrlgrl testbench -c [module name]`
 * GUI: `mrlgrl testbench -g [module name]`

The GUI mode also creates a `run.do` script which re-compile the project and update the waveforms.
You can run this script within the ModelSim console via `do run.do`. This script is generated
before the GUI is opened and removed after you close the GUI.

## Versions
 - 0.0.1:
   * Prototype for testing.
 - 0.0.2:
   * Fixed adding recursive modules for testbenches.
   * Fixed regex to find testbench modules.

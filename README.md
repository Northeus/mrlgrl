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

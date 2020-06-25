#!/bin/bash

rootDir="$PWD"

mkdir -p thirdparty
cd thirdparty || exit 1

# Install yapf.
if [ ! -d yapf ]
then
    git clone https://github.com/google/yapf.git
fi
cd yapf || exit 1
mkdir -p build/lib/python
PYTHONPATH=build/lib/python python2.7 setup.py install --home build
# Test.
PYTHONPATH=build/lib/python build/bin/yapf --help
if [ $? -ne 0 ]
then
    echo "Install yapf failed, return code: $?."
    exit 1
fi
# Generate style file.
cd ../.. || exit 1
mkdir -p config
PYTHONPATH=thirdparty/yapf/build/lib/python \
    thirdparty/yapf/build/bin/yapf          \
    --style="google"                        \
    --style-help                            \
    > config/yapf.cfg
if [ $? -ne 0 ]
then
    echo "Generate default config file failed, return code: $?"
fi

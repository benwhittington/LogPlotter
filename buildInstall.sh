#!/usr/bin/bash
python3 setup.py bdist_wheel
pip3 install ./dist/*.whl --force-reinstall


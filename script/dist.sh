#!/bin/bash

pip install -Ur requirements.txt

rm -rf buid dist lintaosp.egg-info/

python setup.py sdist bdist_wheel
python -m twine upload dist/*

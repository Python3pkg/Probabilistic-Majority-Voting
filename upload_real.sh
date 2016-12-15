#!/bin/bash

python setup.py register -r pypi
python setup.py sdist bdist_wheel upload -r pypi

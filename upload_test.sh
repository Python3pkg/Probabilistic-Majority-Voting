#!/bin/bash

python setup.py register -r pypitest
python setup.py sdist bdist_wheel upload -r pypitest

#!/bin/bash

export TESTING=true
$PWD/python3-virtualenv/bin/python -m unittest discover -v tests/
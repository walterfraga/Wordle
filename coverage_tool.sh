#!/bin/bash
PWD=$(pwd)
export PYTHONPATH=$PWD/src:$PYTHONPATH
coverage run -m unittest discover test
coverage report -m --omit=$PWD/test/*

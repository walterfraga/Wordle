#!/bin/bash
export PYTHONPATH=/home/wfraga/PycharmProjects/Wordle/src:$PYTHONPATH
coverage run -m unittest discover test
coverage report -m

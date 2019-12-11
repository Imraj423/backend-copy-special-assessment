#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "???"


def get_special_paths(dir):
    result = []
    fnames = os.listdir(dir)
    for name in fnames:
        if re.match(r'.+\_\_\w+\_\_.+', name):
            print(name)
            result.append(name)
            # print(path)
    return result
# os.path.abspath('xyz_hello_.txt')
# os.path.abspath('zz_something_.jpg')


def copy_to(paths, dir):
    if not os.path.exists(os.path.abspath(dir)):
        os.makedirs(os.path.abspath(dir))
    for path in paths:
        shutil.copy(path, os.path.abspath(dir))


def zip_to(paths, zippath):
    cmd = 'zip -j {} '.format(zippath) + " ".join(paths)
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    print output

# +++your code here+++
# Write functions and modify main() to call them

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='origin dir for special files')
    results = parser.parse_args()

    if not results:
        parser.print_usage()
        sys.exit(1)

    todir = results.todir
    from_dir = results.from_dir
    tozip = results.tozip
    result = get_special_paths(from_dir)
    if todir:
        copy_to(result, todir)
    elif tozip:
        zip_to(path, tozip)
    else:
        print "\n".join(result)
    # Read the docs and examples for the argparse module about how to do this.
# wefwef
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()


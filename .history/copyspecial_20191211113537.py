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
__author__ = "Imraj423"


def get_special_paths(dir):
    result = []
    fnames = os.listdir(dir)
    for name in fnames:
        if re.match(r'.+\_\_\w+\_\_.+', name):
            print(name)
            result.append(os.path.abspath(name))
    return result


def copy_to(paths, dir):
    if not os.path.exists(os.path.abspath(dir)):
        os.makedirs(os.path.abspath(dir))
    for path in paths:
        shutil.copy(path, os.path.abspath(dir))


def zip_to(files, zip_dir):
    """given a list of paths, zip those files up into the given zipfile"""
    cmd = ['zip', '-j', zip_dir]
    cmd.extend(files)
    print("Command I\'m running is: {}".format(" ".join(cmd)))
    subprocess.call(cmd)
    return 0


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
        zip_to(result, tozip)
    else:
        print "\n".join(result)


if __name__ == "__main__":
    main()

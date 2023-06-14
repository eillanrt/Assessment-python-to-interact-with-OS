#!/usr/bin/env python

import sys
import subprocess

file_name = sys.argv[1]
print(file_name)
with open(file_name, 'r') as old_files:
    lines = old_files.readlines()

    for line in lines:
        updated_line = line.strip().replace('jane', 'jdoe')

        subprocess.run(['mv', line.strip(), updated_line])
    old_files.close()

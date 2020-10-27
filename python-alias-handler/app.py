#!/usr/bin/python
import os
import subprocess

data_folder = os.path.join(os.path.expanduser('~'))
file_to_open = ".bash_aliases"
alias = input(" Enter command alias => ")
cmd = input(" Enter command  => ")

cmd_alias = f"alias {alias}='{cmd}'"
print(cmd_alias)

hs = open(os.path.join(data_folder, file_to_open), 'a+')
hs.write(cmd_alias + "\n")
hs.close()

#!/usr/bin/python
import os
import subprocess

data_folder = os.path.join(os.path.expanduser('~'))
file_to_open = "bash_alias"
alias = input(" Enter command alias => ")
cmd = input(" Enter command  => ")
print(alias)
print(type(alias))

cmd_alias = "alias " + str(alias) + "='" + str(cmd) + "'"
print(cmd_alias)

hs = open(os.path.join(file_to_open), 'a+')
hs.write(cmd_alias + "\n")
hs.close()

subprocess.call("/home/anandhu/Desktop/ask/python-alias-handler/source_update.sh", shell=True)


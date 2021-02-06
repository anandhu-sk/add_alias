import os
import pathlib
from pathlib import Path
home = str(Path.home())
src_file = '.zshrc'

def create_alias_file():
    fname = 'bash_alias'
    f = open(os.path.join(fname), 'w+')

    print(pathlib.Path(__file__).parent.absolute())
    full_path = os.path.join(pathlib.Path(__file__).parent.absolute(), fname)
    print(full_path)
    f.close()
    return full_path

def link_to_zshrc_file(full_path):
    link_alias_to_zshrc = f"""\nif [ -f {full_path} ]; then
        . {full_path}\nfi
"""
    print(link_alias_to_zshrc)
    p = os.path.join(home, src_file)
    f = open(p, 'a')
    f.write(link_alias_to_zshrc)
    f.close()

def add_alias():
    full_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "app.py")

    add_alias = f"\nalias add_alias='python {full_path} '"
    aa = f"\nalias aa='python {full_path}'"
    p = os.path.join(home, src_file)

    f = open(p, 'a')
    f.write(add_alias)
    f.write(aa)
    f.close()


f_path = create_alias_file()
link_to_zshrc_file(f_path)
add_alias()





#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of web_static
using do_pack.
Name of folder: web_static_<year><month><day><hour><minute>
"""
from fabric.api import local, task


@task
def do_pack():
    """Pack all web_static directory and it's contents into .tgz file

    Return:
        The archive path if archive was successfully created else None
    """
    from os import system
    from datetime import datetime
    dir_name = 'versions/'
    fmt = datetime.now().strftime('%Y%m%d%H%M')
    file_name = f"web_static_{fmt}"
    system(
        "if ! [ -d versions ];then mkdir versions;fi")
    local(f"tar --mode=664 -cvzf {dir_name}{file_name}.tgz web_static")

#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of web_static
using do_pack.
Name of folder: web_static_<year><month><day><hour><minute>
"""
from fabric.api import local, task, puts


@task
def do_pack():
    """Pack all web_static directory and it's contents into .tgz file

    Return:
        The archive path if archive was successfully created else None
    """
    from os import system
    from datetime import datetime
    import os
    dir_name = 'versions/'
    fmt = datetime.now().strftime('%Y%m%d%H%M')
    file_name = f"web_static_{fmt}"
    tar_file = f"{dir_name}{file_name}.tgz"
    system(
        "if ! [ -d versions ];then mkdir versions;fi")
    puts(f'Packing web_static to {tar_file}')
    local(f"tar -cvzf {tar_file} web_static")
    puts(f'web_static packed: {tar_file} -> {os.path.getsize(tar_file)}Bytes')

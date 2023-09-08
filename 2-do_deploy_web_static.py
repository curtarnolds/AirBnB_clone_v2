#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of web_static
using do_pack.
Name of folder: web_static_<year><month><day><hour><minute>
"""
from fabric.api import *


env.hosts = ['54.87.209.173', '54.144.148.21']
env.user = 'ubuntu'


def do_pack():
    """Pack all web_static directory and it's contents into .tgz file

    Return:
        The archive path if archive was successfully created else None
    """
    from os import system, path
    from datetime import datetime
    dir_name = 'versions/'
    fmt = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f"web_static_{fmt}"
    tar_file = f"{dir_name}{file_name}.tgz"
    system(
        "if ! [ -d versions ];then mkdir versions;fi")
    puts(f'Packing web_static to {tar_file}')
    pack = local(f"tar -cvzf {tar_file} web_static")
    puts(f'web_static packed: {tar_file} -> {path.getsize(tar_file)}Bytes')
    if pack.succeeded:
        return tar_file
    else:
        return False


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    from os import path
    if path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False

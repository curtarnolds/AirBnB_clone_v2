#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of web_static
using do_pack.
Name of folder: web_static_<year><month><day><hour><minute>
"""
from fabric.api import local, puts, put, run, env


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


def do_deploy(archive_path=None):
    """Distributes an archive to web servers.

    Args:
        archive_path: The path to archive
    """
    from os import path
    if path.exists(archive_path):
        put(archive_path, '/tmp/')
        archive = archive_path.rsplit('/', 1)[1]
        remote_path = archive.rsplit('.', 1)[0]
        wstatic = '/data/web_static'
        run(f'sudo mkdir -p {wstatic}/releases/{remote_path}/')
        run(f'sudo tar -xzf /tmp/{archive} -C \
                          {wstatic}/releases/{remote_path}/')
        run(f'sudo mv -f {wstatic}/releases/{remote_path}/web_static/* \
                       {wstatic}/releases/{remote_path}/')
        run(f'sudo rm -rf {wstatic}/releases/{remote_path}/web_static/ \
                     /tmp/{archive} {wstatic}/current')
        run(f'sudo ln -s {wstatic}/releases/{remote_path}/ {wstatic}/current')
        puts('New version deployed!')
        return True
    return False

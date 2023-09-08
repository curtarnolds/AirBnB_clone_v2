#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.87.209.173', '54.144.148.21', 'localhost']


def do_pack():
    """
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        sudo("sudo mkdir -p {}".format(newest_version))
        sudo("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        sudo("sudo rm {}".format(archived_file))
        sudo("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        sudo("sudo rm -rf {}/web_static".format(newest_version))
        sudo("sudo rm -rf /data/web_static/current")
        sudo("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False

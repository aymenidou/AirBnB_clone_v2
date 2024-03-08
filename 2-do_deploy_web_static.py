#!/usr/bin/python3
"""module for automating website deployment"""
from datetime import datetime
import os
from fabric.operations import local, put, run
from fabric.api import runs_once, local, env

env.hosts = ["54.167.96.145", "34.239.254.105"]


def do_pack():
    """this function pack our site in a tgz file"""
    if (not os.path.exists("versions")):
        os.mkdir("versions")
    time = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second)
    print("Packing web_static to ".format(archive_path))
    local("tar -cvzf {} web_static".format(archive_path))
    file_detail = os.stat(archive_path)
    print("web_static packed: {} -> {}Bytes\n".format(archive_path,
                                                      file_detail.st_size))
    return archive_path


def do_deploy(archive_path):
    """this function deploy our website to the servers"""
    if (not os.path.exists(archive_path)):
        return False

    path_nx = os.path.splitext(archive_path)[0]
    path_nx = path_nx.split('/')[-1]
    path_yx = path_nx + '.tgz'

    try:
        put(archive_path, "/tmp/")

        run('mkdir -p /data/web_static/releases/{:s}/'.format(path_nx))

        run('tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}/'.
            format(path_yx, path_nx))

        run('rm /tmp/{:s}'.format(path_yx))

        run('mv /data/web_static/releases/{:s}/web_static/*'
            ' /data/web_static/releases/{:s}/'.
            format(path_nx, path_nx))

        run('rm -rf /data/web_static/releases/{:s}/web_static'.format(path_nx))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{:s}/ /data/web_static/current'.
            format(path_nx))
        print('New version deployed!')
        return True
    except Exception:
        return False

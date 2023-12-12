#!/usr/bin/python3
"""module for automating website deployment"""
from datetime import datetime
import os
from fabric.api import local, env, put, run, runs_once

env.hosts = ["54.236.49.164", "52.86.203.42"]


# @runs_once
# def do_pack():
#     """this function pack our site in a tgz file"""
#     if (not os.path.exists("versions")):
#         os.mkdir("versions")
#     time = datetime.now()
#     archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
#         time.year,
#         time.month,
#         time.day,
#         time.hour,
#         time.minute,
#         time.second)
#     print("Packing web_static to ".format(archive_path))
#     local("tar -cvzf {} web_static".format(archive_path))
#     file_detail = os.stat(archive_path)
#     print("web_static packed: {} -> {}Bytes\n".format(archive_path,
#                                                       file_detail.st_size))
#     return archive_path


def do_deploy(archive_path):
    """this function deploy our website to the servers"""
    if (not os.path.exists(archive_path)):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace('.tgz', '')
    extraction_path = "/data/web_static/releases/{}".format(folder_name)
    print(file_name)
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(extraction_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, extraction_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/ ".format(extraction_path, extraction_path))
        run("rm -rf {}/web_static/ ".format(extraction_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(extraction_path))
        print('New version deployed!')
        return True
    except Exception:
        return False

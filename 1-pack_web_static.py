#!/usr/bin/python3
"""module for automating website deployment"""
from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """this function pack our site in a tgz file"""
    if (not os.path.exists("versions")):
        os.mkdir("versions")
    time = datetime.now()
    fileName = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second)
    print("Packing web_static to ".format(fileName))
    local("tar -cvzf {} web_static".format(fileName))
    fileDetail = os.stat(fileName)
    print("web_static packed: {} -> {}Bytes\n".format(fileName, fileDetail.st_size))
    print("Done")
    return fileName

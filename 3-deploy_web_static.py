#!/usr/bin/python3
"""Full Deployment Module"""


import time
from fabric.operations import local
from fabric.api import *
from os import path
env.hosts = ["34.139.7.21", "18.207.134.95"]


def do_pack():
    """Function compressing files

    Returns:
        archive(str): if correctly generated
        None: otherwise
    """

    local("sudo mkdir -p versions")
    c_time = time.localtime(time.time())
    if int(c_time.tm_mon) < 10:
        c_mon = "0{}".format(c_time.tm_mon)
    else:
        c_mon = c_time.tm_mon
    pname = "{}{}{}{}{}{}".format(c_time.tm_year, c_mon,
                                  c_time.tm_mday, c_time.tm_hour,
                                  c_time.tm_min, c_time.tm_sec)
    full_path = "versions/web_static_{}.tgz".format(pname)
    archive = local("sudo tar -cvzf {} ./web_static/".format(full_path))
    if archive.failed:
        return None
    return full_path


def do_deploy(archive_path):
    """ Distributes archives to web server

    Arguments:
        archiev_path(str): path to the archive

    Returns:
        False(bool): if path doesn't exist
    """
    if path.exists(archive_path):
        put(archive_path, "/tmp/")
        strip_name = archive_path.split("/")[-1][:-4]
        run("sudo mkdir -p /data/web_static/releases/{}".format(strip_name))
        run("sudo tar -xzf /tmp/{}.tgz -C".format(strip_name) +
            "/data/web_static/releases/{}/".format(strip_name))
        run("sudo rm /tmp/{}.tgz".format(strip_name))

        run("sudo mv /data/web_static/releases/{}/web_static/* "
            .format(strip_name) +
            "/data/web_static/releases/{}/".format(strip_name))

        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(strip_name))

        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -snf /data/web_static/releases/{}/ ".format(strip_name) +
            "/data/web_static/current")
        return True
    return False


def deploy():
    """Deployment task"""
    pat = do_pack()
    if path.exists(str(pat)):
        return do_deploy(pat)
    return False

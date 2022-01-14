#!/usr/bin/python3
"""Fabric Script Generating .tgz and
deploys archive to the web servers"""


from fabric.api import *
from os import path
env.hosts = ["18.207.134.95", "34.139.7.21"]


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
        run("sudo ln -sfn /data/web_static/releases/{}/ ".format(strip_name) +
            "/data/web_static/current")
        return True
    return False

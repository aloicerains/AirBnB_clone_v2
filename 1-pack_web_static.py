#!/usr/bin/python3
"""Fabric Script Generating .tgz from web_static folder"""


import time
from fabric.operations import local


def do_pack():
    """Function compressing files

    Returns:
        arpath(str): if correctly generated
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
    if archive:
        return archieve
    else:
        return None

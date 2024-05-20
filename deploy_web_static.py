#!/usr/bin/python3
""" This script deploys a web app
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
from os import getenv
from dotenv import load_dotenv

load_dotenv()

env.hosts = [getenv("HOST_WEB_2")]
env.key_filename = getenv("HOST_PRIVET_KEY")
env.user = getenv("USER_WEB_2")

def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} cli_frontend server .env".format(file_name))
        return file_name
    except:
        return None
    
def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('rm -rf /data/web_static/releases/*')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
    
def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
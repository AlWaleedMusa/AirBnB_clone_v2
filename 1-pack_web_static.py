#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Create the file name for the archive
        now = datetime.now()
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Generate the .tgz archive
        local("tar -cvzf versions/{} web_static".format(file_name))

        # Return the archive path
        return "versions/{}".format(file_name)
    except Exception as e:
        print(e)
        return None

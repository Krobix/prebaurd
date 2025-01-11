import bottle
import os, sys
import multiprocessing as mp
import subprocess as sp

HOME = os.getenv("HOME")
prefix = f"{HOME}/.local/share/prebaurd"

DEFAULT_CONFIG = {
    "servers": [], #strinsg containing addresses for client
    "packages": [], #(not used for client) list of dicts with two fields: name and version. version can be blank
    "check_interval_mins": 1440, #by default check once a day (for server)
}

def mkdirif(dir, wipe=False):
    if not os.path.isdir(dir):
        os.mkdir(dir)

    elif wipe:
        os.system(f"rm -rf {dir}")

class Package:
    def __init__(self, name):
        #Object that represents a package during the build process.
        self.name = name

    def build(self):
        proc = sp.run(["pikaur", "-Sw", "--noconfirm", "--noedit", "--nodiff", "--skip-failed-build", self.name])




def start_server():
    mp.set_start_method("forkserver")

#!usr/bin/env Python
"""
Content manager: maintain load file and content log
"""

import os


def reconfig_dir():
    if 'content' not in os.listdir():
        os.mkdir(path="./content")
        dir_contents = os.listdir("./content")
        if ".loadfile" not in dir_contents:
            pass
        if ".contentlog" not in dir_contents:
            pass


def on_startup():
    reconfig_dir()


def update_log(file_nm: str):
    with open(file=".contentlog", mode="a") as log_file:
        log_file.write(f"{file_nm}\n")

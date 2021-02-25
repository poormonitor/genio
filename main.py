# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:32
# @Author  : Johnson Sun (@poormonitor)
# @Email   : poormonitor@outlook.com
# @File    : main.py

import names
import subprocess
import os
import platform


def pythoncmd():
    if platform.system() == "Linux":
        return "python3"
    else:
        return "python"


def gen(exe):
    genin = subprocess.run("%s ran.py" % pythoncmd(), shell=True, capture_output=True).stdout.decode()[::-1].replace(
        "\n", "", 1).replace("\r", "", 1)[::-1]
    genout = subprocess.run(exe, input=bytes(genin, encoding="UTF-8"), shell=True,
                            capture_output=True).stdout.decode()[::-1].replace("\n", "", 1).replace("\r", "", 1)[::-1]
    return genin, genout


def genfile(cmd):
    name = names.get_last_name().lower()
    genin, genout = gen(cmd)
    filein = open("io/" + name + ".in", 'w')
    fileout = open("io/" + name + ".out", "w")
    filein.write(genin)
    fileout.write(genout)
    filein.close()
    fileout.close()


if __name__ == "__main__":
    cmd = input("Input your command (eg. %s code.py): " % pythoncmd())
    times = input("Input pair numbers (default: 20) : ")
    if times == "":
        times = 20
    else:
        times = int(times)
    if cmd == "":
        cmd = "%s code.py" % pythoncmd()
    if not os.path.exists("io"):
        os.mkdir("io")
    for i in range(times):
        genfile(cmd)

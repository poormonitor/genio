# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:32
# @Author  : Johnson Sun (@poormonitor)
# @Email   : poormonitor@outlook.com
# @File    : main.py

import names
import subprocess


def gen(exe):
    genin = subprocess.run("python ran.py", shell=True, capture_output=True).stdout.decode()
    genout = subprocess.run(exe, input=bytes(str(genin), encoding="UTF-8"), shell=True, capture_output=True).stdout.decode()
    return genin, genout


def genfile(cmd):
    name = names.get_last_name().lower()
    genin, genout = gen(cmd)
    filein = open(name + ".in", 'w')
    fileout = open(name + ".out", "w")
    filein.write(genin)
    fileout.write(genout)
    filein.close()
    fileout.close()


if __name__ == "__main__":
    cmd = input("Input your command (eg. python code.py): ")
    times = input("Input pair numbers (default: 20) : ")
    if times == "":
        times = 20
    else:
        times = int(times)
    for i in range(times):
        genfile(cmd)

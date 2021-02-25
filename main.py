# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:32
# @Author  : Johnson Sun (@poormonitor)
# @Email   : poormonitor@outlook.com
# @File    : main.py

import names
import subprocess


def replace_last(string, find, replace):
    reversed = string[::-1]
    replaced = reversed.replace(find[::-1], replace[::-1], 1)
    return replaced[::-1]


def gen(exe):
    genin = subprocess.run("python ran.py", shell=True, capture_output=True).stdout.decode()
    genin = replace_last(genin, "\n", "")
    genout = subprocess.run(exe, input=bytes(str(genin), encoding="UTF-8"), shell=True,
                            capture_output=True).stdout.decode()
    return genin, genout


def genfile(cmd):
    name = names.get_last_name().lower()
    genin, genout = gen(cmd)
    filein = open("code/" + name + ".in", 'w')
    fileout = open("code/" + name + ".out", "w")
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
    if cmd == "":
        cmd = "python code.py"
    for i in range(times):
        genfile(cmd)

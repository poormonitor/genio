# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:33
# @Author  : Johnson Sun (@poormonitor)
# @Email   : poormonitor@outlook.com
# @File    : generate.py


import subprocess
import random
def gen(exe):
    genin=random.randint(1,100000)
    genout=subprocess.run(exe,input=bytes(str(genin),encoding="UTF-8"),shell=True,capture_output=True)
    return (str(genin),genout.stdout.decode())
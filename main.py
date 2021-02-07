# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:32
# @Author  : Johnson Sun (@poormonitor)
# @Email   : poormonitor@outlook.com
# @File    : main.py

command=input("Input your command:")
times=int(input("Input pair numbers:"))
from generate import gen
import names
def generate(cmd):
    name=names.get_last_name().lower()
    genin,genout=gen(cmd)
    filein=open(name+".in",'w')
    fileout=open(name+".out","w")
    filein.write(genin)
    fileout.write(genout)
    filein.close()
    fileout.close()
for i in range(times):
    generate(command)
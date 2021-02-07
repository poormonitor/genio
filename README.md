## Introduction

年轻人，是否曾因为评测数据而苦恼？
年轻人，是否因手打评测数据而老眼昏花？
现在，你可以用Genio自动生成评测数据！

## Usage

Clone代码并安装names模块。

```shell
git clone https://github.com/poormonitor/genio.git
cd genio
pip install -r requirements.txt
```

在运行前，需在ran.py中配置生成随机输入的代码，这里提供几种参考：

eg. 1
```python
import random

#生成1-10000间的整数
out = random.randint(1,10000)
print(out) #必须print输出
```
eg. 2
```python
import random

#生成1-50行，每行5-50个数字，数字范围是1-5
out = ""
row = random.randint(1, 50)
num = random.randint(5, 50)
for i in range(row):
    for i in range(num):
        out = out + str(random.randint(1, 5)) + " "
    out = out + "\n"
print(row, num, sep=" ") #第一行为接下来的行数与数字数
print(out) #必须print输出
```

接着，可以运行main.py：

```shell
python main.py
```

程序会要求输入两个参数：

1、运行指令。比如python code.py，要求该shell能够在输入后输出正解。（非解释型语言请先编译）

2、生成对数。默认20，即在同目录下生成20对in与out。输出时，会采用随机英文名，并保证配对。

## Attention

考虑到不同系统换行符不同，尽可能在服务器同操作系统下进行。跨系统可能导致OJ出错。

## LICENSE

[GPL v3][3]

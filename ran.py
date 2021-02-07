import random

out = ""
row = random.randint(1, 50)
num = random.randint(5, 50)
for i in range(row):
    for n in range(num):
        out = out + str(random.randint(1, 5)) + " "
    out = out + "\n"
print(row, num, sep=" ")
print(out)

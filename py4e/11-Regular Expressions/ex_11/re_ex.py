# if you want to use a module you cant name the file the same name as the module !! the more you know

import re

fh = open("regex_sum_1495525.txt")
fr = fh.read()

num = re.findall("[0-9]+", fr)

for i in range(len(num)):
    num[i] = int(num[i])

print(sum(num))
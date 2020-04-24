#!/usr/bin/env python
# Created by YHJin 2019.10.8 15:26
# Require file: structure.in created by createStructure.py
# How to use: check_pos.py
import math
import re

regex = re.compile("\s+")
count = 0
error = 0
with open("structure.in", "r") as f:
    lines = f.readlines()

for i in range(1, len(lines)):
    # x, y, z
    check_point_1 = regex.split(lines[i])[2:5]
    for j in range(len(lines)-1, i, -1):
        check_point_2 = regex.split(lines[j])[2:5]
        sub_x = (float(check_point_1[0]) - float(check_point_2[0]))
        sub_y = (float(check_point_1[1]) - float(check_point_2[1]))
        sub_z = (float(check_point_1[2]) - float(check_point_2[2]))
        distance_square = sub_x**2 + sub_y**2 + sub_z**2
        distance = math.sqrt(distance_square)
        count += 1
        if distance < 1.7:
            error += 1
            print(check_point_1, check_point_2)
            print(distance)
        else:
            pass
print("Total checked: %d distance, %d error positions found." % (count,error))

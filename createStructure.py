#!/usr/bin/env python
import re
import math
import sys
from compiler.ast import flatten
from decimal import *

def read_pos(filename):
	with open(filename, "r") as f:
		lines = f.readlines()
	return lines

def is_hex(lattice_line):
#**********************************************************
#***!!! For convenience, I write the func like this. !!!***
#***!!! However, in real condictions, it should be   !!!***
#***!!! writen using the angles between Vectors.     !!!***
#**********************************************************
	Hexagonal = False
	for line in lattice_line:
		for num in line:
			if float(num) < 0:
				Hexagonal = True
				break
			else:
				pass
	return Hexagonal

def dir2car(pos_line, lattice_line):
	angle = Decimal(str(math.sqrt(3)))
	x = Decimal(pos_line[0])
	y = Decimal(pos_line[1])
	z = Decimal(pos_line[2])
	Ax = Decimal(lattice_line[0][0])
	Ay = Decimal(lattice_line[0][1])
	Az = Decimal(lattice_line[0][2])
	Bx = Decimal(lattice_line[1][0])
	By = Decimal(lattice_line[1][1])
	Bz = Decimal(lattice_line[1][2])
	Cx = Decimal(lattice_line[2][0])
	Cy = Decimal(lattice_line[2][1])
	Cz = Decimal(lattice_line[2][2])
	car_y = y*Ay + y*By + y*Cy
	car_z = z*Az + z*Bz + z*Cz
	bohr_constant = Decimal("0.5291772")
	Hexagonal = is_hex(lattice_line)
	# print(car_y ,car_z)
	if not Hexagonal:
		car_x = x*Ax + x*Bx + x*Cx
	else:
		car_x = x*Ax - car_y / angle
	car_x_bohr = car_x/bohr_constant
	car_y_bohr = car_y/bohr_constant
	car_z_bohr = car_z/bohr_constant
	return str('%.15f' %car_x_bohr), str('%.15f' %car_y_bohr), str('%.15f' %car_z_bohr), Hexagonal, str('%.15f' %car_x), str('%.15f' %car_y), str('%.15f' %car_z)

def get_label(regex, lines):
	# get label and num
	label_list = regex.split(lines[5].strip())
	number_list = regex.split(lines[6].strip())
	total_labels = list()
	fin_list = list()
	for i in range(len(label_list)):
		total_labels.append((label_list[i] + " ") * int(number_list[i]))
		fin_list.append(total_labels[i].strip().split(" "))

	return flatten(fin_list)

def is_fix(fix_in):
	if fix_in == "T":
		return True
	else:
		return False

def drop_zero_lines():
	pass



def main():
	try:
		sys.argv[1]
	except Exception as ret:
		print("   Usage: createStructure.py POSCAR.")
		exit()
	filename = sys.argv[1]
	lines = read_pos(filename)
	regex = re.compile('\s+')
	# get lattice
	lattice_lines = lines[2:5]
	lattice_line = list()
	for i in range(0,3):
		lattice_line.append(regex.split(lattice_lines[i].strip()))
	# get label & support CONTCAR
	label_list = get_label(regex, lines)
	count_non_zero_lines = len(label_list) + 9
	count_total_lines = len(lines)
	count_useless_line = count_total_lines - count_non_zero_lines
	if count_useless_line == 0:
		pass
	else:
		lines = lines[:-count_useless_line]
	# get pos
	pos_lines = lines[9:]
	pos_list = list()
	out_string_list = list()
        out_string_list_2 = list()
	for i in range(0, len(pos_lines)):
		pos_line = regex.split(pos_lines[i].strip())
		x = pos_line[0]
		y = pos_line[1]
		z = pos_line[2]
		fix_in = pos_line[3]
		car_x, car_y, car_z, Hexagonal, x, y, z = dir2car([x, y, z], lattice_line)
		if is_fix(fix_in):
			fix_flag = " 1"
		else:
			fix_flag = " 0"
		out_string = '{0:>3}{1:>3}{2:>20}{3:>20}{4:>20}{5:>3}'.format("ion", 
				str(label_list[i]), car_x, car_y, car_z, fix_flag)
		out_string_list.append(out_string)
		out_string_2 = '{0:>3}{1:>20}{2:>20}{3:>20}'.format(str(label_list[i]), x, y, z)
		out_string_list_2.append(out_string_2)
	# write to file
	with open("structure.in", "w") as f:
		for line in out_string_list:
			f.write(line + "\n")
	with open("Input.xyz", "w") as f:
		f.write(str(len(label_list)))
		f.write("\n")
		f.write("Created by createStructure.py\n")
		for line in out_string_list_2:
			f.write(line + "\n")


if __name__ == "__main__":
	main()

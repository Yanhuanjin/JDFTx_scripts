#!/usr/bin/env python
# Created by YHJin 2019.7.13 12:29
# Require file: POSCAR
# How to use: ang2bohr.py

def log():
	print ">> Generation Complete.\nPlease make sure:\n 1. The crystal system is right.\n 2. You know how it works!!!\n"

def read_POS():
	try:
		with open('POSCAR','r') as f:
			lines = f.readlines()
		total_list = list()
		for i in range(2, 5):
			line = lines[i]
			line_list = convert(line)
			total_list.append(line_list)
		return (total_list)
	except Exception as ret:
		print "'POSCAR' NOT FOUND OR WRONG FILE'.\nPLEASE PUT 'POSCAR' FILE IN PATH !!!"
		exit()

def convert(line):
	i_list = list()
	split_line = line.split(' ')
	for item in split_line:
		if item != '':
			i = float(item)/0.52917706 # 1 Angstrom = 0.5291772 Bohr
			i_list.append(i)
	return i_list	

def is_hex(pos_line):
	Hexagonal = False
	for line in pos_line:
		for num in line:
			if num < 0:
				Hexagonal = True
				break
			else:
				pass
	return Hexagonal

def main():
	# Format output
	pos_line = read_POS()
	hex = is_hex(pos_line)
	with open("lattice.in", 'w') as f:
		f.write("lattice\\"+"\n")
		if not hex:
			print("The crystal system is: Orthorhombic.\n")
			for line in pos_line:
				for num in line:
					f.write("%.15f" %num + " "),
				f.write("\\\n")
		else:
			print('The crystal system is: Hexagonal.\n')
			a = pos_line[0][0]
			c = pos_line[-1][-1]
			f.write("Hexagonal\\\n%.15f\\\n%.15f" %(a, c)),
	log()


if __name__ == "__main__":
	main()

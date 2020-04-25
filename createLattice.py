#!/usr/bin/env python
# Created by YHJin 2019.7.13 12:29
# Require file: POSCAR
# How to use: createLattice.py POSCAR
import sys

def log():
"""
print log.
"""
	print ">> Generation Complete.\nPlease make sure:\n 1. The crystal system is right.\n 2. You know how it works!!!\n"

def read_POS(filename):
"""
Read the POSCAR/CONTCAR lines2-5, which determine the lattice type. Return a list.
"""
	try:
		with open(filename,'r') as f:
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
"""
Convert the lattice constant from Angstrom to Bohr.
"""
	i_list = list()
	split_line = line.split(' ')
	for item in split_line:
		if item != '':
			i = float(item)/0.52917706 # 1 Angstrom = 0.5291772 Bohr
			i_list.append(i)
	return i_list	

def is_hex(pos_line):
"""
Judge if the lattice type is Hexagonal or Orthorhombic. Not completed yet. (Other types including Triclinic, Monoclinic, Tetragonal, 
Rhombohedral, Cubic...)
"""
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
	try:
		sys.argv[1]
	except Exception as ret:
		print("   Usage: createLattice.py POSCAR.")
		exit()
	filename = sys.argv[1]
	pos_line = read_POS(filename)
	hex = is_hex(pos_line)
	with open("lattice.in", 'w') as f:  # write to lattice.in
		f.write("lattice\\"+"\n")
		if not hex:
			print("\nThe crystal system is: Orthorhombic.\n")
			for line in pos_line:
				for num in line:
					f.write("%.15f" %num + " "),
				f.write("\\\n")
		else:
			print('The crystal system is: Hexagonal.\n')
			a = pos_line[0][0]
			c = pos_line[-1][-1]
			f.write("Hexagonal %.15f %.15f" %(a, c)),
	log()


if __name__ == "__main__":
	main()

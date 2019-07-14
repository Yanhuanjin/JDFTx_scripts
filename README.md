# JDFTx_scripts
Some scripts to create the input file for JDFTx: Using the POSCAR

## Introdution

This project is created for those who are familiar with VASP but new to use JDFTx. The only needed file is "POSCAR", and the two scripts can generate two structure input files.

## Environment

Python2.7: Python 3 is not supported temporarily.

FILE: POSCAR like following. 

The Orientation standard of POSCAR should be "Insight II standard"

The line positions must be same! (Just for this initial version).

(Lattice Lines:Line 3-5, AtomLabel:Line 6, AtomNumber:Line 7, Fractional coordinates:Line 10-end)

	1：  XYZ   H H                      
	2：  1.00000000000000     
	3：  15.4161728677862033    0.0000000000000000    0.0000000000000000
	4：  -7.7080864338931017   13.3507973326353042    0.0000000000000000
	5：  0.0000000000000000    0.0000000000000000   22.8670327734613998
	6：  H  
	7：  2
	8：  Selective dynamics
	9：  Direct
	10： 0.2673344787272941  0.4793380419980036  0.4161816185942523   T   T   T
	11： 0.3481328037468368  0.5044238614747599  0.3622895316252637   F   F   F

## Usage

`mkdir test`

`cp createLattice.py createStructure.py POSCAR test/`

`chmod +x createLattice.py createStructure.py`
 
`./createLattice.py`

`./createStructure.py`

## Output File

`lattice.in`: 

Containing the lattice information(bohr). Hexagonal or Orthorhombic. Not support other crystal systems yet. 

(It is just because I used a very stupid way to judge them... NEED YOUR HELP!)

It looks like this:

	lattice\
	hexagonal\
	29.132352917539933\
	43.212441547374333

`structure.in`

Containing the structure information(bohr).

It looks like this:

	ion H 0.805959664944308 12.093387720668192 17.984219108659595 1  # 1 for T
	ion H 2.794399985383460 12.726286665969026 15.655411066759651 0  # 0 for F 

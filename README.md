# JDFTx_scripts
Scripts to create the input file for JDFTx: Using the POSCAR/CONTCAR

## Introdution

This project is created for those who are familiar with VASP but new to JDFTx. The only needed file is "POSCAR", and this scripts package can generate JDFTx input files automatically.

## Environment && You need to know

Succeed in Python2.7

1. IF INPUT FILE IS **POSCAR**:

FILE: POSCAR like following(a H2 example). 

The **POSCAR** should be in this format:
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

1. IF INPUT FILE IS **POSCAR** or **CONTCAR**:

`mkdir test`
 
`createLattice.py POSCAR` or `createLattice.py CONTCAR`

`createStructure.py POSCAR` or `createStructure.py CONTCAR`

Then, `copy fix_potential_example/* ./`, you can submit your calculation task. `fix_potential_example` is your example dir.


###  Generated File

`lattice.in`: 

Containing the lattice information(bohr). Hexagonal or Orthorhombic. Not support other crystal systems yet. 

(It is just because I used a very simple way to judge them... NEED YOUR CONTRIBUTION!)

It looks like this:

	lattice\
	hexagonal\
	29.132352917539933\
	43.212441547374333

`structure.in`

Containing the structure information(in bohr).

It looks like this(or in fractional coordinates):

	ion H 0.805959664944308 12.093387720668192 17.984219108659595 1  # 1 for T
	ion H 2.794399985383460 12.726286665969026 15.655411066759651 0  # 0 for F 


\* Any problem, write [here](https://github.com/Yanhuanjin/JDFTx_scripts/issues) and let me know.

# JDFTx_scripts
Scripts to create the input file for JDFTx: Using the POSCAR/CONTCAR or .xsd

## Introdution

This project is created for those who are familiar with VASP but new to JDFTx. The only needed file is "POSCAR" or ".xsd" file, and this scripts package can generate JDFTx input files automatically.

## Decompression

Use `tar xvf jdftx_scripts.tar` and `tar xvf fix_potential_example.tar`, and you get two folders, including an example folder and a script folder. Add the script folder to your PATH, add `export PATH=PATH_OF_script_folder:$PATH` to .bashrc and source it.

For example, if PATH_OF_script_folder is `/home/users/yhjin/example/jdftx/usage/jdftx_scripts`, 

`export PATH=/home/users/yhjin/example/jdftx/usage/jdftx_scripts:$PATH`.

edit `/jdftx_scripts/fix_potential_jdftx.sh`, change `xsd2pos2` to your Vasp script that creates five input files, and also remember to change this line to your jdftx example dir, `cp ~/example/jdftx/fix_potential/* ./`

## Environment && You need to know

Succeed in Python2.7

1. IF INPUT FILE IS **POSCAR**:

FILE: POSCAR like following(a H2 example). 

The Orientation standard of POSCAR should be **"Insight II standard"** in Materials Studio, to judge the type of crystal system (Hex or Orth), or you can edit the code to fit more crystal systems. 

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

2. IF INPUT FILE IS **".xsd"**:

The **"Insight II standard"** mode in Materials Studio is necessary, or you will get in trouble.

Your "xsd2pos" script must generate **POSCAR** like aforementioned.



## Usage

1. IF INPUT FILE IS **POSCAR** or **CONTCAR**:

`mkdir test`
 
`createLattice.py POSCAR` or `createLattice.py CONTCAR`

`createStructure.py POSCAR` or `createStructure.py CONTCAR`

Then, `copy fix_potential/* ./`, you can submit your calculation task by `qsub neutral.script` or `qsub jdftx.sh` or `qsub fix_potential.script`

2. IF INPUT FILE IS **.xsd**:

run `fix_potential_jdftx.sh`, you will get all input files, and then you can submit your task.

### Before submit your task

Run `j_check_pos.py` to confirm if there is any errors in your `structure.in` file, and it will get you remind of set the **"Insight II standard"** mode correctly in Materials Studio.


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

It looks like this:

	ion H 0.805959664944308 12.093387720668192 17.984219108659595 1  # 1 for T
	ion H 2.794399985383460 12.726286665969026 15.655411066759651 0  # 0 for F 

`common.in`

A common input file, you can change it **DO REMEMBER TO CHAGE IT TO YOUR OWN SYSTEM!** See [JDFTx](http://jdftx.org/) official website.

`Charged.in` & `fix_potential.script`

An input file that contains the Charge information, to do a single point fix potential calculation.

`Neutral.in` & `neutral.script`

An input file to do a single point neutral calculation.

`jdftx.sh`

A scirpt to do a series of fix potential calculations.

For example, we wrote those lines to do a series of calculations in a potential range of [-1, 1] eV. (It is also metioned in the official website).

	for iMu in {-10..10..2}; do
    	export mu="$(echo $iMu | awk '{printf("%.4f", -4.4/27.2114+0.1*$1/27.2114)}')"
    	mpirun -np $NP -hostfile $PBS_NODEFILE $EXEC -c 1 -i Charged.in | tee Charged$mu.out
    	mv common.nbound Charged$mu.nbound
	done

 WARNING：***Before do any calculations, you should know what you are doing! ***

\* Any problem, write [here](https://github.com/Yanhuanjin/JDFTx_scripts/issues) and let me know.

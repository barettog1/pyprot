![pyprot Logo](https://raw.githubusercontent.com/rasbt/pyprot/master/images/logos/molecule_logo.png)

**PyProt is a Python package for working with protein structure files. It comes with a collection of ready-to-use scripts for the most common file operations and protein analyses.**



[[download pyprot.zip](https://github.com/rasbt/pyprot/archive/master.zip)] [[link to pyprot on GitHub](http://htmlpreview.github.io/?https://github.com/rasbt/pyprot/blob/master/README.html)]

<hr>
## ReadMe Contents
- [Scripts and command line tools](#scripts-and-command-line-tools)
- [Tutorials](#tutorials)
- [API documentation](#api-documentation)
- [Installation](#installation)

<hr>



<br>
<br>




## Scripts and command line tools

PyProt provides ready-to-use command line scripts that are using the underlying `pyprot` objects to work with PDB and MOL2 files.  
The scripts are located in the subdirectory `./scripts` and can be used after `pyprot` was successfully installed.   


### List of command line tools

- Working with PDB files
    - Center of Mass
    - Grab atoms within a radius
    - Root-mean-square deviation (RMSD)
    - PDB to FASTA conversion
    - PDB atom and residue renumbering
    - B-factor statistics
    - PDB downloader
  
- Working with MOL2 files
    - Transfer charges
    - Split multimol2 files
	- MOL2 functional group filter
	- MOL2 intermolecular functional group screening


<br>
<br>


## API documentation

Please find the API documentation at [http://rasbt.github.io/pyprot/](http://rasbt.github.io/pyprot/).


<br>
<br>



## Tutorials

In progress ...

<br>
<br>

## Installation

PyProt was build and tested in Python 3.

The `pyprot` package can be installed like any other "normal" Python package via 
	
	pip install pyprot
	
or 

	python setup.py install
	
after downloading it from this repository. Once the pyprot package is installed, the scripts and tools from the `./scripts` subdirectory are ready to use.   
For more details, please see the separate **["Installation Documentation"](./docs/pyprot_installation.md)**
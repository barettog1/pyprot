<a class="mk-toclify" id="pyprot-installation"></a>
# PyProt Installation


- [Installing the `pyprot` package](#installing-the-pyprot-package)
- [Using the command line scripts](#using-the-command-line-scripts)
- [[Optional] Adding the scripts to your PATH](#optional-adding-the-scripts-to-your-path)






<br>
<br>
**Note that PyProt was only tested to work with Python 3.x.**

<br>
<br>

<a class="mk-toclify" id="installing-the-pyprot-package"></a>

#### Installing the `pyprot` package

[[back to top](#pyprot-installation)]
1. Download pyprot from this GitHub repository at [https://github.com/rasbt/pyprot/archive/master.zip](https://github.com/rasbt/pyprot/archive/master.zip)
2. After unzipping the archive, `cd` into the `pyprot` directory
3. Install `pyprot` it via `python setup.py install`

<br>
<br>

<a class="mk-toclify" id="using-the-command-line-scripts"></a>

#### Using the command line scripts

[[back to top](#pyprot-installation)]
Python scripts based on the `pyprot` classes for common protein file operations is provided in the subdirectory `./scripts` and can be directly be executed via Python from this directory once `pyprot` is installed. For more information about the the scripts, please see the following section [Scripts and Command Line Tools](#scripts_and_tools).

<br>
<br>

<a class="mk-toclify" id="optional-adding-the-scripts-to-your-path"></a>

#### [Optional] Adding the scripts to your PATH
[[back to top](#pyprot-installation)]

Since the usage of those provided scripts is optional, they will not be automatically installed if you install `pyprot`. I recommend you to copy them to a different directory on your drive, e.g., `~/home/username/pyprot_scripts/` and add the script directory to your `PATH`.


<br>
**Step 1: Appending the script directory to PATH**   

E.g., if you are using a bash shell, you can add the line

	export PATH=:$PATH:/home/username/pyprot_scripts/

to your `~/.bash_profile` or `~/.bashrc` file

You can do this directly from the command line via

	echo "export PATH=:$PATH:/home/username/pyprot_scripts/" >> .bash_profile

<br>
**Step 2: Making the scripts executable from the command line**  

In order to call the scripts without issuing the Python command, e.g, 
	
	rmsd.py   

instead of 

	python3 ./path/to/rmsd.py
	
you have to add a python-shebang (e.g., `#!/usr/bin/python`) on top of the scripts. To do this automatically for all python script files in the current directory, you can use the shell script `prepend_python_shebang.sh`.

	sh prepend_python_shebang.sh

<br>
<br>


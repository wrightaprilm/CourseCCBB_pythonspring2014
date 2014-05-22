#Other things

## Permissions

```UNIX

chmod +x filename

```

This makes files executeable. Reading on [permissions](http://linuxcommand.org/lts0070.php).


##Python Path

Many computer scientists advise creating a single directory for all your scripts, and putting that in what is called your PythonPath.

I keep most of my scripts in a directory called scripts. In my .bashrc file, I include a line that says:

```UNIX
export PATH="/home/april/scripts:$PATH"
```

This allows me to execute my scripts from the scripts folder from anywhere on my computer. 

##Interesting Modules for Biologists

###Sci-Kit Bio

Methods for parsing and formatting sequence data, playing with trees and automating testing.

http://scikit-bio.org/

###Sci-Kit Learn

Tools for data mining and analysis. PCA, regression, model selection and other mathematical operations.

http://scikit-learn.org/stable/index.html

### Dendropy

Tools for manipulating phylogenetic trees and associated data matrices. Also has nice integration with various phylogenetic software.

http://pythonhosted.org/DendroPy/

### Biopython

Biopython has tools mostly aimed at molecular biologists. DNA sequence parsing, format conversion

http://biopython.org/wiki/Main_Page


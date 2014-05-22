## SJS 5/22/14. Feel free to email stephanie.spielman@gmail.com with questions!
# Script to introduce the biopython module and regular expression usage.

# import the sequence input-ouput functionality from the Biopython module
from Bio import SeqIO

# import the regular expression python module
import re


# This file contains several histamine receptor (HRH) sequences in fasta format
file_name = 'HRH.fasta' 

# This line uses biopython to read in a sequence file in fasta format.
# The command will read in a file containing multiple sequences.
# The variable "records" we create here will contain a list of "Sequence Records," which biopython creates for us automatically
records = list(SeqIO.parse(file_name, 'fasta'))

## NOTE:
# Other ways to use SeqIO:
# 1. Read in a file of sequences in phylip format:      list(SeqIO.parse(file_name, 'phylip'))
# 2. Read in a fasta file containing a SINGLE sequence: SeqIO.read(file_name, 'fasta') . Because there is only a single sequence, there is no need to turn it into a list.

# We can obtain information from each sequence record stored in the "records" list we have created, using a for loop.
# The usual information you'll need are the sequence id, and the sequences themselves. They can be accessed by typing the name of the record (in this case, the loop variable "my_record"), and then .id or .seq .
print "\nHere are the records from HRH.fasta:"
for my_record in records:
    print my_record.id    #print the  id
    print my_record.seq   #print the sequence 
    print                 #print a new line (for easier viewing!)


# Now we can use regular expressions to extract ONLY the NCBI part of each sequence id from our records, using the re module.
# Recall - 
# \w = letter or digit
# \d = number
# .  =  wildcard! Represents (most) anything ever.
# If I actually want a period, I must "escape" the wildcard behavior by adding a backslash: \. is a real period.
# add + after your regular expression character to match one or more of them
# add + after your regular expression character to match 0 or more of them

# First, let's construct a regular expression for the entire id, and prove to ourselves that it works by printing.
# First, to prove the regular expression works
print "\nProving that my regular expression works"
for record in records:
    find_id = re.search('\wP_\d+\.\d_HRH\d', record.id)
    if find_id:
        print find_id.group()

# Now!! We can capture the actual part of the id we are interested in, using parentheses inside the regular expression.
print "\nCapturing the interesting part of the id for future use"
for record in records:
    find_id = re.search('(\wP_\d+\.\d)_HRH\d', record.id)
    if find_id:
        ncbi_id = find_id.group(1)
        print ncbi_id


## NOTE: Often times, it is useful to have your regular expressions be as general as possible. Here's a more general version of the regular expression used above -
# For instance, NCBI ids might look like XP_389571 instead of XP_389571.1, so we might want flexibility allowing the ".1" at the end of the NCBI id to be optional. We can accomplish this using asterisks.
# HERE:   \w+_\d+\.*\d*_.+     

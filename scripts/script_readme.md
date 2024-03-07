# Scripts for data processing

After downloading the data, follow these steps to refine it using the provided scripts:

**Step 1: Review Fasta header Format** 
 - Before running any scripts, familiarize yourself with the format of the downloaded data to ensure compatibility with the scripts.

**Step 2: Select Relevant Scripts**

 - Identify the scripts that correspond to the format of your downloaded data. It is not necessary to run all scripts.

#### Script 1: `add_lettercode.py`
- **Description:** This script adds the provided letter code to all protein IDs as prefix in the given FASTA file.
- **Usage Instructions:** Run `python add_lettercode.py` to print the usage instructions of the script. The script provides several options:
  - `-c`: Specify the letter code/extended letter code.
  - `-i`: Input FASTA file.
  - `-o`: Output directory.
  - `-ncbi`: Filter out proteins based on certain header descriptions and separate major and other isoforms as well as ﬁlters out proteins whose descriptions contain “(mitochondrion)”, “(plasmid)”, “(plastid)”
or “(chloroplast)” and writes the proteins in a lettercodemt.fa resp. lettercodepl.fa resp.
lettercodept.fa ﬁle. .
  - `-human`: Handle special cases for human and mouse protein files.

- **Example Usage:**
```
  $ python add_lettercode.py -c [letter_code] -i input.fasta -o output_directory
```

#### Script 2: `split_isoform.py`
- **Description:** This script splits a file containing only major isoforms and a file containing all proteins into two separate files, one for major isoforms and one for other isoforms. (this happens when the data is downloaded from Phytozome)
- **Usage Instructions:** Run `python split_isoform.py` to print the usage instructions of the script. The script requires the following inputs:
  - `-o`: Output directory.
  - `-wo`: File containing only major isoforms.
  - `-iso`: File containing all proteins.
- **Example Usage:**
```
  $ python split_isoform.py -o output_directory -wo NANGAwo.fa -iso NANGA.fa
```

#### Script 3: `split_isoform_dot.py`
- **Description:** This script groups proteins with the same ID part together, uses the longest one as the major isoform, and writes the others into an isoform file. The script also adds the letter code at the beginning of the FASTA ID.
- **Usage Instructions:** Run `python split_isoform_dot.py` to print the usage instructions of the script. The script requires the following inputs:
  - `-o`: Output directory.
  - `-i`: Input FASTA file.
  - `-c`: Letter code.
  - `-p`: Pattern used for splitting.
- **Example Usage:**
```
  $ python split_isoform_dot.py -o output_directory -i input.fasta -c CAMSA -p .
```

#### Script 4: `split_hc_lc.py`
- **Description:** This script is designed for handling protein files containing low and high confidence proteins. Proteins with identifiers or descriptions containing "_hc_" or "_lc_" are separated into low confidence and high confidence files respectively.
- **Usage Instructions:** Running `python split_hc_lc.py` will print the usage instructions of the script. The script requires the following inputs:
  - `-o`: Output directory.
  - `-i`: Input FASTA file.
- **Example Usage:**
```
  $ python split_hc_lc.py -o output_directory -i input.fasta
```

#### Script 5: `split_hc_lc.py`

**Step 3: Running Scripts**

 - Execute the selected scripts according to your downloaded data format. Refer to script documentation for any specific instructions/parameters. 


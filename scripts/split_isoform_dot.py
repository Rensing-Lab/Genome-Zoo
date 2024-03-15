import sys
import argparse
import os 

"""
Usage: python split_isoform_dot.py

This script can be used if you have a ﬁle containing isoforms. The ﬁrst part of the ID of the isoforms
has to be the same up to a certain pattern which has to be given as a parameter! The script then
groups all proteins with the same ID part together and uses the longest one as major isoform. 

The letter code has to be given using the -c option, the output directory using the -o option, the input
fasta ﬁle using the -i option and the pattern used for splitting using the -p option.

Options:
  -c, --code        The letter code to be added at the beginning of the fasta ID.
  -o, --output      The output directory.
  -i, --input       The input fasta file.
  -p, --pattern     The pattern used for splitting.
"""


def main():
    parser = argparse.ArgumentParser(prog='split_isoform_dot_t', usage='python split_isoform_dot_t.py -o outDir '
                                                                       '-i Fasta -c lettercode -p pattern',
                                     description='Split file containing major and other isoforms into two files'
                                                 ' according to the fasta headers containing the given pattern before '
                                                 'the isoform number. The programm will split the fasta header at the '
                                                 'given pattern and take the first filed in the split as grouping '
                                                 'string (key in a dictionary) to group isoforms. The script will also '
                                                 'add the letter code to the beginning of the fasta IDs.')
    parser.add_argument('-i', '-infile', help='fasta input file')
    parser.add_argument('-o', '-outdir', help='fasta output directory')
    parser.add_argument('-c', '-code', help='specify 5 letter code')
    parser.add_argument('-p', help='specify pattern for splitting fasta IDs')
    args = parser.parse_args()

    if args.i is None or args.o is None or args.c is None or args.p is None:
        parser.print_help()
        print("Please indicate all needed parameters!")
    else:
        if os.path.isfile(args.i):
            if os.path.isdir(args.o):
                if args.o.endswith("/"):
                    wm = open("%s%s.fa" % (args.o, args.c), 'w')
                    wi = open("%s%siso.fa" % (args.o, args.c), 'w')
                else:
                    wm = open("%s/%s.fa" % (args.o, args.c), 'w')
                    wi = open("%s/%siso.fa" % (args.o, args.c), 'w')
                prot_map = {}
                header = ""
                header_line = ""
                protein = []
                r = open(args.i, 'r')

                for line in r:
                    if line.startswith('>'):
                        if header != "":
                            protein_string = "".join(protein)
                            if header in prot_map:
                                prot_map[header][len(protein_string)] = {"header": header_line[1:],
                                                                         "protein": protein_string}
                            else:
                                prot_map[header] = {len(protein_string): {"header": header_line[1:],
                                                                          "protein": protein_string}}

                        protein = []

                        temp = line.strip().split(args.p)
                        header = temp[0]
                        header_line = line

                    else:
                        protein.append(line)

                r.close()

                if header != "":
                    protein_string = "".join(protein)
                    if header in prot_map:
                        prot_map[header][len(protein_string)] = {"header": header_line[1:],
                                                                 "protein": protein_string}
                    else:
                        prot_map[header] = {len(protein_string): {"header": header_line[1:],
                                                                  "protein": protein_string}}

                for key in prot_map:
                    if len(prot_map[key]) > 1:
                        max_len = -1
                        max_key = ""
                        for header in list(prot_map[key].keys()):
                            if len(prot_map[key][header]["protein"]) > max_len:
                                max_len = len(prot_map[key][header]["protein"])
                                max_key = header

                        for num in list(prot_map[key].keys()):
                            if num == max_key:
                                wm.write(">%s_%s%s" % (args.c, prot_map[key][num]["header"],
                                                       prot_map[key][num]["protein"]))
                            else:
                                wi.write(">%s_iso_%s%s" % (args.c, prot_map[key][num]["header"],
                                                          prot_map[key][num]["protein"]))
                    else:
                        wm.write(">%s_%s%s" % (args.c, prot_map[key][list(prot_map[key].keys())[0]]["header"],
                                               prot_map[key][list(prot_map[key].keys())[0]]["protein"]))

                wi.close()
                wm.close()
            else:
                print("Given output directory does not exist: %s" % args.o)
        else:
            print("Given input file does not exist: %s" % args.i)

if __name__ == '__main__':
    main()

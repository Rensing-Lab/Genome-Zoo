import argparse
import os


def main():
    parser = argparse.ArgumentParser(prog='split_hc_lc', usage='python split_hc_lc.py -o outDir -i Fasta',
                                     description='Split file containing high and low confidence proteins into two '
                                                 'files.')
    parser.add_argument('-i', '-infile', help='fasta input file')
    parser.add_argument('-o', '-outdir', help='fasta output directory')
    args = parser.parse_args()
    if args.i is None or args.o is None:
        parser.print_help()
        print("Please indicate all needed parameters!")
    else:
        if os.path.isfile(args.i):
            if os.path.isdir(args.o):
                file_name = args.i.split('/')[-1].rsplit('.', 1)[0]
                if args.o.endswith("/"):
                    wl = open("%s%s_lc.fa" % (args.o, file_name), 'w')
                    wh = open("%s%s_hc.fa" % (args.o, file_name), 'w')
                else:
                    wl = open("%s/%s_lc.fa" % (args.o, file_name), 'w')
                    wh = open("%s/%s_hc.fa" % (args.o, file_name), 'w')

                r = open(args.i, 'r')
                hc = True
                for line in r:
                    if line.startswith('>'):
                        if "_hc_" in line: ## Make sure header contain 'hc' in header line, or change it accordingly.  
                            hc = True
                        else:
                            hc = False

                    if hc:
                        wh.write(line)
                    else:
                        wl.write(line)

                r.close()
                wl.close()
                wh.close()
            else:
                print("Given output directory does not exist: %s" % args.o)
        else:
            print("Given input file does not exist: %s" % args.i)


if __name__ == '__main__':
    main()

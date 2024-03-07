import argparse
import os


def main():
    parser = argparse.ArgumentParser(prog='shorten_fasta_header', usage='python shorten_fasta_header.py -i Fasta',
                                     description='Shorten fasta header lines only to ID (sometimes needed due to '
                                                 'forbidden characters in the header)')
    parser.add_argument('-i', '-infile', help='fasta input file')
    args = parser.parse_args()

    if args.i is None:
        parser.print_help()
        print("\nPlease indicate fasta file!")
    else:
        if os.path.isfile(args.i):
            outfile = "%s_chopped.fa" % args.i.rsplit('.', 1)[0]

            r = open(args.i, 'r')
            w = open(outfile, 'w')

            for line in r:
                if line.startswith('>'):
                    w.write("%s\n" % line.split()[0])

                else:
                    w.write(line)

            r.close()
            w.close()
        else:
            print("Given input file does not exist: %s" % args.i)

if __name__ == '__main__':
    main()

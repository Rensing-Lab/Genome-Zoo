import argparse
import os


def get_num(line):
    temp = line.split('isoform ')[1].strip().strip('X')
    try:
        if not temp or temp[0] not in "0123456789":
            return 1
        else:
            i = -1
            in_number = True
            while in_number and i < (len(temp) - 1):
                i += 1
                if temp[i] not in "0123456789":
                    in_number = False
            if i == 0:
                return int(temp)
            else:
                return int(temp[:i])

    except ValueError:
        print(line.strip())
        print("If this error occurred, adapt the code to make it work!")
        assert False


def main():
    parser = argparse.ArgumentParser(prog='add_lettercode', usage='python add_lettercode.py -i inputFasta -o '
                                                                  'outputDir -c lettercode [-ncbi -human]',
                                     description='Add 5 letter code to existing FASTA headers. '
                                                 'The output file will be lettercode.fa')
    parser.add_argument('-i', '-infile', help='fasta input file')
    parser.add_argument('-o', '-outdir', help='fasta output directory')
    parser.add_argument('-c', '-code', help='specify 5 letter code')
    parser.add_argument('-ncbi', help="Indicate if file was downloaded from NCBI", action='store_true')
    parser.add_argument('-human', help="Indicate if file has to be handled with special rules for human protein file",
                        action='store_true')
    args = parser.parse_args()

    if args.i is None or args.o is None or args.c is None:
        parser.print_help()
        print("\nPlease indicate all needed parameters!")

    else:
        if os.path.isfile(args.i):
            if os.path.isdir(args.o):
                if args.o.endswith("/"):
                    w = open("%s%s.fa" % (args.o, args.c), 'w')
                else:
                    w = open("%s/%s.fa" % (args.o, args.c), 'w')

                r = open(args.i, 'r')
                in_other = False
                in_iso = False
                in_plasmid = False
                to_save = False
                in_plastid = False
                wm = None
                wi = None
                wp = None
                wc = None
                iso_map = {}
                protein = []
                save_key = ""
                header = ""

                for line in r:
                    if line:
                        if line.startswith('>'):
                            if args.human and protein and save_key and header:
                                prot = "".join(protein)
                                if save_key not in iso_map:
                                    # The length of the protein also contains newlines, but it is okay because all
                                    # protein line parts have the same length
                                    iso_map[save_key] = {"len": len(prot), "protein": prot, "header": header}
                                elif len(prot) > iso_map[save_key]["len"]:
                                    wi.write(">%siso_%s%s" % (args.c, iso_map[save_key]["header"],
                                                              iso_map[save_key]["protein"]))
                                    iso_map[save_key] = {"len": len(prot), "protein": prot, "header": header}

                            in_other = False
                            in_iso = False
                            to_save = False
                            in_plasmid = False
                            in_plastid = False
                            protein = []
                            header = ""
                            save_key = ""

                            if (args.ncbi or args.human) and "(mitochondrion)" in line:
                                if not wm:
                                    if args.o.endswith("/"):
                                        wm = open("%s%smt.fa" % (args.o, args.c), 'w')
                                    else:
                                        wm = open("%s/%smt.fa" % (args.o, args.c), 'w')
                                in_other = True
                                wm.write(">%smt_%s" % (args.c, line[1:]))

                            elif args.ncbi and "(plasmid)" in line:
                                if not wp:
                                    if args.o.endswith("/"):
                                        wp = open("%s%spl.fa" % (args.o, args.c), 'w')
                                    else:
                                        wp = open("%s/%spl.fa" % (args.o, args.c), 'w')
                                in_plasmid = True
                                wp.write(">%spl_%s" % (args.c, line[1:]))

                            elif args.ncbi and ("(chloroplast)" in line or "(plastid)" in line):
                                if not wc:
                                    if args.o.endswith("/"):
                                        wc = open("%s%spt.fa" % (args.o, args.c), 'w')
                                    else:
                                        wc = open("%s/%spt.fa" % (args.o, args.c), 'w')
                                in_plastid = True
                                wc.write(">%spl_%s" % (args.c, line[1:]))

                            elif (args.ncbi or args.human) and 'isoform ' in line:
                                if not args.human:
                                    num = get_num(line)
                                    if num > 1:
                                        if not wi:
                                            if args.o.endswith("/"):
                                                wi = open("%s%siso.fa" % (args.o, args.c), 'w')
                                            else:
                                                wi = open("%s/%siso.fa" % (args.o, args.c), 'w')
                                        in_iso = True
                                        wi.write(">%siso_%s" % (args.c, line[1:]))
                                    else:
                                        w.write(">%s_%s" % (args.c, line[1:]))
                                else:
                                    if not wi:
                                        if args.o.endswith("/"):
                                            wi = open("%s%siso.fa" % (args.o, args.c), 'w')
                                        else:
                                            wi = open("%s/%siso.fa" % (args.o, args.c), 'w')
                                    to_save = True
                                    save_key = line.strip().split(" ", 1)[1].split(" isoform")[0]
                                    header = line[1:]

                            else:
                                w.write(">%s_%s" % (args.c, line[1:]))

                        elif in_other:
                            wm.write(line)
                        elif in_plasmid:
                            wp.write(line)
                        elif in_plastid:
                            wc.write(line)
                        elif in_iso:
                            wi.write(line)
                        elif to_save:
                            protein.append(line)
                        else:
                            w.write(line)

                r.close()

                if args.human and protein and save_key and header:
                    prot = "".join(protein)
                    if save_key not in iso_map:
                        # The length of the protein also contains newlines, but it is okay because all
                        # protein line parts have the same length
                        iso_map[save_key] = {"len": len(prot), "protein": prot, "header": header}
                    elif len(prot) > iso_map[save_key]["len"]:
                        iso_map[save_key] = {"len": len(prot), "protein": prot, "header": header}

                for key in iso_map:
                    w.write(">%s_%s%s" % (args.c, iso_map[key]["header"], iso_map[key]["protein"]))

                w.close()

                if wm:
                    wm.close()

            else:
                print("Given output directory does not exist: %s" % args.o)
        else:
            print("Given input file does not exist: %s" % args.i)

if __name__ == '__main__':
    main()

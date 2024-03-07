# Genome Zoo / MAdLandDB 

<!-- HTML -->
<a href="https://madland.science">
    <img src="https://madland.science/img/MAdLand.jpg" alt="Image Description" align="right" width="100" height="100">
</a>

Genome Zoo also known as MAdLandDB is a protein sequence Database for fully sequenced plant and algal genomes, with a particular emphasis on non-seed plants and streptophyte algae. This database contains over 21 million sequences, representing a diverse group of more than 600 species.

## Download Species Data Information

To access the species data information, please visit the [downloads page](https://madland.science/madlandwiki/downloads). This link is currently accessible only to MAdLand members.

## Adding New Data to Genome Zoo

When adding new species to Genome Zoo, begin by adding the metadata information to the Genome Zoo Table. Before making any changes to the Genome Zoo table, follow these steps:

1. **Ensure the Species is Not Already in Genome Zoo:**
   - Check NCBI Taxonomy to verify if the species is already listed, possibly under a synonym.
   - Even if the species is already present, consider adding new transcriptome data or data for a different strain if they differ significantly.

2. **Create a Letter Code for the Species:**
   - Use the first three letters of the genus name and the first two from the species name (e.g., <i>ORYSA = ORYza SAtiva.</i>).

3. **Check that the letter code is not taken yet**
   - Ensure that the letter code is not already taken in the table.
   - If the code is not taken yet, everything is ﬁne. If the code is already taken remove the last letter from the code and use a number (also check here that the number is not taken yet for that four-letter code and that they are consecutive; start with 1).

4. **Check if you need an extension for your letter code**
    - If the source of the proteins is not genome, but transcriptome, the letter code has to be extended with tr. 
    - If you add new a transcriptome data set for a species that is already in Genomezoo use the first two characters of the first author name of the corresponding paper (or something else indicating the source, note it down in the table) to extend the code (e.g., NITMItrJU)
    - If you have to add a new strain, use two upper-case letters to extend the letter code e.g. ORYSAJA for <i>Oryza sativa (spp. japonica)</i> (this is not needed if the species is in the table only once).
   - If you want to add a new version of a protein set for the species that is already in the Genome Zoo. Add a 'v' or 'V' followed by the version number for updated protein sets.

5. **Download Protein Files for the Species:**
   - Obtain protein files from provided links or papers. If not available, contact corresponding authors for data access.
   - Explore NCBI genome and Phytozome for available data. 

6. **Check and Download Organelle Proteins:**
   - Download mitochondrial, chloroplast, or plastid proteins if available.

7. **Naming Convention for Files:**
   - Prefix the file name(s) with the letter code, following specific conventions based on the protein source.
        There are diﬀerent cases for the diﬀerent protein sources:
        - Genome: use the letter code
        - Transcriptome: Use the letter code containing the tr
        - Mitochondrion: add mt to the end of the letter code
        - Plasmid: add pl to the end of the letter code
        - Chloroplast or other plastids: add pt to the end of the letter code
        - High conﬁdence proteins: add hc to the end of the letter code (only if there are also low
        conﬁdence proteins)
        - Low conﬁdence proteins: lc to the end of the letter code
        - Unknown organelle proteins: add org to the end of the letter code
    



This README serves as a guide for to Genome Zoo / MAdLandDB addition. For any inquiries or assistance, please contact the [Rensing Lab](https://plantco.de/)


## Misc

Command for splitting up a full Genome zoo `.faa` file into per-species fasta files:

```
awk -v OFS="\n" '/^>/ {getline seq; print $0,seq > substr($1,2,index($1,"_")-2)".fa"}' MAdLand.14.02.2024.db.faa
```

(Note that this assumes fasta headers start with the 5lettercode followed by underscore, e.g. `>AMBTR_`, and the sequence is always on a single line``


#get pdb id and chain ids of protein and peptide
awk -F'\t' '{print $3, $4, $5}' 41467_2021_27838_MOESM4_ESM.txt | sort | uniq -c > pdb.list

#get fasta file of each pdb
awk '{print $1}' pdb.list | tr "[:lower:]" "[:upper:]" | awk '{print "wget https://www.rcsb.org/fasta/entry/"$1}' | bash


QUERY: ( Total Number of Polymer Instances (Chains) > 1 AND Entry Polymer Types = "Protein (only)" AND ( Count Per Polymer Entity > 0 AND Type (Polymer Entity Feature Summary) = "modified_monomer" ) ) AND Full Text = "covalent"

awk '$NF=="prot" && $3<=15{print $1}' peptidelist.txt | sort | uniq > pep15.txt
cat pep15.txt pdb_with_cov.txt | sort | uniq -c | awk '$1>1{print $2}' > cov_pep.txt

4MLI
4I7C
7O07

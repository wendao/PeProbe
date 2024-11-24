for p in $(cat list)
do
cd $p
mv target.pdb raw.pdb
python ~/work/peprobe/pdb_fst_match/scripts/idealize_pdb.py raw.pdb > target.pdb
mv pep.pdb raw.pdb
python ~/work/peprobe/pdb_fst_match/scripts/idealize_pdb.py raw.pdb > pep.pdb
mv recptor.pdb raw.pdb
python ~/work/peprobe/pdb_fst_match/scripts/idealize_pdb.py raw.pdb > recptor.pdb

~/bakerlab/./rosetta_src_2020.08.61146_bundle/main/source/scripts/python/public/pdb2fasta.py pep.pdb > pep.fasta
cd ..
done

for d in $(cat pep16.txt)
do
  cd /data/database/pepbdb/pepbdb/$d
  echo "DIST $d" $(~/share/bin/cal_min_dist.x receptor.pdb peptide.pdb)
  cd -
done

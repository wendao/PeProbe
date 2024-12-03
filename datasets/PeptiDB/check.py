import sys
lines = open("db.list",'r').readlines()
#print "set fetch_path, mmcif"
for l in lines:
    es = l.strip().split('\t')
    if len(es[3].split(':')) == 2 and len(es[1])==1:
        #print(es[0].lower() + "_" + es[1])
        print(es[0].lower() + "_" + es[2])

        #ref protein
        #print "fetch "+es[0]+", async=0"
        #print "save "+es[0]+"/target.pdb, chain "+es[1]
        #print "delete all"

        #peptide
        #print "fetch "+es[0]+", async=0"
        #print "save "+es[0]+"/pep.pdb, chain "+es[2]
        #print "delete all"

        #prot, ch = es[3].split(':')
        ##free protein
        #print "fetch "+prot+", async=0"
        #print "save "+es[0]+"/recptor.pdb, chain "+ch
        #print "delete all"

        #pep length
        #with open(es[0]+"/pep.fasta", 'r') as fp:
        #    tmp = fp.readlines()
        #    seq = tmp[1].strip()
        #    if int(es[4]) != len(seq):
        #      print es[0], es[4], len(seq), seq


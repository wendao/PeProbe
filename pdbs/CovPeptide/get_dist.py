import sys

lines = open("dist.txt", 'r').readlines()
map_pep = {}
map_dis = {}
for l in lines:
    es = l.strip().split()
    prot_pep = es[1]
    prot = prot_pep[:4]
    pep = prot_pep[-1]
    dist = float(es[2])
    if prot not in map_dis.keys():
        map_pep[prot] = pep
        map_dis[prot] = dist
    elif map_dis[prot]>dist:
        map_pep[prot] = pep
        map_dis[prot] = dist

lines = open("cov_pep.txt", 'r').readlines()
for l in lines:
    es = l.strip().split()
    print es[0], map_pep[es[0]], map_dis[es[0]]

#!/usr/bin/env python3

from .constants import Constants as Cnsts

class IndexMaper:
    def __init__(self):
        pass


    def getIndexMap(self):
        words = []
        with open(Cnsts.RESDIR+Cnsts.RAWINDEX_MAP_FILE,'r') as ridxfil:
            for line in ridxfil:
                words.append(line)
        

        idxmap = {}
        with open(Cnsts.RESDIR+Cnsts.INDEX_MAP_FILE,'w') as idxfil:
            totlen = len(words)
            idxlen = int(totlen/2)
            for idx in range(idxlen):
                short = words[idx][:-1]
                wlong = words[idx+idxlen][:-1]
                idxmap[short] = wlong
                idxfil.write("'"+short+"':'"+wlong+"',\n")

        return idxmap




if __name__ == '__main__':
    IndexMaper().mapIndex()

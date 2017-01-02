#!/usr/bin/python
"""
exclude_nodes.py

@author Chen Wang
@date 12/2014
Exclude nodes in file list-A from nodes in file list-B and dump the left nodes in B to file listB_A = listB - listA
"""
import sys

def get_nodes(nodes_file):
    nodes = []
    with open(nodes_file) as fd:
        lines = fd.readlines()
        for ln in lines:
            node_name = ln.rstrip('\n')
            nodes.append(node_name)
    return nodes

def write_nodes(nodes_file_name, nodes):
    cfp = open(nodes_file_name, 'w')
    for node in nodes:
        cfp.write("%s\n" % (node))
    cfp.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python exclude_nodes.py listA listB listB_A"
        sys.exit(-1)

    listA = get_nodes(sys.argv[1])
    listB = get_nodes(sys.argv[2])

    for node in listA:
        print node
        if node in listB:
            listB.remove(node)

    write_nodes(sys.argv[3], listB)



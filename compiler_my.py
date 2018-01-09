import sys
import parser_my as myp
from parser_my import Assign, Int, Var, Bin_Op, While, Print

def read_file(filename):
	with open(filename) as f:
	    return f.read()

def compile(node):
    if isinstance(node, Print):
        compile(node.exp)
        print("PRINT")
    elif isinstance(node, Int):
        print("INT", node.val)
#    if isinstance(node, Var):
#        print(

def run():
    filedata = read_file(sys.argv[1])
    tree = myp.parse(filedata)
    for n in tree:
        compile(n)

run()

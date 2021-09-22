import argparse
import operator

parser = argparse.ArgumentParser(description='Task #2')
parser.add_argument('x', type=str)
parser.add_argument('y', type=int)
parser.add_argument('z', type=int)
args = parser.parse_args()
    
try:
    print(eval("operator." + args.x)(args.y, args.z))
except:
    print("Error.")

import argparse
import operator

parser = argparse.ArgumentParser(description='Task #2')
parser.add_argument("x", type=str, nargs='*')
args = parser.parse_args()
    
y = eval("operator." + args.x[0])(int(args.x[1]), int(args.x[2]))
# add 1 2 => (func_name)(numb_1, numb_2)
print(y)
import argparse

parser = argparse.ArgumentParser(description='Task #1')
parser.add_argument('a1', type=str)
parser.add_argument('a2', type=str, choices=['+', '-', '*', '/'])
parser.add_argument('a3', type=str)
args = parser.parse_args()

print(eval(args.a1 + args.a2 + args.a3))
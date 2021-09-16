import argparse

parser = argparse.ArgumentParser(description='Task #4')
parser.add_argument("capacity", type=int)
parser.add_argument("weights", type=int, nargs = '*')
args = parser.parse_args()

par1 = [int(bar) for bar in args.weights]
par2 = [[0 for j in range(args.capacity + 1)] for i in range(len(par1) + 1)]

for i in range(len(par1) + 1):
    for j in range(args.capacity + 1):
        if i == 0 or j == 0:
            par2[i][j] = 0
        elif par1[i-1] <= j:
            par2[i][j] = max(par1[i-1] + par2[i-1][j - par1[i-1]], 
            par2[i-1][j])
        else:
            par2[i][j] = par2[i-1][j]
            
print("The largest possible weight:", par2[len(par1)][args.capacity], "bars.")

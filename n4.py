import argparse

parser = argparse.ArgumentParser()
parser.add_argument("capacity", type=int)
parser.add_argument("weight", type=int, nargs = '*')
args = parser.parse_args()
gold = [int(baggage) for baggage in args.weight]

length = len(gold)
two_dim_arr = [[0 for b in range(args.capacity + 1)] for a in range(length + 1)]
for a in range(length + 1):
      for b in range(args.capacity + 1):
            if a == 0 or b == 0:
                  two_dim_arr[a][b] = 0
            elif gold[a - 1] <= b:
                  two_dim_arr[a][b] = max(gold[a - 1] + two_dim_arr[a - 1][b - gold[a - 1]], 
                  two_dim_arr[a - 1][b])
            else:
                  two_dim_arr[a][b] = two_dim_arr[a - 1][b]
print("The largest number:", two_dim_arr[len(gold)][args.capacity], "bars.")
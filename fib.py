import sys

filename = sys.argv[1]

with open(filename) as f:
    line = f.readline()
    nums = line.split()
    n = int(nums[0])
    k = int(nums[1])

    young_pairs = 1
    reproducing_pairs = 0

    for _ in range(n - 1):
        new_young = k * reproducing_pairs
        reproducing_pairs += young_pairs
        young_pairs = new_young

    print(young_pairs + reproducing_pairs)

import sys

filename = sys.argv[1]

with open(filename) as f:
    string = f.readline()

    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for char in string:
        if char == 'A':
            a_count += 1
        elif char == 'C':
            c_count += 1
        elif char == 'G':
            g_count += 1
        elif char == 'T':
            t_count += 1

    print(a_count, c_count, g_count, t_count)

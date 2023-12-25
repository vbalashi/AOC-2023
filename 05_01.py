from functools import reduce

with open("05_task01.txt") as f:
    seeds, *maps = f.read().strip().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))
    

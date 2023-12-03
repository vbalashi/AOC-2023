from operator import truediv
from pickle import TRUE
import re
import sys

red_max = 12
green_max = 13
blue_max = 14

def green_has_outlier(line: str) -> int:
    green_values = re.findall(r'(\d+) green', line)
    int_list = list(map(int, green_values))
    return max(int_list) 

def blue_has_outlier(line: str) -> int:
    blue_values = re.findall(r'(\d+) blue', line)
    int_list = list(map(int, blue_values))
    return max(int_list) 

def red_has_outlier(line: str) -> int:
    red_values = re.findall(r'(\d+) red', line)
    int_list = list(map(int, red_values))
    return max(int_list) 

def power_of_cubes(line: str) -> int:
    return green_has_outlier(line) * blue_has_outlier(line) * red_has_outlier(line)

def main():
    sum = 0
    id = 0
    for line in sys.stdin:
        sum += power_of_cubes(line)
    print(sum)
    
if __name__ == "__main__":
    main()

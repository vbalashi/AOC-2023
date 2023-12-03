from operator import truediv
from pickle import TRUE
import re
import sys

red_max = 12
green_max = 13
blue_max = 14

def green_has_outlier(line: str) -> bool:
    green_values = re.findall(r'(\d+) green', line)
    int_list = list(map(int, green_values))
    is_outlier = False
    if max(int_list)>green_max:
        is_outlier = True 
    return is_outlier 

def blue_has_outlier(line: str) -> bool:
    blue_values = re.findall(r'(\d+) blue', line)
    int_list = list(map(int, blue_values))
    is_outlier = False
    if max(int_list)>blue_max:
        is_outlier = True 
    return is_outlier 

def red_has_outlier(line: str) -> bool:
    red_values = re.findall(r'(\d+) red', line)
    int_list = list(map(int, red_values))
    is_outlier = False
    if max(int_list)>red_max:
        is_outlier = True 
    return is_outlier 

def outlier_in_line(line: str) -> bool:
    return green_has_outlier(line) or blue_has_outlier(line) or red_has_outlier(line)

def main():
    sum = 0
    id = 0
    for line in sys.stdin:
        id += 1
        if not outlier_in_line(line):
            sum += id
    print(sum)
    
if __name__ == "__main__":
    main()

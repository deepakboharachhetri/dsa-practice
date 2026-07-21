from ast import List
import sys


def find_maximum_number(arr: List[int]) -> int:
    maximum = -sys.maxsize - 1
    for element in arr:
        if element > maximum:
            maximum = element
    return maximum

if __name__ == "__main__":
    array = [4, 5, 6, 7, 8, 11, 77, 101, 200, 5000, 5001, 2002]
    print(find_maximum_number(array)) #user-defined function
    print(max(array)) #built-in function

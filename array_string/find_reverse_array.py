"""
Algorithm
-------------------
i)DSA  Approach
----------------
1. first find the length of the array
2. Iterate from last of the array and append(add in last position) in new array
3.return the new_array


ii) pythonic approach
----------------------
1. reverse() -----> method fo list only(modify present array), time O(n), space O(n)
  list.reverse()

2. reversed() ---->  method for sequential data type  list, tuple, string, range  ( create reverse iterator ),
time create iterator O(1),O(n),space(1)
   - for list, tuple
     List(reversed(.....)

   - for string
    ""+join(reversed(string))

   - range
    list(reversed(range(5)))

3. slicing  --> create new object -> time O(n) ,space O(n)
  array[::-1]
"""
from ast import List

def find_maximum_number_return_new(array):
    reversed_array = []
    for i in range(len(array)-1,-1,-1):
              reversed_array.append(array[i])
    return reversed_array
def find_maximum_number_updated_current(array):
    length= len(array)
    for i in range(length//2):
        temp=array[i]
        array[i]=array[-i-1]
        array[-i-1]=temp

if __name__=="__main__":
    arr=[1,5,7,0,-1,2,5]
    print(arr)
    print("custom function", find_maximum_number_return_new(arr))
    find_maximum_number_updated_current(arr) # update arr
    print("custom function", arr)
    arr.reverse()# update  arr
    print("using reverse()",arr)
    new_arr=List(reversed(arr)) #create new_arr
    print("using reversed() ",new_arr)

    print("using slicing ", arr[::-1]) # create copy and return new_arr


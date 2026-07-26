def remove_duplicates_using_array(array):
    return list(set(array))

if __name__ == "__main__":
    arr=[1,2,3,3,4,5,6,6,7,8,9]
    print("remove duplicates from array using set: ",remove_duplicates_using_array(arr))

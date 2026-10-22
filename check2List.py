# Function to check if arr1 and arr2 contain the same elements
def areEqual(arr1, arr2):
    # If lengths of arrays are not equal
    if len(arr1) != len(arr2):
        return False

    # Dictionary to store arr1 elements and their counts
    mp = {}
    for num in arr1:
        mp[num] = mp.get(num, 0) + 1

    # Traverse arr2 and check if all elements are present in arr1
    # with the same counts
    for num in arr2:
        # If an element in arr2 is not in arr1
        if num not in mp:
            return False
        # If an element appears more times in arr2 than in arr1
        if mp[num] == 0:
            return False
        # Decrease the count of arr2 elements in the dictionary
        mp[num] -= 1

    return True

# Driver code
if __name__ == "__main__":
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]

    # Function call
    if areEqual(arr1, arr2):
        print("Yes")
    else:
        print("No")
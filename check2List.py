from collections import Counter


# Function to check if arr1 and arr2 contain the same elements
def areEqual(arr1, arr2):
    # If lengths of arrays are not equal
    if len(arr1) != len(arr2):
        return False

    # Compare element frequencies using C-optimized Counter
    return Counter(arr1) == Counter(arr2)

# Driver code
if __name__ == "__main__":
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]

    # Function call
    if areEqual(arr1, arr2):
        print("Yes")
    else:
        print("No")

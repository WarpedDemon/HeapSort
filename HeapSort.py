#Internet source / insperation: https://www.programiz.com/dsa/heap-sort

#To sort a[left...right] into ascending order:
#1. If left < right:
#1.1. Partition a[left...right] such that
#a[left...p–1] are all less than or equal to a[p], and
#a[p+1...right] are all greater than or equal to a[p].
#1.2. Sort a[left...p–1] into ascending order.
#1.3. Sort a[p+1...right] into ascending order.
#2. Terminate.

# Test Vars: a = [4,3,4,5,2,3,4,6,8,9,10]  # O(1)

# Test Vars: 
a = ["fox", "cow", "pig", "cat", "rat", "lion", "tiger", "goat", "dog"]  # O(1)
# Test Vars: a = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 99, 1, 12]  # O(1)

arr = a  # O(1)

# Heapify
def Heapify(Data, n, i, NumberOfComparisons):

    largest = i  # O(1)
    l = 2 * i + 1  # O(1)
    r = 2 * i + 2  # O(1)

    NumberOfComparisons += 1  # O(1)
    if l < n and Data[largest] < Data[l]:  # O(1)
        largest = l  # O(1)

    if r < n and Data[largest] < Data[r]:  # O(1)
        largest = r  # O(1)

    if largest != i:  # O(1)
        Data[i], Data[largest] = Data[largest], Data[i]  # O(1)
        NumberOfComparisons += 1  # O(1)

        # Total time complexity: O(log(n))
        # Total space complexity: O(1)
        Heapify(Data, n, largest, NumberOfComparisons)  # O(log(n))

def HeapSort(Data):

    n = len(Data)  # O(1)
    NumberOfComparisons = 0 # O(1)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):  # O(n)
        Heapify(Data, n, i, NumberOfComparisons)  # O(log(n))

    # Extract elements one by one
    for i in range(n-1, 0, -1):  # O(n)
        Data[i], Data[0] = Data[0], Data[i]  # O(1)
        NumberOfComparisons += 1  # O(1)
        Heapify(Data, i, 0, NumberOfComparisons)  # O(log(n))

    # Total time complexity: O(n*log(n))
    # Total space complexity: O(1)
    return Data, NumberOfComparisons  # O(1)

print(HeapSort(arr))  # O(n*log(n))
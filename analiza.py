



x = []
with open("passwords_file") as file:
    for l in file:
        x.append(l.strip())

print(x[0])
file.close()


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(x)

    print("Sorted array is: ")
    printList(x)

# *************************
# # sort big files
# *************************

def insertion_sort(array, left=0, right=None):

    if right is None:

        right = len(array) - 1


    # Loop from the element indicated by

    # `left` until the element indicated by `right`

    for i in range(left + 1, right + 1):

        # This is the element we want to position in its

        # correct place

        key_item = array[i]


        # Initialize the variable that will be used to

        # find the correct position of the element referenced

        # by `key_item`

        j = i - 1


        # Run through the list of items (the left

        # portion of the array) and find the correct position

        # of the element referenced by `key_item`. Do this only

        # if the `key_item` is smaller than its adjacent values.

        while j >= left and array[j] > key_item:

            # Shift the value one position to the left

            # and reposition `j` to point to the next element

            # (from right to left)

            array[j + 1] = array[j]

            j -= 1


        # When you finish shifting the elements, position

        # the `key_item` in its correct location

        array[j + 1] = key_item


    return array


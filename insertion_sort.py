unsorted = [3, 4, 2, 5, 7, 2, 9, 3, 76, 5, 4]

def insertion_sort(li):
    # iterate up the list, and for eacch item iterate down until we find the place that the item belongs!
    for i in range(len(li)):
        # store the current number (for comparison)
        current_number = li[i]
        # loop backwards until we find a smaller number than the stored number
        j = i - 1
        while j >= 0 and current_number < li[j]:
            li[j], li[j + 1] = li[j + 1], li[j]
            j -= 1



insertion_sort(unsorted)

print(unsorted)
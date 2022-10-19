needs_swap = [1, 2, 'four', 3]

# order of how things are = order how you want them to be 
needs_swap[2], needs_swap[3] = needs_swap[3], needs_swap[2]

# print(needs_swap)


unsorted = [4, 1, 5, 8, 3, 9, 7, 6]

def bubble_sort(li):
    # keep a flag for whether or not a swap was made
    has_swapped = True
    while has_swapped:
        # first thing -- set our flag to be False in case no swap is made
        has_swapped = False
        # loop over entire list
        for i in range(len(li) -1):
            # check neighbor's values
            if li[i] > li[i + 1]:
                # swap them if i is bigger than i + 1
                li[i], li[i + 1] = li[i + 1], li[i]
                # since we made a swap, indicate that another iteration is needed
                has_swapped = True 


bubble_sort(unsorted)

print(unsorted)









# def bubble_swapping(list, swapped=None):
#     if list == 0:
#         return f'please provide something to sort!'
#     while True:
#         swapped = False
#         for index, value in enumerate(list):
#             if value > list[index+1]:
#                 list[index], list[index+1] = list[index+1], list[index]
#                 swapped = True
#         else:
#             return({list})

# print(bubble_swapping([1, 2, 5, 3, 4]))
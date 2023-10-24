#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    # O(n) only loops through the list once
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(1, len(items)):
        if items[i] < items[i - 1]:
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    # O(n^2) (worst) O(n) (best)
    TODO: Memory usage: ??? Why and under what conditions?
    # O(1) because no new memory is allocated for the sorting"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    if is_sorted(items) == True:
        return items

    for i in range(len(items)):
        swapped = False
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
            swapped = True
        if not swapped:
            return items
    
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    O(n^2) (worst and best)
    TODO: Memory usage: ??? Why and under what conditions?
    # O(1) because no new memory is allocated for the sorting"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    if is_sorted(items) == True:
        return items

    for i in range(len(items)):
        smallest = items[i]
        swapped = False
        for j in range(i, len(items)):
            if smallest > items[j]:
                smallest = items[j]
                items[j], items[i] = items[i], items[j]
                swapped = True
        if not swapped:
            break
    return items





def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    O(n^2) (worst and best)
    TODO: Memory usage: ??? Why and under what conditions?
    # O(1) because no new memory is allocated for the sorting"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    if is_sorted(items) == True:
        return items

    for i in range(1, len(items)):
        for j in range(0, i):
            if items[i] < items[j]:
                items[i], items[j] = items[j], items[i] # swap the elements
    return items


print('check sorted')
print(is_sorted([1, 2, 3])) # should return true
print(is_sorted([3, 2, 3])) # should return false

print('bubble sort')
print(bubble_sort([3, 2, 31]))
print(bubble_sort([3, 4, 31]))

print('selection sort')
print(selection_sort([3, 4, 2, 1]))

print('insertion sort')
print(insertion_sort([1, 4, 3, 2, 2]))
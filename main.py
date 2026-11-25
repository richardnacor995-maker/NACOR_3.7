
# ASSESSMENT 3.7: SORTING ALGORITHMS
# Name: Richard Nacor

# Full Name
full_name = "Richard Nacor"


# Remove duplicate letters, spaces, and symbols
def create_array(name):
    array = []

    for letter in name:
        if letter.isalpha() and letter.lower() not in [
            x.lower() for x in array
        ]:
            array.append(letter)

    return array


# 1. BUBBLE SORT
def bubble_sort(arr):
    a = arr.copy()

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j].lower() > a[j + 1].lower():
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# 2. SELECTION SORT
def selection_sort(arr):
    a = arr.copy()

    for i in range(len(a)):
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j].lower() < a[min_index].lower():
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


# 3. INSERTION SORT
def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j].lower() > key.lower():
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


# 4. MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 5. QUICK SORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[-1]

    smaller = [
        x for x in arr[:-1]
        if x.lower() <= pivot.lower()
    ]

    greater = [
        x for x in arr[:-1]
        if x.lower() > pivot.lower()
    ]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


# 6. TIMSORT
def tim_sort(arr):
    return sorted(arr, key=str.lower)


# CREATE UNSORTED ARRAY
unsorted_array = create_array(full_name)


# DISPLAY ALL SORTING METHODS
sorting_methods = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Timsort": tim_sort
}


print("======================================")
print("       ASSESSMENT 3.7")
print("        SORTING ALGORITHMS")
print("======================================")

print("Full Name:", full_name)
print("Unsorted Array:", unsorted_array)


for method_name, method_function in sorting_methods.items():

    sorted_array = method_function(unsorted_array)

    print("\n--------------------------------------")
    print("Sorting Method:", method_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:  ", sorted_array)

print("\n======================================")
print("       SORTING COMPLETED!")
print("======================================")

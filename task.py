import timeit, random

def insertion_sort(lst):
    """Sorting by insertion"""
    srt = list(lst)
    for i in range(1, len(lst)):
        key = srt[i]
        j = i-1
        while j >=0 and key < srt[j] :
            srt[j+1] = srt[j]
            j -= 1
        srt[j+1] = key

    return srt

def merge_sorted_arrays(left, right):
    """Merge sorted arrays"""
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_sort(arr):
    """Sorting by merging sorted parts"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge_sorted_arrays(merge_sort(left_half), merge_sort(right_half))

def gen_array(size: int):
    arr = list()
    for i in range(1,size+1):
        arr.append(random.randint(0,100))
    
    return arr
    
if __name__ == "__main__":
    for n in [10, 100, 1000, 10000]:
        test_array = gen_array(n)
        is_t = timeit.timeit('insertion_sort(test_array)', number=20, globals=globals())/20
        ms_t = timeit.timeit('merge_sort(test_array)', number=20, globals=globals())/20
        ts_t = timeit.timeit('sorted(test_array)', number=20, globals=globals())/20
        
        print(f"Sort array {n:5} elements using methond: Insertion {is_t:.8f}, Merged {ms_t:.8f}, Tim {ts_t:.8f}")




# --- Next Function Block ---

import re
import math
from abc import ABC, abstractmethod
from collections import Counter
import functools
import string
import random

class A:
    def print():
        pass
# -----------------------------------------------------
# Function 1: Insertion sort (in-place) using insertion‐like algorithm.
def insertion_sort(arr: list) -> list:
    """
    Sorts the list 'arr' using a variant of insertion sort.
    
    Example:
      Input: [4, 2, 1, 3]
      Output: [1, 2, 3, 4]
    """
    head = arr.copy()
    i = 1
    while i < len(head):
        if head[i] < head[i - 1]:
            j = i - 1
            # Move left until we find a position where head[i] is not less.
            while j >= 0 and head[i] < head[j]:
                j -= 1
            # Insert head[i] at the correct position.
            head.insert(j + 1, head[i])
            # Remove the duplicate element (since head[i] was shifted).
            del head[i + 1]
        else:
            i += 1
    return head


# --- Next Function Block ---


# -----------------------------------------------------
# Function 2: Pairwise swap (inserting elements from end into the middle)
def pairwise_swap(head: list) -> list:
    """
    Given a list 'head', inserts elements from the end into the middle positions.
    The snippet shows inserting element at the end at index i and then removing the duplicate.
    
    Example:
      Input: [1]
      Output: [1]  (For a single element, nothing changes.)
    """
    head = head.copy()
    i = 1
    j = len(head) - 1
    while j > i:
        head.insert(i, head[j])
        del head[j + 1]
        i += 2
    return head


# --- Next Function Block ---


# -----------------------------------------------------
# Function 3: Demonstrate closure with a global variable.
def demonstrate_closure() -> None:
    """
    Demonstrates variable lookup in a closure by printing a global variable.
    """
    def f():
        print(x)
    x = 1
    f()


# --- Next Function Block ---


class A:
    def print():
        pass

# -----------------------------------------------------
# Function 4: Rotate a list by k positions (to the right).
def rotate_list(head: list, k: int) -> list:
    """
    Rotates the list 'head' to the right by k positions.
    
    Example:
      head = [0,1,2], k = 3
      Since k % len(head) == 0, the rotated list is the same.
    """
    n = len(head)
    if n == 0:
        return head
    k = k % n
    # Using slicing for rotation:
    return head[-k:] + head[:-k]


# --- Next Function Block ---


# -----------------------------------------------------
# Function 5: Count distinct substrings in a reversed string.
def count_distinct_substrings(s: str) -> int:
    """
    Reverses the string s, then counts distinct substrings generated by
    expanding from each character.
    
    Note: The original snippet is ambiguous; this function uses a simple
    method to count all distinct substrings.
    """
    s = s[::-1]
    substrings = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.add(s[i:j])
    return len(substrings)


# --- Next Function Block ---


# -----------------------------------------------------
# Function 6: Append text to a file and then read its contents.
def append_and_read_file(filename: str, text: str) -> None:
    """
    Appends 'text' to the file 'filename' and then prints its contents.
    """
    with open(filename, "a") as f:
        f.write(text)
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")


# --- Next Function Block ---


# -----------------------------------------------------
# Function 7: Print numbers missing in a list.
def get_missing_numbers(arr: list) -> list:
    """
    Given a list 'arr', prints and returns numbers in range [0, max(arr))
    that are not present in arr.
    """
    missing = []
    for i in range(max(arr)):
        if i not in arr:
            missing.append(i)
    return missing


# --- Next Function Block ---


# -----------------------------------------------------
# Function 8: Reverse a subarray between two 1-indexed positions.
def reverse_subarray(head: list, left: int, right: int) -> list:
    """
    Reverses a portion of the list 'head' from index left-1 to right-1 (inclusive).
    
    Example:
      head = [1,2,3,4,5,6,8], left = 2, right = 4
      Output: [1, 4, 3, 2, 5, 6, 8]
    """
    # Convert left and right to 0-indexed.
    left_idx = left - 1
    right_idx = right
    new_list = head[:left_idx] + head[left_idx:right_idx][::-1] + head[right_idx:]
    return new_list


# --- Next Function Block ---


# -----------------------------------------------------
# Function 9: Print increasing slices of a list.
def print_increasing_slices(head: list) -> None:
    """
    For each index i in head, prints the slice head[i:j] where j increases based on a rule.
    (The original snippet increases j by j-i each iteration.)
    """
    i = 0
    j = 1
    while i < len(head):
        print(head[i:j])
        i += 1
        j += (j - i)


# --- Next Function Block ---


# -----------------------------------------------------
# Function 10: Remove up to k occurrences across groups and return distinct group count.
def remove_k_occurrences(arr: list, k: int) -> int:
    """
    Counts the occurrences of each element in arr and then “removes” up to k occurrences across groups.
    Returns the number of groups (distinct elements) remaining after removals.
    
    This function uses the Counter to get counts, then iterates through the sorted counts.
    (Based on snippet logic, returns len(count) - j, where j is incremented when count goes below 1.)
    """
    counts = dict(sorted(Counter(arr).items(), key=lambda item: item[1]))
    j = 0
    flag = False
    for key in counts:
        while counts[key] > 0:
            if k > 0:
                counts[key] -= 1
                k -= 1
                if counts[key] < 1:
                    j += 1
            else:
                flag = True
                break
        if flag:
            break
    return len(counts) - j


# --- Next Function Block ---


# -----------------------------------------------------
# Function 11: Reverse chunks of a list (based on index modulus k).
def reverse_chunks(arr: list, k: int) -> list:
    """
    Divides the list 'arr' into chunks of size k and reverses each chunk.
    If the last chunk is smaller than k, leaves it as is.
    
    Example:
      arr = [1,2,3,4], k = 2 → returns [2,1,4,3]
    """
    result = []
    for i in range(0, len(arr), k):
        chunk = arr[i:i+k]
        if len(chunk) == k:
            result.extend(chunk[::-1])
        else:
            result.extend(chunk)
    return result


# --- Next Function Block ---


# -----------------------------------------------------
# Function 12: Transform list by conditional chunk reversal.
def transform_list_by_chunks(arr: list) -> list:
    """
    Transforms the list 'arr' by taking chunks (whose size depends on a changing parameter k)
    and reverses the chunk if its length is even, otherwise leaves it as is.
    
    The update of the start index uses the rule i = k*k - i and increments k by 1 each iteration.
    (This is one interpretation of the snippet.)
    """
    nums = []
    i = 0
    k = 1
    n = len(arr)
    while i < n:
        # Determine chunk size as k; slice from i to i+k.
        chunk = arr[i:i+k]
        if len(chunk) % 2 == 0:
            nums.extend(chunk[::-1])
        else:
            nums.extend(chunk)
        # Update i as shown in snippet: i = k*k - i.
        i = k * k - i
        k += 1
    return nums


# --- Next Function Block ---


# -----------------------------------------------------
# Function 13: Remove elements until list is sorted.
def remove_until_sorted(nums: list) -> (list, int):
    """
    Repeatedly removes an element that is out of order until the list is sorted.
    Returns a tuple of (final sorted list, number of iterations).
    
    Example:
      nums = [4,5,7,7,13]
    """
    count = 0
    while nums != sorted(nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i+1] < nums[i]:
                del nums[i+1]
            else:
                i += 1
        count += 1
    return nums, count


# --- Next Function Block ---


# -----------------------------------------------------
# Function 14: Count common elements in two lists.
def count_common_elements(head: list, nums: list) -> int:
    """
    Counts how many elements in 'head' are also present in 'nums'.
    
    Example:
      head = [0,1,2,3], nums = [0,1,3] → returns 3.
    """
    count = 0
    for item in head:
        if item in nums:
            count += 1
    return count


# --- Next Function Block ---


# -----------------------------------------------------
# Function 15: Length of sublist after the maximum element.
def length_after_max(head: list) -> int:
    """
    Returns the length of the sublist after the maximum element in head.
    
    Example:
      head = [5,2,13] → maximum is 13 at index 2, so returns len(head) - 3 = 0.
    """
    if not head:
        return 0
    max_val = max(head)
    max_index = head.index(max_val)
    return len(head) - (max_index + 1)


# --- Next Function Block ---


# -----------------------------------------------------
# Function 16: Maximum reachable index with given bricks and ladders.
def max_reachable_index(heights: list, bricks: int, ladders: int) -> int:
    """
    Simulates moving from the first building to subsequent buildings using bricks and ladders.
    For each step, if the next building is higher, uses bricks (or ladders if insufficient bricks).
    Returns the maximum index reached (0-indexed).
    
    Example:
      heights = [14,3,19,3], bricks = 17, ladders = 0.
    """
    i = 0
    while i < len(heights) - 1:
        diff = heights[i+1] - heights[i]
        if diff > 0:
            if diff > bricks and ladders > 0:
                ladders -= 1
            elif diff <= bricks:
                bricks -= diff
            else:
                break
        i += 1
    return i


# --- Next Function Block ---


# -----------------------------------------------------
# Function 17: Insert GCD between adjacent elements.
def insert_gcd_between_adjacent(arr: list) -> list:
    """
    For each pair of adjacent elements in arr, computes their GCD and inserts it between them.
    
    Example:
      arr = [18,6,10,3] 
      Returns a new list with the GCD inserted between adjacent pairs.
    """
    def gcd(a, b):
        return math.gcd(a, b)
    res = []
    for i in range(len(arr)-1):
        res.append(arr[i])
        res.append(gcd(arr[i], arr[i+1]))
    res.append(arr[-1])
    return res


# --- Next Function Block ---


# -----------------------------------------------------
# Function 18: Merge parts of two lists.
def merge_lists(list1: list, list2: list, a: int, b: int) -> list:
    """
    Merges segments of list1 and list2:
      - Takes the first a elements from list1.
      - Then all elements from list2.
      - Then all elements of list1 after index b.
    
    Example:
      list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
      Returns: list1[:3] + list2 + list1[5:]
    """
    return list1[:a] + list2 + list1[b+1:]


# --- Next Function Block ---




# -----------------------------------------------------
# Function 1: Find the nth number in a custom sequence.
def find_nth_number(n: int) -> int:
    """
    Finds and returns the nth number in a sequence defined by:
      - For numbers less than 7, every number is counted.
      - For numbers >= 7, if the number is divisible by 7, it is skipped.
      - Otherwise, if the number is composite (i.e. it has a divisor other than 1 and itself), it is counted.
    
    This is one interpretation of the snippet.
    """
    count = 0
    i = 1
    while count < n:
        if i < 7:
            count += 1
        else:
            # Skip numbers divisible by 7.
            if i % 7 == 0:
                i += 1
                continue
            prime_flag = False  # Actually, true means composite.
            j = 2
            while j < i:
                if i % j == 0:
                    prime_flag = True
                    break
                j += 1
            if prime_flag:
                count += 1
                print("Counting:", i)
        if count == n:
            break
        i += 1
    return i


# --- Next Function Block ---


# -----------------------------------------------------
# Function 2: Process folder paths and select one per key.
def process_folders(folders: list) -> dict:
    """
    Processes a list of folder paths and builds a dictionary keyed by the first two characters.
    If a key already exists, the folder with the shorter path is kept; if equal, a new entry with the full
    folder string is added.
    
    Example:
      folders = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    """
    d = {}
    i = 0
    while i < len(folders):
        key = folders[i][:2]
        if key in d:
            # Keep the one with the shorter length
            if len(folders[i]) < len(d[key]):
                d[key] = folders[i]
            elif len(folders[i]) == len(d[key]):
                # In the snippet, a new key is added with folder itself.
                d[folders[i]] = folders[i]
        else:
            d[key] = folders[i]
        i += 1
    return d


# --- Next Function Block ---


# -----------------------------------------------------
# Function 3: Print binary representations of numbers.
def print_binary(nums: list) -> None:
    """
    Given a list of numbers, prints each number along with its binary representation.
    """
    i = 0
    while i < len(nums):
        print(bin(nums[i]), nums[i])
        i += 1


# --- Next Function Block ---


# -----------------------------------------------------
# Function 4: Calculate an expression using logarithms.
def calculate_expression(a: int, b: int) -> int:
    """
    If a is 0 and b is not, returns b.
    If b is 0 and a is not, returns a.
    Otherwise, computes int(math.log(math.exp(a) * math.exp(b))) which is equivalent to a+b.
    
    Example:
      a = 707, b = 2 → returns 709.
    """
    if a == 0 and b != 0:
        return b
    elif b == 0 and a != 0:
        return a
    else:
        return int(math.log(math.exp(a) * math.exp(b)))


# --- Next Function Block ---


# -----------------------------------------------------
# Function 5: Filter even numbers from a list.
def filter_evens(arr: list) -> list:
    """
    Returns a list of even numbers from the given list 'arr'.
    
    Example:
      arr = [1,2,3,4,5,6] → returns [2,4,6].
    """
    return list(filter(lambda x: x % 2 == 0, arr))


# --- Next Function Block ---


# -----------------------------------------------------
# Function 6: Find the maximum average subarray of length k.
def max_average_subarray(nums: list, k: int) -> float:
    """
    Finds the contiguous subarray of length k that has the maximum average.
    Prints the subarray each time a new maximum average is found.
    Returns the maximum average.
    
    Example:
      nums = [-1], k = 1.
    """
    max_avg = float('-inf')
    best_sub = None
    i = 0
    while i < len(nums) - k + 1:
        current_avg = sum(nums[i:i+k]) / k
        if current_avg > max_avg:
            max_avg = current_avg
            best_sub = nums[i:i+k]
            print("New best subarray:", best_sub)
        i += 1
    return max_avg


# --- Next Function Block ---


# -----------------------------------------------------
# Function 7: Binary search on a sorted list.
def binary_search(nums: list, target: int) -> int:
    """
    Performs a binary search on a sorted list 'nums' to find 'target'.
    Returns the index if found; otherwise, returns -1.
    
    Example:
      nums = [1,2,3,1], target = 2 → returns index 1.
    """
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# --- Next Function Block ---


# -----------------------------------------------------
# Function 8: Rank array elements.
def rank_array(arr: list) -> (list, dict):
    """
    Ranks the elements of 'arr' by sorting the unique values and mapping them to ranks starting at 1.
    Replaces each element in arr with its rank.
    
    Example:
      arr = [40,10,20,30] → returns ([4,1,2,3], {10: 1, 20: 2, 30: 3, 40: 4})
    """
    unique_sorted = sorted(set(arr))
    ranking = {val: idx + 1 for idx, val in enumerate(unique_sorted)}
    ranked_arr = [ranking[val] for val in arr]
    return ranked_arr, ranking


# --- Next Function Block ---


# -----------------------------------------------------
# Function 9: Evaluate a string expression.
def evaluate_expression(expr: str):
    """
    Evaluates a string expression using Python's eval.
    
    Example:
      expr = "-9.1234" → returns -9.1234.
    """
    return eval(expr)


# --- Next Function Block ---


# -----------------------------------------------------
# Function 10: Reverse a subarray given left and right indices (1-indexed).
def reverse_subarray(head: list, left: int, right: int) -> list:
    """
    Reverses the subarray of 'head' from index left-1 to right-1 (inclusive).
    
    Example:
      head = [1,2,3,4,5,6,8], left = 2, right = 4 → returns [1,4,3,2,5,6,8].
    """
    left_idx = left - 1
    right_idx = right
    return head[:left_idx] + head[left_idx:right_idx][::-1] + head[right_idx:]


# --- Next Function Block ---


# -----------------------------------------------------
# Function 11: Merge two lists by inserting a segment.
def merge_lists(list1: list, list2: list, a: int, b: int) -> list:
    """
    Merges two lists by taking:
      - The first a elements from list1,
      - Then all elements from list2,
      - Then all elements from list1 after index b.
    
    Example:
      list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
      Returns: list1[:3] + list2 + list1[b+1:].
    """
    return list1[:a] + list2 + list1[b+1:]


# --- Next Function Block ---





def a(n):
    for i in range(0,n+1):
        a = i
        for k in range(n-i):
            print(end=" ")
        b=False
        for j in range(1, 2*i-2):
            print(a, end="")
            if a<3:
                b=True
            if b:
                a+=1
            else:
                a-=1
        print("\r")

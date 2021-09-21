

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

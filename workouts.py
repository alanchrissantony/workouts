

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

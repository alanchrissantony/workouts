

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

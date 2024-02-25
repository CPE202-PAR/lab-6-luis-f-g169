from dataclasses import dataclass
from typing import Any, List

@dataclass
class MinHeap:
    heap_capacity: int = 50          # default capacity of heap is 50

    def __post_init__(self):
        self.heap = [0]*(self.heap_capacity+1)      # index 0 not used for heap
        self.num_items = 0                          # empty heap

    def enqueue(self, item: Any) -> None:
        """inserts 'item' into the heap
        Raises IndexError if there is no room in the heap"""

    def peek(self) -> Any:
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""

    def dequeue(self) -> Any:
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""

    def contents(self) -> List:
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""

    def build_heap(self, alist: List) -> None:
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""

    def is_empty(self) -> bool:
        """returns True if the heap is empty, false otherwise"""

    def is_full(self) -> bool:
        """returns True if the heap is full, false otherwise"""

    def capacity(self) -> int:
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
    
    def size(self) -> int:
        """the actual number of elements in the heap, not the capacity"""

    def perc_down(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

    def perc_up(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

    def heap_sort_ascending(self, alist: List) -> None:
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""

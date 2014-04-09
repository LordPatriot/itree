__author__ = 'LordPatriot'


class Node():
    def __init__(self, median):
        self.median = median
        self.overlap_begin_sort = []
        self.overlap_end_sort = []
        self.right = None
        self.left = None

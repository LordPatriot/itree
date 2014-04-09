__author__ = 'bozo'

from Interval import Interval
from Node import Node
import operator


class IntervalTree():
    def __init__(self):
        self.root = None

    def build(self, array):
        if len(array) > 0:
            # counting the median, which is the key
            median = IntervalTree.get_median_point(self, array)
            # current Node
            n = Node(median)
            left = []
            right = []
            overlap = []

            for i in range(0, len(array)):
                if array[i].begin <= median <= array[i].end:
                    overlap.append(array[i])
                elif array[i].end < median:
                    left.append(array[i])
                elif array[i].begin > median:
                    right.append(array[i])

            n.overlap_begin_sort = sorted(overlap, key=operator.attrgetter("begin"))
            n.overlap_end_sort = sorted(overlap, key=operator.attrgetter("end"), reverse=True)

            if self.root is None:
                self.root = n

            n.left = self.build(left)
            n.right = self.build(right)

            return n
        else:
            return None

    # Method that returns all the intervals that overlap with this point
    def find(self, point):
        if self.root is None:
            return None
        else:
            current_node = self.root
            result = []
            IntervalTree.find_inner(current_node, point, result)

        return result

    # An inner recursion for the find method
    @staticmethod
    def find_inner(current_node, point, result):
        if current_node.median <= point:
            for i in range(0, len(current_node.overlap_end_sort)):
                if point <= current_node.overlap_end_sort[i].end:
                    result.append(current_node.overlap_end_sort[i])
                else:
                    break

            if current_node.right is not None:
                IntervalTree.find_inner(current_node.right, point, result)
        else:
            for i in range(0, len(current_node.overlap_begin_sort)):
                if point >= current_node.overlap_begin_sort[i].begin:
                    result.append(current_node.overlap_begin_sort[i])
                else:
                    break

            if current_node.left is not None:
                IntervalTree.find_inner(current_node.left, point, result)

    # A method to find a median point of an array of intervals
    @staticmethod
    def get_median_point(self, array):
        result = 0
        for i in range(0, len(array)):
            result += (array[i].begin + array[i].end)/2

        result /= len(array)
        return result


if __name__ == "__main__":
    ints = list()
    ints.append(Interval(50, 100))
    ints.append(Interval(5, 30))
    ints.append(Interval(20, 40))
    ints.append(Interval(120, 170))
    ints.append(Interval(140, 145))

    tree = IntervalTree()
    tree.build(ints)

    r = tree.find(142)
    print()

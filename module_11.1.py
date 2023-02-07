import unittest


def merge(list_one, list_two):
    result = []
    i = j = 0
    while i < len(list_one) and j < len(list_two):
        if list_one[i] < list_two[j]:
            result.append(list_one[i])
            i += 1
        else:
            result.append(list_two[j])
            j += 1
    while i < len(list_one):
        result.append(list_one[i])
        i += 1
    while j < len(list_two):
        result.append(list_two[j])
        j += 1
    return result


def merge_sort(s):
    if len(s) == 1:
        return s
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return merge(left, right)


print(*merge_sort([7, 9, 15, 1, 18, 0, 41, 23, 13, 26]))


class TestMergeSort(unittest.TestCase):

    def test1(self):
        x = [4, 12, 47, 20, 15, 3, 10, 33]
        y = sorted(x)
        self.assertEqual(merge_sort(x), y)

    def test2(self):
        x = [8, 5, 1, 14, 21, 2, 7, 25, 6]
        y = sorted(x)
        self.assertEqual(merge_sort(x), y)

    def test3(self):
        x = [2, 41, 34, 6, 18, 80, 54, 4]
        y = sorted(x)
        self.assertEqual(merge_sort(x), y)


unittest.main()

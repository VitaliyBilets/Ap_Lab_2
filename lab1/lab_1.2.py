import unittest


def plan_seds(matrix):
    if matrix == [] or matrix[0] == []:
        return []

    result = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    col = 0
    while col < num_cols:

        if col % 2 == 0:
            row = 0
            while row < num_rows:
                result += [matrix[row][col]]
                row += 1
        else:

            row = num_rows - 1
            while row >= 0:
                result += [matrix[row][col]]
                row -= 1

        col += 1

    return result

    return result
class Test(unittest.TestCase):

       def test_rectangular_matrix(self):
              matrix = [
                     [1, 2, 3, ],
                     [4, 5,  6],
                     [7, 8, 9,]
              ]
              expected = [1, 4, 7, 8, 5, 2, 3, 6, 9]
              self.assertEqual(plan_seds(matrix), expected)


if __name__ == "__main__":
       unittest.main()
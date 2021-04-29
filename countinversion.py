import sys
from typing import List, Tuple


def merge(left: List[int], right: List[int],
          mid: int) -> Tuple[List[int], int]:
    i, j = 0, 0
    cnt = 0
    output = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        elif left[i] > right[j]:
            output.append(right[j])
            j += 1
            cnt += (mid - i)

    output.extend(left[i:])
    output.extend(right[j:])
    return output, cnt


def count(l_input: List[int]) -> int:
    if len(l_input) < 2:
        return l_input[:], 0
    middle = len(l_input) // 2
    a, x = count(l_input[:middle])
    b, y = count(l_input[middle:])
    c, z = merge(a, b, middle)

    return c, z + x + y,


if __name__ == '__main__':
    with open('data.txt') as f:
        data = f.read()
    rows = [int(i) for i in data.split('\n') if i != '']
    _, cnt = count(rows)
    sys.stdout.write(f'Total count inversion: {cnt}')

def make_order(rows, nums):
    return '\n'.join(['*' * rows for _ in range(nums // rows)]) + '\n' + '*' * (nums % rows)


print(make_order(7, 15))

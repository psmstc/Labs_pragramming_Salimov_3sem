
"""
[1, 1, 3, 4]
{0: 1, 1: 1, 2: 3, 3: 4}
"""

def two_sum(lst, target):
    final_tuple = []
    my_dict = dict(zip(range(len(lst)), lst,))
    for l in lst:
        diff = target - l
        for k in my_dict:
            if my_dict.get(k) == diff and k != 1:
                final_tuple.append(k)
                final_tuple.append(l)
            return tuple(final_tuple)


lst = [1, 1, 3, 4]
target = 2

print(two_sum(lst, target))

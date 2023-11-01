
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8


def two_sum(lst, target):
    final_tuple = []
    for i in range(len(lst)-1):
        for j in range(1, len(lst)):
            if (lst[i] + lst[j]) == target:
                final_tuple.append(i)
                final_tuple.append(j)
        return tuple(final_tuple)


print(two_sum(lst, target))


def cheat_sort(seq):
    seq.sort()


def cheat_merge(left, right):
    return sorted(left+right)


# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result


# def merge_sort(seq):
#     if len(seq) <= 1:
#         return seq

#     mid = len(seq) // 2
#     leftHalf = seq[:mid]
#     rightHalf = seq[mid:]

#     sortedLeft = merge_sort(leftHalf)
#     sortedRight = merge_sort(rightHalf)
#     seq.clear()
#     seq.extend(merge(sortedLeft, sortedRight))
#     return seq
# def cheat_sort(seq):
#     seq.sort()

# def cheat_merge(left, right):
#     return sorted(left + right)

def merge(left, right):
    left_idx = 0
    right_idx = 0

    ans = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            ans.append(right[right_idx])
            right_idx += 1
        else:
            ans.append(left[left_idx])
            left_idx += 1

    if left_idx < len(left):
        while left_idx < len(left):
            ans.append(left[left_idx])
            left_idx += 1
    else:
        while right_idx < len(right):
            ans.append(right[right_idx])
            right_idx += 1

    return ans


def merge_sort(seq):
    if len(seq) <= 1:
        return seq

    middle = len(seq)//2
    a = seq[:middle]
    b = seq[middle:]
    a = merge_sort(a)
    b = merge_sort(b)
    ans = merge(a, b)
    for i in range(len(ans)):
        seq[i] = ans[i]
    return seq

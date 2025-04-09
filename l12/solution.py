def pivot_naive(seq):
    return seq[0]

def partition_naive(seq, pivot):
    left = []
    middle = []
    right = []
    for i in seq:
      if i > pivot:
        right.append(i)
      elif i < pivot:
        left.append(i)
      else:
        middle.append(i)
    return left, middle, right

def quicksort_naive(seq):
      if len(seq) <= 1:
        return seq
      pivot = pivot_naive(seq)
      a, b, c = partition_naive(seq, pivot)
      a = quicksort_naive(a)
      c = quicksort_naive(c)
      ans = a + b + c
      for idx, val in enumerate(ans):
        seq[idx] = val
      return seq

def pivot_upgrade(seq, lo, hi):
    middle = (hi+lo)//2
    return seq[middle]

def quicksort_upgrade(seq):
    __quicksort_upgrade(seq, 0, len(seq))

def __quicksort_upgrade(seq, lo, hi):
    if lo == hi:
      return seq
    pivot = pivot_upgrade(seq, lo, hi)
    a, b, c = partition_upgrade(seq, pivot, lo, hi)
    __quicksort_upgrade(seq, lo, lo+a)
    __quicksort_upgrade(seq, hi-c, hi)

def partition_upgrade(seq, pivot, lo, hi):
    [one, two, three] = partition_naive(seq[lo:hi], pivot)
    seq[lo:hi] = one + two + three
    return [len(one), len(two), len(three)]

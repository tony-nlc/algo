def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1):
        for i in range(0, j):
            if (i < j and seq[j] < seq[i]) or (i > j and seq[j] > seq[i]):
                seq[i], seq[j] = seq[j], seq[i]


def selection_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        curr = seq[i]
        j = i-1
        while j >= 0 and seq[j] > curr:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = curr

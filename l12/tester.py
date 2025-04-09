import random

import solution


def make_case(n):
    return random.sample(range(1, 2 * n + 2), n)


def test_partition_naive(size):
    case = make_case(size)
    pivot = random.choice(case)
    [a, b, c] = solution.partition_naive(case, pivot)
    if not all([elt < pivot for elt in a]):
        raise AssertionError(
            f"partition_naive failed for size {size}, not all of the following are less than {pivot}:   {a}"
        )
    if not all([elt == pivot for elt in b]):
        raise AssertionError(
            f"partition_naive failed for size {size}, not all of the following are equal to {pivot}:   {b}"
        )
    if not all([elt > pivot for elt in c]):
        raise AssertionError(
            f"partition_naive failed for size {size}, not all of the following are greater than {pivot}:   {c}"
        )
    return True


def test_quicksort_naive(size):
    case = make_case(size)
    result = case[:]
    solution.quicksort_naive(result)
    if result == sorted(case):
        return True
    else:
        raise AssertionError(
            f"quicksort_naive failed for size {size}, this doesn't look sorted {case}"
        )


def test_quicksort_upgrade(size):
    case = make_case(size)
    result = case[:]
    solution.quicksort_upgrade(result)
    if result == sorted(case):
        return True
    else:
        raise AssertionError(
            f"quicksort_upgrade failed for size {size}, this doesn't look sorted {result}"
        )


def test_partition_upgrade(size):
    def pick_lo_hi(size):
        a, b = random.sample(range(size), 2)
        if a < b:
            return a, b
        elif a > b:
            return b, a
        else:
            return pick_lo_hi(size)

    case = make_case(size)
    result = case[:]
    lo, hi = pick_lo_hi(size)
    pivot = random.choice(result[lo:hi])
    [a, b, c] = solution.partition_upgrade(result, pivot, lo, hi)
    if (a + b + c) != (hi - lo):
        raise AssertionError(
            f"partition_naive failed for size {size}, before partitioning: {case}, lo:{lo}, hi:{hi}, after partitioning: {result}, pivot: {pivot}.  Alleged sizes of partitions do not add up:   {a}+{b}+{c} != {(hi - lo)}"
        )
    if not all([elt < pivot for elt in result[lo : lo + a]]):
        raise AssertionError(
            f"partition_naive failed for size {size}, before partitioning: {case}, lo:{lo}, hi:{hi}, after partitioning: {result}, pivot: {pivot}   Not all of the following are less than {pivot}:   {result[lo : lo + a]}"
        )
    if not all([elt == pivot for elt in result[lo + a : hi - c]]):
        print(case, pivot, lo, hi, result)
        raise AssertionError(
            f"partition_naive failed for size {size}, before partitioning: {case}, lo:{lo}, hi:{hi}, after partitioning: {result}, pivot: {pivot}   Not all of the following are equal to {pivot}:   {result[lo + a: hi - c]}"
        )
    if not all([elt > pivot for elt in result[hi - c : hi]]):
        raise AssertionError(
            f"partition_naive failed for size {size}, before partitioning: {case}, lo:{lo}, hi:{hi}, after partitioning: {result}, pivot: {pivot}   Not all of the following are greater than {pivot}:   {result[hi - c: hi]}"
        )
    return True


def main():
    for name, test_func in [
        ["partition_naive", test_partition_naive],
        ["quicksort_naive", test_quicksort_naive],
        ["quicksort_upgrade", test_quicksort_upgrade],
        ["partition_upgrade", test_partition_upgrade],
    ]:
        try:
            print(f"\ntesting {name}")
            for sz in range(3, 20):
                for i in range(20):
                    test_func(sz)
            print(f"✅  {name} passed tests")
        except Exception as e:
            print(f"❌  {e}")


main()

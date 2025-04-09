import math
import random


def make_case(n, ratio=0.5):
    ratio = min(1.0, max(0.0, ratio))   # clamp to range 0..1
    left_size = math.floor(n * ratio)
    left = sorted(random.sample(range(1, 2 * left_size + 2), left_size))
    right = sorted(random.sample(range(1, 2 * (n - left_size) + 2), (n - left_size)))
    return [left, right]

def do_tests(merge_function, test_count=5, case_size=10, ratio=0.5):
    for i in range(test_count):
        case = make_case(case_size, ratio)
        result = merge_function(case[0], case[1])
        correct = sorted(case[0] + case[1])
        if correct != result:
            error_explanation = f"❌  Sorting failed for sort <{merge_function.__name__}> (test {i+1} of {test_count}, size ${case_size}, ratio ${ratio})"
            raise AssertionError(
                f"{error_explanation}\n   input: {case}\n  output: {result}\n  correct: {correct}"
            )


def import_and_test(sort_name):
    # I was kinda bored, so I did some metaprogramming for laughs.  Sorry.
    IMPORT_FILE = "solution"
    try:
        module = __import__(IMPORT_FILE, globals(), locals(), [sort_name])
    except ImportError as e:
        print("could not import sort_implementations.py")
    if sort_name not in vars(module):
        print(f"✗  {sort_name} not found in sort_implementations.py")
    else:
        sort_func = vars(module)[sort_name]
        try:
            for size in range(5, 51, 5):
                do_tests(sort_func, 20, size)
                do_tests(sort_func, 5, size, 0.1)
                do_tests(sort_func, 5, size, 0.9)
        except Exception as e:
            print(e)
            return
        print(f"✅  {sort_name} passed tests")


for sort_func_name in ["cheat_merge", "merge"]:
    import_and_test(sort_func_name)

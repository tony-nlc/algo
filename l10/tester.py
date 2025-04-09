import random


def make_case(n):
    return random.sample(range(1, 2 * n + 2), n)


def do_tests(sort_function, test_count=5, case_size=10):
    for i in range(test_count):
        case = make_case(case_size)
        result = case[:]
        sort_function(result)
        correct = sorted(case)
        if correct != result:
            error_explanation = f"❌  Sorting failed for sort <{sort_function.__name__}> (test {i+1} of {test_count}, size ${case_size})"
            raise AssertionError(
                f"{error_explanation}\n   input: {case}\n  output: {result}\n  correct: {correct}"
            )


def import_and_test(sort_name):
    # I was kinda bored, so I did some metaprogramming for laughs.  Sorry.
    IMPORT_FILE = "sort_implementations"
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
        except Exception as e:
            print(e)
            return
        print(f"✅  {sort_name} passed tests")


for sort_func_name in ["bubble_sort", "selection_sort", "insertion_sort"]:
    import_and_test(sort_func_name)

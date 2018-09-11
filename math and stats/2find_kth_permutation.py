# Given a set of n elements find their kth permutation.
def find_kth_permutation(arr, k):
    if type(arr) != list:
        return None

    if len(arr) < 2:
        return arr
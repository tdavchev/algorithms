# Given a set of n elements find their kth permutation.

def perm(arr, k, curr, lenarr):
    if len(arr) == 1:
        return curr + arr, k-1

    for i in range(len(arr)):
        curr = curr + [arr[i]]
        ans, k = perm(arr[:i] + arr[i+1:], k, curr, lenarr)
        if k == 0:
            print(ans)
        curr = curr[:-1]


    return curr, k


def fact(n):
    return reduce(lambda x, y:x*y, range(1, n+1), 1)

def kth_perm(arr, k):
    if len(arr) == 0:
        print("len must be at least of size 1")

    if fact(len(arr)) < k:
        print("k is too big")

    perm(arr, k, [], len(arr))

kth_perm([1,2,3,4], 16)

def be_smart(arr, k):
    if len(arr) == 0:
        return None

    ans = []
    #k = 3, arr = [1,2,3], ans --> [2, 1, 3]
    while len(arr) > 1:
        f = fact(len(arr) - 1) # 2, 1
        digit = (k-1) // f # 3-1 // 2 = 1; 0 // 1 = 0
        if digit > 0:
            k = k - (digit*f) # 3 - 1*2 - 1 = 0
        ans.append(arr[digit]) # 2, 1
        arr = arr[:digit] + arr[digit+1:] #[1, 3]

    ans = ans + arr

    print(ans)

be_smart([1,2,3,4], 16)

def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
  if not v:
    print(result)
    return
  
  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  selected = (k - 1) / count
  
  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  find_kth_permutation(v, k, result)

find_kth_permutation([1,2,3,4], 16, [])

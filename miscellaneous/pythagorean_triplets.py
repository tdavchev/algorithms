# Given an integer array find all Pythagorean triplets. 
def pyth_triplets(arr):
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            summed = arr[i]**2 + arr[j]**2
            count = j+1
            while count < len(arr):
                if arr[count] < summed:
                    if arr[count]**2 == summed:
                        print((arr[i], arr[j], arr[count]))
                    count += 1
                else:
                    count = len(arr) + 1

pyth_triplets([4, 16, 1, 2, 3, 5, 6, 8, 25, 10])


# [4, 5, 6, 8, 10, 25]
# i used for c
# j = used for a
# k used for a

def find_et(arr):
    arr.sort()
    if len(arr) == 0:
        return None

    for i in range(len(arr)):
        j = 0 
        k = len(arr)-1
        while j < k:
            if k == i:
                k -= 1

            if j == i:
                j += 1

            triplet = arr[j]**2 + arr[k]**2 - arr[i]**2
            if triplet == 0:
                print((arr[j], arr[k], arr[i]))
                j = k
            elif triplet > 0:
                k -= 1
            elif triplet < 0:
                j += 1

print("smarter...")

find_et([4, 16, 1, 2, 3, 5, 6, 8, 25, 10])

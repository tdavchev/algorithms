def triplets(arr):
    ans = []
    for i in range(len(arr)):
        c = arr[i]
        for j in range(len(arr)):
            if i != j:
                a = arr[j]
                for y in range(j+1, len(arr)):
                    if y != i:                  
                        b = arr[y]
                        if c**2 - (a**2 + b**2) == 0:
                            ans.append([a,b,c])

    return ans

def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

def smart_triplets(arr):
    arr = quicksort(arr)
    ans = []
    for i in range(len(arr)):
        start = 0
        end = len(arr) - 1
        while start < end:
            if i == start:
                start += 1
            elif end == start:
                end -= 1

            equ = arr[i]**2 - (arr[start]**2 + arr[end]**2)
            if equ == 0:
                ans.append([arr[start], arr[end], arr[i]])
                start = end
            elif equ < 0:
                end -= 1
            else:
                start += 1

    return ans
    
    

    return arr

print(smart_triplets([4,16,1,2,3,5,6,8,25,10]))
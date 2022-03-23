text = open(r'C:\Users\Connor\randpy\random\IntegerArray.txt' ,'r')
array = []

for line in text:
    array.append(line)

def merge_and_countSplitInversions(left,right):
    i = 0
    j = 0
    c = []
    inversions = 0
    for k in range((len(left) + len(right))):

        if left[i] < right[j]:
            c.append(left[i])
            print(c , "<- C",  i, "<- left index", j , "<- right index")
            i += 1
            print("If Reached, left[i] < right[j]")
        else:
            c.append(right[j])
            print(c , "<- C",  i, "<- left index", j, "<-right index")
            j += 1
            inversions += (len(left) - i)
            print("Else Reached, left[i > right[j]")
        if i >= (len(left)):
            c += right[j:]
            break
        if j >= (len(right)):
            c += left[i:]
            break
    print(k, "<- K")

    return c , inversions

left = [2,4,8,10,12]
right = [9,11,22,24,30]
expected_output = [2,4,8,9,10,11,12,22,24,30]

leftr = [6,5,4]
rightr =
if merge_and_countSplitInversions(left,right)[1] == expected_output:
    print("Sucess!")
else:
    print("Broken")
    ## print(merge_and_countSplitInversions(left,right))



"""def merge_and_count(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:(len(arr)//2)]
        b = arr[len(arr)//2:]

        a, ai = merge_and_count(a)
        b, bi = merge_and_count(b)

        c = []

        i = 0
        j = 0
        inversions += 0 + ai + bi
        print(inversions,"line 25")
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)
    
    c += a[i:]
    c += b[j:]

    return c, inversions """

test_case = [1,6,2,4,9]
expected = [1,2,4,6,9]



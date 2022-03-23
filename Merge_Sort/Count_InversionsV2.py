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
            return c , inversions
        if j >= (len(right)):
            c += left[i:]
            return c, inversions
    print(k, "<- K")

    return c , inversions

left = [2,4,8,10,12]
right = [9,11,22,24,30]
expected_output = [2,4,8,9,10,11,12,22,24,30]

leftr = [4,5,6]
rightr = [1,2,3]
if merge_and_countSplitInversions(left,right)[1] == expected_output:
    print("Sucess!")
else:
    print("Broken")
    ## print(merge_and_countSplitInversions(left,right))



def merge_and_count(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        length = len(arr)
        mid = length // 2
        left = arr[:mid]
        right = arr[mid:]
        a, ainversions = merge_and_count(left)
        b, binversions = merge_and_count(right)
        c, cinversions = merge_and_countSplitInversions(a,b)

        inversions = ainversions + binversions + cinversions


        return c, inversions 

test_case = [1,6,2,4,9]
expected = [1,2,4,6,9]

print(merge_and_count(array)[1])

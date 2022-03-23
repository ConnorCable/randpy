text = open(r'C:\Users\Connor\randpy\random\IntegerArray.txt' ,'r')
array = []

for line in text:
    array.append(line)

inversions = 0

def count_and_mergeSplitInv(left,right):
    i = 0
    j = 0
    c = []
    global inversions
    for k in range((len(left) + len(right))):

        if left[i] < right[j]:
            c.append(left[i])
            ##print(c , "<- C",  i, "<- left index", j , "<- right index")
            i += 1
            ##print("If Reached, left[i] < right[j]")
        else:
            c.append(right[j])
            ##print(c , "<- C",  i, "<- left index", j, "<-right index")
            j += 1
            inversions += int((len(left) - i))
            ##print("Else Reached, left[i > right[j]")
        if i >= (len(left)):
            c += right[j:]
            break
        if j >= (len(right)):
            c += left[i:]
            break
    ##print(k, "<- K")


def count_and_merge(arr):
    global inversions
    if len(arr) == 1:
        return arr
    else:
        a = arr[:int(len(arr)//2)]
        b = arr[int(len(arr))//2:]
        a = count_and_merge(a)
        b = count_and_merge(b)
        count_and_mergeSplitInv(a,b)
        c = []
        i = 0
        j = 0
        

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        c+= a[i:]
        c+= b[j:]

        return c


test = [3,1,8,5,10,4,9,2,21,25,22,33,14]
count_and_merge(array)   
print(inversions)
print(len(array))

 
def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 

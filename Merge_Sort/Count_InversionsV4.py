text = open(r'C:\Users\Connor\randpy\random\IntegerArray.txt' ,'r')
array = []

for line in text:
    array.append(line)


def merge(left, right):
    result = list()
    i,j = 0,0
    inv_count = 0
    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return result,inv_count

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left, left_inversions = merge_sort(left)
    right, right_inversions = merge_sort(right)
    merged, count = merge(left,right)
    i = j = k = 0
    count += (left_inversions + right_inversions)
    return merged, count
        
                
        

print(merge_sort(array)[1])




        
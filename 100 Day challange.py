
def mergesort(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

#write me tests

def test_mergesort():
    assert mergesort([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]) == [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
    assert mergesort([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]) == [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
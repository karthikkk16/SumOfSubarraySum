def SumOfSubArraySum(array):
    n=len(array)
    prefix=[0]*n
    prefix[0]=array[0]

    for i in range(1,n):
        prefix[i]=prefix[i-1]+array[i]

    sum = 0

    for i in range(len(array)):
        for j in range(i, len(array)):
            if i == 0:
                sum += prefix[j]
            else:
                sum += prefix[j] - prefix[i - 1]

    return sum
array=list(map(int,input().split()))
print(SumOfSubArraySum(array))
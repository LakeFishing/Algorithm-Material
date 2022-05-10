import math

def FindMaxCrossingSubarray(A, low, mid, high):
    leftSum = 0 - (math.inf)
    sum = 0
    maxLeft = 0
    maxRight = 0
    for i in range(mid, low, -1):
        sum = sum + A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    rightSum = 0 - (math.inf)
    sum = 0
    for j in range(mid + 1, high):
        sum = sum + A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    return(maxLeft, maxRight, leftSum + rightSum)

def FindMaximumSubarray(A, low, high):
    if high == low:
        return(low, high, A[low])
    else:
        mid = (low + high) // 2
        (leftLow, leftHigh, leftSum) = FindMaximumSubarray(A, low, mid)
        (rightLow, rightHigh, rightSum) = FindMaximumSubarray(A, mid + 1, high)
        (crossLow, crossHigh, crossSum) = FindMaxCrossingSubarray(A, low, mid, high)
        if (leftSum >= rightSum) and (leftSum >= crossSum):
            return(leftLow, leftHigh, leftSum)
        elif (rightSum >= leftSum) and (rightSum >= crossSum):
            return(rightLow, rightHigh, rightSum)
        else:
            return(crossLow, crossHigh, crossSum)

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(FindMaximumSubarray(A, 0, 15))



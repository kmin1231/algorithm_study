def solution(arr, n):
    length = len(arr)
    answer = []
    if (length%2 == 1):
        for i in range(length):
            if (i%2 == 0): answer.append(arr[i] + n)
            else: answer.append(arr[i])
    else:
        for i in range(length):
            if (i%2 == 1): answer.append(arr[i] +n)
            else: answer.append(arr[i])
    return answer
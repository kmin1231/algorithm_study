def solution(arr, queries):
    answer = arr
    for elem in queries:
        [s, e, k] = elem
        for i in range(s, e + 1):
            if (i % k) == 0: answer[i]+=1
    return answer
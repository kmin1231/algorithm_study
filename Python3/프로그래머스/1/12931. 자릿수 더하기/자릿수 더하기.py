def solution(n):
    answer = 0
    for digit in str(n):
        answer += int(digit)
    return answer
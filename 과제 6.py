'''from collections import deque

def solution(priorities, location):
    queue = deque((p, i) for i, p in enumerate(priorities))
    counter = 0

    while queue:
        max_priority = max(queue, key=lambda x: x[0])[0]
        priority, idx = queue.popleft()

        if priority == max_priority:
            counter += 1
            if idx == location:
                break
        else:
            queue.append((priority, idx))

    return counter

if __name__ == '__main__':
    assert solution([2, 1, 3, 2], 2) == 1
    assert solution([1, 1, 9, 2, 3, 4], 1) == 6
    assert solution([1, 1, 2, 1, 1, 1], 0) == 5

    print("테스트 통과")'''

from collections import deque

def solution(prices):
    n = len(prices)  
    result = [0] * n 

    stack = deque() 

    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()  
            result[j] = i - j  
        stack.append(i)
        
    while stack:
        j = stack.pop()
        result[j] = n - j - 1

    return result 

if __name__ == '__main__':
    prices = [1000, 2000, 3000, 2000, 3000]
    result = solution(prices)
    print(result)
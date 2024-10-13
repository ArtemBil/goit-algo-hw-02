from collections import deque

def is_palindrome(word):
    dequeue = deque()
    
    for char in list(word.lower().strip()):
        dequeue.append(char)
    
    while len(dequeue) > 1:
        if dequeue.pop() != dequeue.popleft():
            return False
        return True
    
    return False
    
word = 'корок'

print(is_palindrome(word))
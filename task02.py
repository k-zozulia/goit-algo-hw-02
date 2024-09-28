from collections import deque

def is_palindrome(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    
    return True 

test_string = "A man a plan a canal Panama"
print(is_palindrome(test_string))
def is_symmetric(expression):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack == [] or stack.pop() != brackets[char]:
                return "Not symmetric"
    
    return "Symmetric" if not stack else "Not symmetric"

test_cases = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for test in test_cases:
    result = is_symmetric(test)
    print(f"{test}: {result}")
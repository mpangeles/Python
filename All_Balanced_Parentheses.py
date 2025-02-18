
#Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
import random
def balanced_parens(n):
    stack = [('', n, 0)]
    result = []
    
    # Loop until we run out of items in the stack
    while stack:
        current, left, right = stack.pop()
        
        # if no '(' or ')' left to add, add current to the result
        if left == 0 and right == 0:
            result.append(current)
            
        # if we can, add a '(' and return to the stack
        if left > 0:
            stack.append((current + '(', left - 1, right + 1))
            
        # if we can, add a ')' and return to the stack    
        if right > 0:
            stack.append((current + ')', left, right - 1))
            
    return result
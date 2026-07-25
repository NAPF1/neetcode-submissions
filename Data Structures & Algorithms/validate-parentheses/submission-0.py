class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "]" : "[", "}" : "{"}

        for c in s: # For every item in list
            if c not in hashmap: # If OPEN item
                stack.append(c) # Add it to the stack
            else: # CLOSE item
                if stack and stack[-1] == hashmap[c]: # Check stack !empty and top matches
                    stack.pop() # GET IT OUT!
                else: 
                    return False
        if not stack:
            return True
        else:
            return False
        
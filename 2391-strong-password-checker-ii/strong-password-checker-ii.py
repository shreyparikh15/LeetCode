class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        
        special = "!@#$%^&*()-+"
        
        is_low = False
        is_up = False
        is_dig = False
        is_spec = False
        for i in range(len(password)):
            ch = password[i]
            if ch.isdigit():
                is_dig = True
            if ch.islower():
                is_low = True
            if ch.isupper():
                is_up = True  
            if ch in special:
                is_spec = True
            if i>0 and password[i]==password[i-1]:
                return False
        if is_dig and is_up and is_low and is_spec:
            return True 
        else:
            return False            
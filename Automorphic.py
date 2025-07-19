def automorphic(n):
    return "Automophric" if str(n*n).endswith(str(n)) else "Not!!"
        
    
print(automorphic(25))
print(automorphic(13))
print(automorphic(76))


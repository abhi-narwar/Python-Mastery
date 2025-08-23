# Take number of test cases
n = int(input())

# Run loop for each test case
for _ in range(n):
    s = input().strip()   # take input string and remove spaces
    
    try:
        float(s)   # check if string can be converted to float
        
        # condition: exactly one dot, and something after the dot
        if s.count('.') == 1 and len(s.split('.')[-1]) > 0:
            print(True)
        else:
            print(False)
    except:
        # if string cannot be converted to float
        print(False)

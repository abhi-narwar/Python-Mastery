n = int(input())
for _ in range(n):
    s = input().strip()
    try:
        # must be convertible to float
        float(s)
        # must have exactly one '.' and at least one digit after '.'
        if s.count('.') == 1 and len(s.split('.')[-1]) > 0:
            print(True)
        else:
            print(False)
    except:
        print(False)

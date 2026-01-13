a = 0
b = 3
while a + b < 8:
    a += 1
    print(a, end='')

# ANSWER: 12345

# STEP-BY-STEP (like playing chess - think ahead):
# Move 1: a=0, check: 0+3=3 < 8? YES → a+=1 (a=1) → print 1
# Move 2: a=1, check: 1+3=4 < 8? YES → a+=1 (a=2) → print 2
# Move 3: a=2, check: 2+3=5 < 8? YES → a+=1 (a=3) → print 3
# Move 4: a=3, check: 3+3=6 < 8? YES → a+=1 (a=4) → print 4
# Move 5: a=4, check: 4+3=7 < 8? YES → a+=1 (a=5) → print 5
# Move 6: a=5, check: 5+3=8 < 8? NO → STOP! Don't print.
# # The output will be: 12345
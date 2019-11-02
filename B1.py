elements = int (input ())
lst = list (map (int, input ().split (maxsplit = elements)))
answer = 0
for i in range (len (lst)):
    if i + 1 < len (lst) and lst [i] > lst [i + 1]:
        answer = answer + 1
print (answer)

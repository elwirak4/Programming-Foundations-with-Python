s = 'nabcaefghijslk'
maxsubs = ""
subs = ""

result = 0
for i in range(len(s)-1):
    if (s[i]<=s[i+1]):
        count +=1
        if count > maxcount:
            maxcount = count
            result = i +1
    else:
        count = 0
startposition = result - maxcount        
        
print("The longest substring in alfabetical order is: ", s[startposition:result +1])

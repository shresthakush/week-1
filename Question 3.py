
input ="This is mE 123"
y=[]
for i in input:
    if not i.isupper():  
        y.append(i)
        
output = ""
for a in y:
    output = output + a + ""

print (output)
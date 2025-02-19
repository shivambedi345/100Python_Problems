a=input('enter something here:')
w=a.split()
for i in range (len(w)):
    w[i]=w[i].lower()

w.sort()
for i in w:
    print(i)



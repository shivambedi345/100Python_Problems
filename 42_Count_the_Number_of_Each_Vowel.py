a="harry potter and the prisoner of azkaban"
vowels="aeiou"
a=a.casefold()
print(a)
count={}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char]+=1
print(count)
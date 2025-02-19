punc="""!()-[]{};:'"\,<>./?@#$%^&*_~"""
string=input("Enter a string: ")
empty_string=""
for char in string:
    if char not in punc:
        empty_string+=char
print("New string after removing punctuation: ",empty_string)

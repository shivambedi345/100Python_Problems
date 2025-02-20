friends={"ram":1,"raju":2,"rakul":5,"hmer":7,"jojo":23}
print(friends)
for key,value in friends.items():
    print(key,":",value)
for key in friends:
    print(key,":",friends[key])
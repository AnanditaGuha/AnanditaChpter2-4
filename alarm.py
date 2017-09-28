now = int(input("what is the time now"))
wait = int(input("how long should we wait"))
then = (now + wait) %24
print(then)
def crackle_pop(i:int) -> str:
    msg = "" 
    if i % 3 == 0:
        msg = "Crackle"
    if i % 5 == 0:
        msg += "Pop"
    if len(msg):
        return msg
    else:
        return str(i)

for i in range(1,101):
    print(crackle_pop(i))

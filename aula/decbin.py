dec = int(input("Informe um número decimal:"))

i = 0 
resp = ""

while dec != 0:
    bin = dec % 2 
    if bin == 1:
        resp = resp + str(bin)
    elif bin == 0:
        resp = resp + str(bin)
    dec = dec // 2

print(resp)
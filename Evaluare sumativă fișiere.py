with open("C:/Users/Alexandra/Desktop/Python/INPUT.txt", 'r') as f:
    print("Nr Numele Prenumele Nota1 Nota2 Nota3")
    print(f.read())
with open("C:/Users/Alexandra/Desktop/Python/INPUT.txt", 'r') as f:
    tx = list(f)

with open("C:/Users/Alexandra/Desktop/Python/INPUT.txt", 'r') as f:
    with open('REZERVA.txt', 'w') as r:
        for i in f:
            r.write(i)    

for i in tx:
    c = i.split()
    nota1 = float(c[3])
    nota2 = float(c[4])
    nota3 = float(c[5])
    medie = (nota1 + nota2 + nota3)/3
    with open('OUTPUT.txt', 'a') as g:
        g.write(c[0])
        g.write(' ')
        g.write(c[1])
        g.write(' ')
        g.write(c[2])
        g.write(' ')
        g.write(str(medie))
        g.write('\n')

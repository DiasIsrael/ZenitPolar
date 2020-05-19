

zenit, polar = 'zenit', 'polar'
texto_final = ''
texto = input('Digite o texto : ')
n = 0
for i in range(len(texto)):
    x = texto[n]
    if x in zenit:
        x = int(zenit.find(texto[n]))
        texto_final += polar[x]
    elif x in polar:
        x = int(polar.find(texto[n]))
        texto_final += zenit[x]
        
    else:
        texto_final += texto[n]
    n += 1

print(texto_final)
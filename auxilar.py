'''ip = '192.168.0.2/24'

lista_ip = ip.split('.')
mascara = lista_ip[3].split('/')
lista_ip[3] = mascara[0]
mascara.pop(0)
print(lista_ip)

print(mascara)'''

'''lista = ['teste']
teste = ['oi']

print(lista, teste)

del lista, teste'''

lista = [0,0,0,0]

print(len(lista))

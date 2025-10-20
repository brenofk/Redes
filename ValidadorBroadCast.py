ip = input ("Digite o seu IP: ");
mask = input ("Digite a mascara: ")
# Mostra o tipo da variavel.
# print(type(ip))
# split é uma função para separar os valores 
partes_do_ip = ip.split('.')

parte1 = int(partes_do_ip[0])
parte2 = int(partes_do_ip[1])
parte3 = int(partes_do_ip[2])
parte4 = int(partes_do_ip[3])

ip_int = (parte1 << 24) | (parte2 << 16) | (parte3 << 8) | parte4


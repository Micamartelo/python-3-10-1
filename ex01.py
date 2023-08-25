km = int(input('Quantos km  foram percorridos? '))
d  = int(input('Quantos dias foram?'))
dias = d *60
pagos = km*0.15
total = pagos + dias
print('Foram pagos: {} por dia e foram pagos por km {:.3f}, e seu total foi {}'.format(dias,pagos,total))
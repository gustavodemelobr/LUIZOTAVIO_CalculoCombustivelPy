d = float(input('Qual é a distância (KM)? '))
x = float(input('Quantas viagens? '))
m = float(input('Qual é a média de consumo L/KM? '))
v = float(input('Qual é o valor do combustível? '))
print()
d2 = d * x
m2 = d2 / m
v2 = m2 * v
print('===' * 16)
print(f'''A distância total será de {d2}km,  
o total de combustível utilizado será de {m2:.1f}L, 
o que equivale à R${v2:.2f}''')

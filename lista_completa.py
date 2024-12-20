import numpy as np # Biblioteca numpy
import matplotlib.pyplot as plot # Biblioteca matplotlib

'''
1. Crie um array NumPy contendo os números de 1 a 10. Em seguida,
transforme-o em um array bidimensional com 2 linhas e 5 colunas.
'''

# 1
print("Questão 1")
matriz_1 = np.arange(1, 11).reshape(2, 5) # Criar matriz 2x5 com os numeros de 1 a 10
print(matriz_1)
print()

'''
2. Crie dois arrays de tamanho 10 contendo números aleatórios entre 1 e 100.
Some, subtraia, multiplique e divida os dois arrays.
'''

#2
print("Questão 2")
array_1 = np.random.randint(1, 101, 10) # Criar um array de 1x10 com os numeros de 1 a 100 aleatoriamente
array_2 = np.random.randint(1, 101, 10) # Criar um array de 1x10 com os numeros de 1 a 100 aleatoriamente
print(array_1)
print(array_2)
print()

print(array_1 + array_2) # somar os dois arrays
print(array_1 - array_2) # subitrair os dois arrays
print(array_1 * array_2) # multiplicar os dois arrays
print(array_1 / array_2) # dividir os dois arrays
print()

'''
3. Crie um array de números de 0 a 50. Extraia os elementos pares e os
múltiplos de 5 desse array.
'''

# 3
print("Questão 3")
array_3 = np.arange(0, 51) # Criar um array de 0 a 50
print(array_3)
print()

array_pares = array_3[array_3 % 2 == 0] # Extrair os elementos pares
array_x5 = array_3[array_3 % 5 == 0] # Extrair os elementos multiplos de 5
print(array_pares)
print(array_x5)
print()

'''
4. Crie um array de 20 números aleatórios entre 0 e 1. Calcule a média, o
desvio padrão, o valor máximo e o mínimo desse array.
'''

# 4
print("Questão 4")
array_4 = np.random.rand(20) # Criar um array de 20 numeros aleatorios entre 0 e 1
print(array_4)
print()

print(np.mean(array_4)) # Calcular a media do array
print(np.std(array_4)) # Calcular o desvio padrao do array
print(np.max(array_4)) # Calcular o valor maximo do array
print(np.min(array_4)) # Calcular o valor minimo do array
print()

'''
5. Crie uma matriz 4x4 preenchida com números de 1 a 16. Obtenha a
transposta dessa matriz e multiplique a matriz original pela transposta.
'''

#5
print("Questão 5")
matriz_4x4 = np.arange(1, 17).reshape(4, 4) # Criar uma matriz 4x4 com os numeros de 1 a 16
print(matriz_4x4)
print()

matriz_transposta = np.transpose(matriz_4x4)
print(matriz_transposta)
print()

print(matriz_4x4 * matriz_transposta)
print()

'''
6. Crie um array de números inteiros aleatórios entre 1 e 100 (tamanho 20).
Substitua todos os valores maiores que 50 por 0.
'''

#6
print("Questão 6")
array_20 = np.random.randint(1, 101, 20) # Criar um array de 1x20 com os numeros de 1 a 100 aleatoriamente
print(array_20)
print()
for i in range(len(array_20)):
  if array_20[i] > 50:
    array_20[i] = 0
print(array_20)
print()

'''
7. Crie um array bidimensional representando notas de 5 alunos em 4 provas.
Calcule a média de cada aluno e a média de cada prova.
'''

#7
print("Questão 7")
array_prova = np.random.randint(1, 11, 20).reshape(5, 4) # Criar um array de 5x4 com os numeros de 1 a 10 aleatoriamente
print(array_prova)

media_aluno = np.mean(array_prova, axis=1) # Calcular a media de cada linha
print(media_aluno)

media_prova = np.mean(array_prova, axis=0) # Calacular a media de cada coluna
print(media_prova)
print()

'''
8. Crie uma matriz quadrada 3x3 aleatória e calcule seus autovalores e
autovetores.
'''

#8
print("Questão 8")
matriz_quadrada = np.random.randint(1, 11, 9).reshape(3, 3) # Criar um array de 3x3 com os numeros de 1 a 10 aleatoriamente
print(matriz_quadrada)
print()
matriz_autovalores, matriz_autovetores = np.linalg.eig(matriz_quadrada) # Calcular os autovalores e autovetores da matriz
print(matriz_autovalores)
print(matriz_autovetores)
print()

'''
9. Dado o seguinte array de valores x=[1,2,3,4,5] e y=[2,4,6,8,10], use
numpy.interp para estimar os valores de y correspondentes a
x=[1.5,2.5,3.5,4.5].
'''

#9
print("Questão 9")
x = [1,2,3,4,5]
y = [2,4,6,8,10]
x_estimar = [1.5, 2.5, 3.5, 4.5]
y_estimar = np.interp(x_estimar, x, y)
print(y_estimar)
print()

'''
10.Gere um conjunto de dados simulando as alturas (em cm) de 100 pessoas,
usando uma distribuição normal com média 170 e desvio padrão 10. Depois
calcule:
a. O percentil 25, 50 (mediana) e 75.
b. A quantidade de pessoas com altura acima de 180 cm.
c. Plote um histograma dos dados usando Matplotlib (não precisa
detalhar o código da plotagem).
'''

#10
print("Questão 10")
alturas = np.random.normal(170, 10, 100)
print(alturas)
print()

#a
print(np.percentile(alturas, 25))
print(np.percentile(alturas, 50))
print(np.percentile(alturas, 75))

#b
print(len(alturas[alturas > 180]))
print()
#c
plot.hist(alturas)
plot.show()
print()

'''
11. Crie um array com os números inteiros de 0 a 20. Converta esse array para o
tipo de dado float e exiba o resultado.
'''

#11
print("Questão 11")
array_inteiros = np.arange(0, 21) # Criar um array de 0 a 20
print(array_inteiros)
print()
array_float = array_inteiros.astype(float) # Converter o array para float
print(array_float)
print()

'''
12.Use numpy.linspace para criar um array com 50 valores igualmente
espaçados entre 0 e 10. Use numpy.arange para criar um array com
valores de 0 a 10, incrementando de 0.2.
'''

#12
print("Questão 12")
array_linspace = np.linspace(0, 10, 50) # Criar um array de 50 valores igualmente espaçados entre 0 e 10
print(array_linspace)
print()
array_arange = np.arange(0, 10, 0.2) # Criar um array de valores de 0 a 10, incrementando de 0.2
print(array_arange)
print()

'''
13.Crie dois arrays 1D de tamanho 5. Eleve cada elemento do primeiro array ao
quadrado e subtraia o correspondente elemento do segundo array.
'''

#13
print("Questão 13")
array_1 = np.random.randint(1, 11, 5) # Criar um array de 1x5 com os numeros de 1 a 10 aleatoriamente
array_2 = np.random.randint(1, 11, 5) # Criar um array de 1x5 com os numeros de 1 a 10 aleatoriamente
print(array_1)
print(array_2)
print()
print(array_1 ** 2 - array_2)
print()

'''
14.Crie um array de tamanho 15 contendo números inteiros aleatórios entre 0 e
100. Use máscaras para:
a. Selecionar todos os números pares.
b. Substituir os números ímpares por -1.
'''

#14
print("Questão 14")
array_15 = np.random.randint(0, 101, 15) # Criar um array de 1x15 com os numeros de 0 a 100 aleatoriamente
print(array_15)
print()

#a
array_pares = array_15[array_15 % 2 == 0] # Extrair os elementos pares
print(array_pares)
print()

#b
array_impares = array_15[array_15 % 2 == 1] # Extrair os elementos impares
array_impares = array_impares -1
print(array_impares)
print()
'''
15.Crie uma matriz 3x3 com números aleatórios entre 1 e 9. Redimensione-a
para 1x9 (flatten) e, em seguida, transforme-a em uma matriz 9x1.
'''

#15
print("Questão 15")
matriz_3x3 = np.random.randint(1, 10, 9).reshape(3, 3) # Criar um array de 3x3 com os numeros de 1 a 9 aleatoriamente
print(matriz_3x3)
print()
matriz_1x9 = matriz_3x3.flatten() # Transformar a matriz em uma matriz 1x9
print(matriz_1x9)
print()
matriz_9x1 = matriz_1x9.reshape(9, 1) # Transformar a matriz em uma matriz 9x1
print(matriz_9x1)
print()

'''
16.Crie dois vetores a=[1,2,3] e b=[4,5,6]. Calcule o produto escalar e o produto
externo (a⊗b).
'''

#16
print("Questão 16")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a)
print(b)
print()
print(np.dot(a, b)) # Calcular o produto escalar
print()
print(np.outer(a, b)) # Calcular o produto externo
print()

'''
17.Crie uma matriz quadrada 3×3 aleatória. Calcule o determinante e, se
possível, a inversa dessa matriz.
'''

#17
print("Questão 17")
matiz_quadrada = np.random.randint(1, 11, 9).reshape(3, 3) # Criar um array de 3x3 com os numeros de 1 a 10 aleatoriamente
print(matiz_quadrada)

det_matiz_quadrada = np.linalg.det(matiz_quadrada) # Calcular o determinante da matriz
print(det_matiz_quadrada)

if det_matiz_quadrada == 0: # Verificar se o determinante é diferente de 0
  print("A matriz não tem inversa")

else:
  inversa_matiz_quadrada = np.linalg.inv(matiz_quadrada) # Calcular a inversa da matriz
  print(inversa_matiz_quadrada)
print()

'''
18.Crie um array representando os coeficientes do polinômio p(x) = x^3 - 4x^2 +
6x - 24. Use funções do NumPy para calcular:
a. As raízes do polinômio.
b. O valor de p(x) para x=2.
'''

#18
print("Questão 18")
coeficientes = np.array([1, -4, 6, -24]) # Criar um array com os coeficientes do polinômio
print(coeficientes)
print()

#a
raizes = np.roots(coeficientes) # Calcular as raízes do polinômio
print(raizes)

#b
valor = np.polyval(coeficientes, 2) # Calcular o valor de p(x) para x=2
print(valor)
print()

'''
19.Crie uma matriz 3×33 \times 33×3 com números de 1 a 9. Subtraia de cada
linha o valor da média dessa linha usando o conceito de broadcasting.
'''

#19
print("Questão 19")
matriz = np.arange(1, 10).reshape(3, 3) # Criar uma matriz 3x33 com os numeros de 1 a 9
print(matriz)
print()

media = matriz - np.mean(matriz, axis=1, keepdims=True) # Subtrair de cada linha o valor da média dessa linha
print(media)
print()

'''
20.Simule um conjunto de dados com 50 amostras (linhas) e 3 características
(colunas) usando números aleatórios entre 0 e 1. Para cada coluna, calcule:
a. A média e o desvio padrão.
b. O valor máximo e o valor mínimo.
c. Normalize os dados de cada coluna para que fiquem no intervalo [0,1].
'''

#20
print("Questão 20")
dados = np.random.rand(50, 3)
print(dados)
print()

#a
media = np.mean(dados)
desvio_padrao = np.std(dados)
print(media)
print(desvio_padrao)
print()

#b
print(np.max(dados))
print(np.min(dados))
print()

#c
dados_normalizados = (dados - np.min(dados)) / (np.max(dados) - np.min(dados))
print(dados_normalizados)
print()

'''
21.Crie:
a. Um array de zeros com tamanho 10.
b. Um array de uns com tamanho 5.
c. Uma matriz identidade 4×4.
'''

#21
print("Questão 21")

#a
array_zeros = np.zeros(10) # Criar um array de zeros
print(array_zeros)
print()

#b
array_uns = np.ones(5) # Criar um array de uns
print(array_uns)
print()

#c
matriz_identidade = np.eye(4) # Criar uma matriz identidade
print(matriz_identidade)
print()

'''
22.Crie um array com os valores x=[0,π/2,π,3π/2,2π]. Calcule o seno e o
cosseno de cada valor.
'''

#22
print("Questão 22")
x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]) # Criar um array com os valores x
print(x)
print()
print(np.sin(x)) # Calcular o seno de cada valor
print(np.cos(x)) # Calcular o cosseno de cada valor
print()

'''
23.Crie um array contendo números inteiros de 1 a 20. Substitua todos os
números que são divisíveis por 3 por -3.
'''

#23
print("Questão 23")
array_inteiros = np.arange(1, 21)
print(array_inteiros)

array_inteiros[array_inteiros % 3 == 0] = -3
print(array_inteiros)
print()

'''
24.Crie uma matriz 5×5 contendo os números inteiros de 1 a 25. Extraia a
submatriz formada pelas linhas 2 a 4 e pelas colunas 2 a 4.
'''

#24
print("Questão 24")
matriz_inteiros = np.arange(1, 26).reshape(5, 5) # Criar uma matriz de 5x5 com os numeros de 1 a 25
print(matriz_inteiros)

sub_matriz = matriz_inteiros[1:4, 1:4] # extrair uma submatriz formada pelas linha 2 a 4 e coluna 2 a 4
print(sub_matriz)
print()

'''
25.Crie um array bidimensional 4×3 com números inteiros aleatórios entre 1 e
10. Calcule:
a. A soma de todos os elementos.
b. O produto dos elementos em cada linha.
'''

#25
print("Questão 25")
array_inteiros = np.random.randint(1, 11, 12).reshape(4, 3) # Criar uma matriz 4x3 com os numeros de 1 a 10 aleatoriamente
print(array_inteiros)
print()

print(np.sum(array_inteiros)) # Calcular a soma de todos os elementos
print()

print(np.prod(array_inteiros, axis=1)) # Calcular o produto dos elementos em cada linha
print()

'''
26.Crie um array com 30 números inteiros aleatórios entre 0 e 10. Identifique os
valores únicos e conte a frequência de cada valor.
'''

#26
print("Questão 26")
array_inteiros = np.random.randint(0, 11, 30) # Criar um array de 1x30 com os numeros de 0 a 10 aleatoriamente
print(array_inteiros)
print()

valores_unicos, frequencia = np.unique(array_inteiros, return_counts=True) # Identificar os valores únicos e contar a frequência de cada valor
print(valores_unicos)
print(frequencia)
print()

'''
27.Crie uma matriz 2×2 para representar uma transformação linear e um vetor
v=[1,2]. Aplique a transformação ao vetor v multiplicando-o pela matriz.
'''

#27
print("Questão 27")
matriz_transformacao = np.array([[1, 2], [3, 4]]) # cria uma matriz 2x2 com os numeros 1, 2, 3 e 4
vetor_v = np.array([1, 2]) # Cria um vetor com os numeros 1 e 2
print(matriz_transformacao)
print(vetor_v)
print()

vetor_transformado = np.dot(matriz_transformacao, vetor_v) # Multiplicando uma matriz e um vetor
print(vetor_transformado)
print()

'''
28.Dado o array x=[0,1,2,3,4] e y=[1,2,0,2,1], crie novos valores para xxx em
passos de 0.1 usando numpy.interp. Plote os valores interpolados (se
necessário, use Matplotlib para exibir).
'''

#28
print("Questão 28")
x = [0,1,2,3,4]
y = [1,2,0,2,1]
xxx = np.arange(0, 4.1, 0.1) # Ele vai fazer todo o seguimento de x só que ao passo de 0.1
yyy = np.interp(xxx, x, y)
print(xxx)
print(yyy)
plot.plot(x, y, 'o', label='Original data')
plot.plot(xxx, yyy, '-', label='Interpolated data')
plot.legend()
plot.xlabel('x')
plot.ylabel('y')
plot.title('Interpolação de dados')
plot.show()
print()

'''
29.Crie um sinal simulado usando y=sin(2πfx), onde f=5 e x varia de 0 a 1 com
100 amostras. Use numpy.fft para calcular a Transformada de Fourier
desse sinal.
'''

#29
print("Questão 29")
f = 5
x = np.linspace(0, 1, 100)
y = np.sin(2*np.pi*f*x)
fft_y = np.fft.fft(y)
print(fft_y)
print()

'''
30.Crie um conjunto de dados simulando uma relação linear: y=2x+3+ruído,
onde x varia de 0 a 10 (20 pontos). Use a álgebra matricial do NumPy para
calcular os coeficientes da regressão linear y=ax+b. Compare os resultados
com os obtidos usando a função numpy.polyfit
'''

#30
print("Questão 30")
x = np.linspace(0, 10, 20)
y = 2*x + 3 + np.random.normal(0, 1, 20)

X = np.vstack((x, np.ones(len(x)))).T
theta = np.linalg.inv(X.T @ X) @ X.T @ y

a_matrix, b_matrix = theta
a_polyfit, b_polyfit = np.polyfit(x, y, 1)

print(a_matrix, b_matrix)
print(a_polyfit, b_polyfit)
print()

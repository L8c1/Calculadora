import matplotlib.pyplot as plt
import numpy as np
import os






# Crie um conjunto de valores x que inclui as raízes

# Defina a função matemática com base nas raízes
def function_2(a, b, c, x):
    return a * x**2 + b * x + c

def plot_function(a, b, c, raiz1, raiz2):
    x = np.linspace(float(min(raiz1, raiz2)) - 1, float(max(raiz1, raiz2)) + 1, 400)
    y = function_2(a, b, c, x)
    return x, y

# Avalie a função para cada valor de x


# Plote a função
def print_function(x, y, raiz1, raiz2):
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Gráfico da Função com Base nas Raízes da Equação do Segundo Grau')
    plt.grid(True)

    # Marque as raízes no gráfico
    plt.plot(raiz1, 0, 'ro', label=f'Raiz 1: {raiz1}')
    plt.plot(raiz2, 0, 'go', label=f'Raiz 2: {raiz2}')
    plt.legend()

    plt.savefig('imagens/graph.png')
    plt.close()





# Evitaremos a utilização do array padrão no Python.

import array as arr
import numpy as np

# Estamos criando um array de pontos flutuantes. No tipo "array", todos os elementos do array devem
# ser do mesmo tipo. Isso é utilizado para otimizarmos ao máximo as operações do array.
arr.array['d', [1, 3, 5]]

# A biblioteca do NumPy é muito utilizada para a realização de cálculos complexos do Python.
# É muito mais recomendado utilizarmos o array do numpy do que o array acima.

# Abaixo, estamos criando um array do NumPy.
np.array([1, 3, 5])
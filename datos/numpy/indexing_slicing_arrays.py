import numpy as np

secuencia = np.arange(10)

secuencia[3]

# Slice funciona similar a los dataframes
secuencia[1:8]

secuencia[7:]

secuencia[:6]

sub_secuencia = secuencia[5:9]

sub_secuencia[0] = 1234

sub_secuencia[0]
secuencia[5]
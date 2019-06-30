# Crear un programa llamado lorem_generator.py,
# que sea capaz de mostrar en pantalla varios párrafosde "Lorem ipsum",
# donde el número de párrafos se especifica al cargar el script.
# El texto puede ser extraído del primer párrafo de https://www.lipsum.com/feed/html
#
# Lorem  ipsum dolor sit  amet, consectetur adipiscing elit.
# Morbi ac  lacinia nibh, nec  faucibus enim.Nullam quis lorem posuere, hendrerit tellus eget, tincidunt ipsum.
# Nam nulla tortor, elementum in elitnec, fermentum dignissim sapien.
# Sed a mattis nisi, sit amet dignissim elit. Sed finibus eros sit ametipsum scelerisque interdum.
# Curabitur justo nibh, viverra a elit vel, elementum hendrerit erat.
# Duisfeugiat mattis ante vel hendrerit.
# Etiam nec nibh nulla.
# Class aptent taciti sociosqu ad litora torquentper conubia nostra, per inceptos himenaeos.

import sys
lorem = "Lorem  ipsum dolor sit  amet, consectetur adipiscing elit.  Morbi ac  lacinia nibh, nec  faucibus enim.Nullam quis lorem posuere, hendrerit tellus eget, tincidunt ipsum. Nam nulla tortor, elementum in elitnec, fermentum dignissim sapien. Sed a mattis nisi, sit amet dignissim elit. Sed finibus eros sit ametipsum scelerisque interdum. Curabitur justo nibh, viverra a elit vel, elementum hendrerit erat. Duisfeugiat mattis ante vel hendrerit. Etiam nec nibh nulla. Class aptent taciti sociosqu ad litora torquentper conubia nostra, per inceptos himenaeos."
n = int(sys.argv[1])

for i in range(n):
    print(lorem)
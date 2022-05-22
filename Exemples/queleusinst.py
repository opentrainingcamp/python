l = ['foo', 'bar', 'baz', 'çorge', 'tititi']

print(l, 'taille de l', len(l))

print('un pop ', l.pop())

print('maintenant l est ', l)

while l:
    if len(l) > 3:
        break
    print(l.pop())

print('fini')



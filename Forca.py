"""Forca"""

print('=' * 10, 'Forca', '=' * 10)
print('Dica: O que é, o que é? Nunca volta, embora nunca tenha ido.')

secreta = 'passado'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if letra not in secreta:
        if chances > 0:
            chances = chances - 1
            print('Você tem {} chances'.format(chances))

    if len(letra) > 1:
        print('Você não pode digitar mais que uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print('PARABÉNS, a letra "{}" pertence ao nome secreto!!!'.format(letra.upper()))
    else:
        print('Você ERROU, tente outra letra.')
        digitadas.pop()

    secreta_temporaria = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temporaria += letra_secreta
        else:
            secreta_temporaria += '*'

    if secreta_temporaria == secreta:
        print('Você GANHOU, o nome secreto é "{}"'.format(secreta.upper()))
        break
    else:
        print('A palavra secreta está assim: {}'.format(secreta_temporaria))

    if chances < 1:
        print('Você esgotou seu número de chances, FIM DE JOGO!!!')
        break

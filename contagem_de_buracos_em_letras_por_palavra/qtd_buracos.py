conta_buraco = {'a': 1, 'B': 2, 'o': 1}
palavras = ['Banana', 'olho', 'çzt']


def contar_qtd_buracos_por_letra():

    """Função que conta a quantidade de buracos que existe nas letras que formam uma palavra.

    Casos de teste de exemplo:
    >>> num_buracos("Banana")
    {'a': 3, 'B': 2}
    >>> num_buracos("olho")
    {'o': 2}
    >>> num_buracos("çzt")
    {0}
    """

    for palavra in palavras:
        buracos(palavra)


def buracos(palavra, buracos=0):
    for letra in palavra:
        if letra in conta_buraco:
            buracos = buracos + conta_buraco[letra]
    print(f'A palavra {palavra}: tem {buracos} buracos')


if __name__ == '__main__':
    contar_qtd_buracos_por_letra()

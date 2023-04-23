if __name__ == '__main__':

    maiorA= 0
    menorB= 3

    for c in range(1, 5):

        Altura = float(input('digite a Altura {}:  '.format(c)))
        if Altura > maiorA:
            maiorA = Altura

            if Altura < menorB:
                menorB = Altura

                print('=' * 20)
                print('Maior Altura:{} '.format(maiorA))
                print('Menor Altura:{} '.format(menorB))
                print('=' * 20)

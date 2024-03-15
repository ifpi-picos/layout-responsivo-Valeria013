#programa que mostra os somatórios do números pares de 1 até 500 com while
cont=1
while cont<=500:
    if cont%2==0:
        i=1
        somatorio=0
        while i<cont:
            somatorio+=i
            i+=1
            print("O somatório de numeros: ",cont,"é:", somatorio)
            cont+=1
            print("Fim do progama")
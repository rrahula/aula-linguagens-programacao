nome = str(input('Digite o primeiro nome. '))
sobrenome = str(input('Digite o sobrenome '))

print('{} , {} '.format(sobrenome[0].upper() + sobrenome[1:].lower(), nome[0].lower() + nome[1:].upper()))


#faça um programa que receba o nome, o sobrenome e o ano de nascimento do usuário, seu programa deve exibir na tela uma única frase seguindo exatamente o modelo:
#“luisa BRAGA nasceu no ano de 1997”

#independente de como o usuário digitar o nome deve ser exibido todo em letras minúsculas e o sobrenome deve ser exibido todo em letras maiúsculas

nome = (input('Digite o seu nome .'))
sobrenome = (input('Digite o seu sobrenome .'))
ano = (input('Digite o seu ano de nascimento '))

print('{} , {},"nasceu no ano de", {}'.format(nome.lower() , sobrenome.upper() , ano))
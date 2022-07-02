# Variáveis no Python. 


nome= 'João Francisco'
sobrenome = 'Torres'

print(nome + sobrenome) # Por serem palavras, pode-se usar no print o simbolo de + para colocar o nome e sobrenome em sequencia. 




ano = 2004
cidade = 'Dianópolis'

print(ano, cidade) # Pelo fato de ano ser declarado por números e cidade por letras, não se pode sequencia-los através de +, ou então dará erro no código.



#--------------------------------------------------------#

#Fazer com que o Usuário informe os valores impregados às variáveis


nome= input('Qual o seu nome?')#isso serve para o usuário informar qual é seu nome
idade= input('Qual a sua idade?')
cidade= input('Em qual cidade você mora?')

print(nome, idade, cidade)



#--------------------------------------------------------#


nome= input('Informe o seu nome: ')

print('Bem vindo(a), '+ nome+ '. Está tudo bem contigo?')
#Usei o + após o nome para deixar o ponto final sequente ao resultado nome. 


#--------------------------------------------------------#


dia= input('Informe seu dia de nascimento: ')
mes= input('Informe seu mes de nascimento: ')
ano= input('Informe seu ano de nascimento: ')

print(dia+'/'+mes+'/'+ano)


#--------------------------------------------------------#

x= int(input('Indique o primeiro número: '))
y= int(input('Indique o segundo número: '))

z= x + y
print('A soma é igual a ', z)

#Somente o input não irá somar os valores. Int irá fazer com que o resultado dado pelo usuário através da mensagem seja interpretado como números, com isso sendo possivel fazer calculos. 




x= input('Indique o primeiro número: ')
y= input('Indique o segundo número: ')

z= x + y
print('A soma é igual a ', z)
# Caso o contrário, ficaria uma sequencia no cosole, ao inves de somar iria mostrar o valor de x seguido do valor de y. 

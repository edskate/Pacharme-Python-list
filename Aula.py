# Estrutura With

# Sem with

arquivo = open('meu_arquivo.txt', 'w')
arquivo.write('Coe Como voce vai , tudo bem com voce')
arquivo.close()

# com with

with open('meu_arquivo.txt', 'w') as arquivo: 
    arquivo.write('E ai tudo bem edy, como foi seu dia hoje ')
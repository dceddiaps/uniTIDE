# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:53:44 2022

@author: userDCPS
"""

import pandas as pd



print("""
__________________ ______   _______     _________ _______  _______  _        _______ 
\__   __/\__   __/(  __  \ (  ____ \    \__   __/(  ___  )(  ___  )( \      (  ____ \
   ) (      ) (   | (  \  )| (    \/       ) (   | (   ) || (   ) || (      | (    \/
   | |      | |   | |   ) || (__           | |   | |   | || |   | || |      | (_____ 
   | |      | |   | |   | ||  __)          | |   | |   | || |   | || |      (_____  )
   | |      | |   | |   ) || (             | |   | |   | || |   | || |            ) |
   | |   ___) (___| (__/  )| (____/\       | |   | (___) || (___) || (____/\/\____) |
   )_(   \_______/(______/ (_______/       )_(   (_______)(_______)(_______/\_______)

  _   _          _    __   _            _     
 | | | |  _ _   (_)  / _| (_)  ___   __| |    
 | |_| | | ' \  | | |  _| | | / -_) / _` |  _ 
  \___/  |_||_| |_| |_|   |_| \___| \__,_| (_)
  
@author: Diogo Silva <dceddiaps@protonmail.com>


#-----------------------------------------------------------------------------#
|Obrigado por usar o TIDE TOOLS unified.                                      |
|                                                                             | 
|Esse programa foi desenvolvido e distribuído gratuitamente.                  |
|Caso queira contribuir, relatar bug ou dar sugestões favor entrar em contato.|
|                                                                             |
|O objetivo do programa é reunir, em um só executável, todas as necessidades  |
|(ou quase todas) que um hidrógrafo pode necessitar para tratamento de marés. |
|                                                                             |
|O programa é orientado ao usuário, abstraindo a programação.                 |
#-----------------------------------------------------------------------------#

Release da primeira versão em 12/03/2022.
***https://www.topster.net/text-to-ascii/epic.html fonte 'epic'/'small'


""")


def print_menu():
    print("""

_______________________________________________________________________________         
|_________________________SELECIONE A OPÇÃO DESEJADA:_________________________|
|                                                                             |
|    1   Previsão de Marés                                                    |
|    2   Resíduos (Maré Observada - Prevista)                                 |
|    3   Reamostragem')                                                       |
|    4   Filtragem Butterworth                                                |  
|    5   PDF2TXT                                                              |
|                                                                             |
|    0   Sair                                                                 | 
|_____________________________________________________________________________|


    """)
    
while True:
    print_menu()
    opcao = int(input())

    if opcao == 0:
        print('Obrigado por utilizar esta aplicação.')
        break

    elif opcao == 1:
        print('#_________Previsão de Marés---------------------------------------------------#')
        print("""\n
A previsão de marés aqui oferecida é uma integração com o programa em FORTRAN 
fornecido pela Publicação Especial n°98 da NOAA. Para mais informações, acessar 
https://tidesandcurrents.noaa.gov/pub.html na secção 'Special Publications'.
    
        """)
        #print('Para voltar ao menu anterior, tecle 9999 em input qualquer')


    elif opcao == 2:
        print('a')
              
    elif opcao == 3:
        print('a')
    
    elif opcao == 4:
        print('----------Filtragem Butterworth----------\n')
        print("""
Selecione o arquivo de maré*:
    
    * Deve estar no formato: yyyy-mm-dd HH:MM:SS       altura
                    Exemplo: 2021-10-05 00:00:00       3.1030    
    
    * O arquivo deve ser digitado como no exemplo abaixo:
          C:\Folder\Projetos\mare\PortoLisboa_tide.txt
          
        """)
    
        root = input()
    
    elif opcao == 5:
        print('a')          
    
    else:
        print('Selecione uma opção válida.\n')          
          
          
          
          
          
          
          
          
          
          
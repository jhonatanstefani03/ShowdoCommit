from funcao import*
import json
import random

tocar_musica(caminho="audios\\silvio-santos-abertura-show-do-milhao.mp3")


digitar_texto("""Está começando mais uma edição do Show do Milhão Tech, onde o conhecimento em programação pode levar você até o topo! Hoje teremos perguntas sobre Python, JavaScript, algoritmos e muito mais!
E atenção, atenção! Aqui, a cada resposta correta, você sobe um nível na stack do sucesso! Mas cuidado! Um erro e o bug pode derrubar seu código!
""")

digitar_texto("""E agora, chamamos nosso primeiro participante! Será que ele consegue rodar o programa sem erros? Ou será que vai cair no famoso "não funciona e não sei por quê"?
Vamos jogar! Primeira pergunta na tela! Valendo 1 milhão de commits bem-sucedidos! 
""")


pular_pergunta =3
cartaz = 1

with open('perguntas.json','r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        perguntas =json.loads(conteudo)

pergunta = random.choice(perguntas)
     
for pergunta in  perguntas:
                
        print('\nPERGUNTA:')
        digitar_texto(pergunta["pergunta"])
        print()

        for i, opcao in  enumerate(pergunta["opções"],1):
                print(f'{i} {opcao}')


        if pular_pergunta >0:
                print(f'\n pulos disponíveis >{pular_pergunta}< digite  "P" para pular')

        resposta = input('digite o numero de sua resposta: ')

        if  resposta.strip() =="p":
                if pular_pergunta >0:
                        pular_pergunta-=1
                        print("vamos para proxima pergunta")
                        continue
                elif pular_pergunta == 0:
                        pergunta
                else:
                        print('voce não tem mais pulos disponíveis precisa responder')
                        

     


        indice_correto =pergunta["opções"].index(pergunta["resposta"])+1

        tocar_musica('audios/silvio-santos-esta-certo-disso.mp3',False)
        confirma = input('voce esta certo disso? (1 para sim/ 2 para nao)')
        parar_musica()

        if resposta.strip() == str(indice_correto):
                tocar_musica('audios/silvio-santos-certa-resposta.mp3',  False)
                print("\n Certa Resposta!") 
        
                print()
                input('enter para continuar')
        elif confirma =="2":
                digitar_texto(pergunta["pergunta"])
        else:
                tocar_musica('audios/silvio-santos-que-pena-voce-errou.mp3', False)

                print('que pena você errou')
                time.sleep(5)
                break
            

                
import pygame
import random
from time import sleep

pygame.init()
som_fgatilho = pygame.mixer.Sound('fgatilho.mp3')
som_tiro = pygame.mixer.Sound('Gunshot.mp3')
print("="*41)
print(" "*10, "\033[4;31;40mBUCKSHOT ROULLETE\033[m")
print("="*41)
print("\033[1;33;40m!!! Bem vindo a roleta russa BUCKSHOT ROULLETE !!!")
print("* Escolher a ação de atirar em si resultará no benefício de jogar outra vez")
print("* Escolher a ação de atirar em seu oponente resultará no benefício de ganhar mais rápido kkkk")
print("* Em seguida, escolha o tambor da arma que irá disparar\033[m")
sleep(9)
print("=====================")

jogador_1=str(input("digite o nome do jogador 1: ")).strip().title()
jogador_2=str(input("digite o nome do jogador 2: ")).strip().title()

jogadores = [jogador_1,jogador_2]

#Definindo a quantidade de tambores na arma:  (5,11)
quantidade_tambores=random.randint(10,21) 

#Criando uma lista com uma range que represente a numeragem de cada tambor da arma:
tambores=list(range(1,quantidade_tambores))

#Definindo a procura de um número válido de tambores carregados, sem que o numero de tambores carregados seja igual a quantidade de tambores da arma e com  no mínimo, 2 tambores vazios a mais do que carregados:
while True: 
 sleep(0.35)
 carregados=random.randint(1,5)
 if carregados!=len(tambores)-2 and carregados!=len(tambores)-1 and carregados < len(tambores):
  break
 
# o número de tambores carregados não pode ser 2 unidades menor do que o total de tambores disponíveis. Isso é feito para garantir que sempre haja pelo menos 2 tambores vazios.
# o número de tambores carregados não pode ser 1 unidade menor do que o total de tambores. Isso impede que haja apenas um tambor vazio e evita um cenário onde a chance de morte seja muito alta.
#  verifica se o número de tambores carregados é menor que o total de tambores

#Escolhendo "carregados" numeros aleatórios DIFERENTES da lista "tambores" para serem "selecionados com munição":
selecionado=random.sample(tambores,k=carregados)


print("="*41)
print(f"Há \033[0;36m{len(tambores)} tambores\033[m na escopeta e\033[0;31m {carregados} deles estão carregados!!!\033[m")


#a variável jogo_ativo é igual a True, a qual mantém o jogo funcionando até que jogo_ativo seja igual a False, encerrando o programa:

jogo_ativo=True
turno_extra=False
turno=0


while jogo_ativo:
    
    chance_morte= (len(selecionado)/len(tambores)) * 100
    
    if turno_extra:
     turno = 1 - turno # inverte o turno ao jogador anterior
     print(f"Turno extra ativado para: \033[0;32m{jogadores[turno]}\033[m")
     turno_extra=False
 
    print("="*51)
    print(f"sua vez de jogar, \033[0;32m{jogadores[turno]}\033[m")
    print("numeragem dos tambores: ",tambores)
    print(f"Chance de Morte: \033[1;33;40m {round(chance_morte,2)} % \033[m")

    while True:
     try:
      acao=str(input("qual será sua ação? em si/oponente: ")).strip()
      if acao!= "em si" and acao != "oponente":
        print("Opção inválida! Por favor, digite 'em si' ou 'oponente'.")
      else:
       break 
     except Exception as e:
      print(f"Erro: {e}")
     
    while True:
     try:
      escolha=int(input("escolha o número do tambor: "))
      if escolha in tambores:
       tambores.remove(escolha)
       break
      else:
       print(f'escolha {escolha} inválida')
     except Exception as e:
      print(f'Erro: {e}')


    som_fgatilho.play()
    print("..... um barulho ecoa no corredor ....")
    sleep(4)

    if escolha in selecionado:


      if acao.lower()=="em si":
       som_tiro.play()
       print(f"seu oponente ri ao ver a poça de sangue no chão, \033[0;31m você morreu {jogadores[turno]}\033[m")

      if acao.lower()=="oponente":
       som_tiro.play()
       print(f"a presença desagradável de seu oponente chega ao fim, \033[0;32m você vive {jogadores[turno]}\033[m, enquanto seu adversário descansa eternamente")
 
      print(f"-----Tambores da \033[0;31m MORTE \033[m ------")
      print(f'\033[0;31m{selecionado}\033[m')

      jogo_ativo=False
      break

    else:
      print("Os dois continuam de pé, mas não por muito tempo...")
      turno = 1 - turno # passa o turno ao proximo jogador

      if acao.lower()=='em si':
       turno_extra = True

pygame.quit()

import random

num_tentativas = 0
min = 0
max = 100

finished = False
pc_guess = random.randint(min, max)

while not finished:
    answer = input(f'A minha tentativa é {pc_guess}. Está correto, demasiado alto ou demasiado baixo?')
    if answer == 'correto':
        num_tentativas += 1
        print(f'Acertei em {num_tentativas} tentativas!')
        finished = True
    elif answer == 'demasiado alto':
        max = pc_guess
        pc_guess = random.randint(min, max)
        num_tentativas += 1
    elif answer == 'demasiado baixo':
        min = pc_guess + 1
        pc_guess = random.randint(min, max)
        num_tentativas +=1
    else:
        print("Não entendi, insira outra resposta")
        answer = input(f'A minha tentativa é {pc_guess}. Está correto, demasiado alto ou demasiado baixo?')


import random

min = 0
max = 100
answer = random.randint(min, max)

guess = int(input(f'O meu número está entre 0 e 100. Descubra qual é:\n'))

num_tentativas = 1

while guess != answer:
    if guess < answer:
        guess = int(input('O meu número é maior, tente outra vez:'))
        num_tentativas += 1
    if guess > answer:
        guess = int(input('O meu número é menor, tente outra vez:'))
        num_tentativas +=1
print(f'Acertaste em {num_tentativas} tentativas, parabéns!')


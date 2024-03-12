from time import sleep
personagens = []

while True:
    print('[1] criar personagens.\n[2] ver personagens.\n[3] encerrar programa.')
    escolha = input('Qual sua opçao: ')

    if escolha == '1':
        nome = input('Qual o nome do personagem: ')
        descricao = input('Qaul a descricao do personagem: ')
        imagem = input('Qual a imagem do personagem: ')
        programa = input('De quak programa é o personagem: ')
        animador = input('Quem é o animador do personagem: ')
        personagem = {"nome": nome, "descricao": descricao, "imagem": imagem, "programa": programa, "animador": animador}
        personagens.append(personagem)

    elif escolha == '2':
        if not personagens:
            print('você ainda não criou seu personagem')
        else:
            for idx, personagem in enumerate(personagens, 1):
                sleep(0.5)
                print(f"\nPersonagens {idx}")
                print(f"Nome: {personagem['nome']}")
                print(f"descricao: {personagem['descricao']}")
                print(f"imagem: {personagem['imagem']}")
                print(f"programa: {personagem['programa']}")
                print(f"animador: {personagem['animador']}")

    elif escolha == '3':
        print('Encerrando seu programa...')
        sleep(0.5)
        print('PROGRAMA ENCERRADO')
        break
    else:
        print('sua opção é invalida!')
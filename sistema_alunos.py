banco_de_dados = []
matricula_atual =0
def criarAluno(nome, idade, curso):
    #permite alterar o valor de uma variável global
    global matricula_atual
    matricula_atual += 1
    #criando um aluno através de um  dicionário
    aluno = {
        'matricula': matricula_atual,
        'nome': nome,
        'idade': idade,
        'curso': curso
    }
    return aluno

def adicionarAluno(nome, idade, curso):
    aluno = criarAluno(nome, idade, curso)
    banco_de_dados.append(aluno)
    print('Aluno adicionado com sucesso!')
def listarTodosAlunos():
    for aluno in banco_de_dados:
        print(f"Matricula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print('--------------------------------\n')

def editarAluno(matricula, nome, idade, curso):
    aluno = alunoExiste(matricula)
    if aluno:
        aluno['nome'] = nome
        aluno['idade'] = idade
        aluno['curso'] = curso
        print('Dados alterados com sucesso!')
    else:
        print('Matricula informada não encontrada!')

def alunoExiste(matricula):
    for aluno in banco_de_dados:
        if aluno['matricula'] == matricula:
            return aluno
    return False

def removerAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        banco_de_dados.remove(aluno)
        print('Aluno removido com sucesso!')
    else:
        print('Matrícula não encontrado!')


def consultarAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        print('---------DADOS DO ALUNO---------')
        print(f'Matricula: {aluno["matricula"]}')
        print(f'Nome: {aluno["nome"]}')
        print(f'Idade:{aluno["idade"]}')
        print(f'Curso{aluno["curso"]}')
    else:
        print('Matrícula não encontrada!')


def menu():
    while True:
        print('---BEM VINDO AO MENU ESCOLAR---')
        print('1 - Adicionar aluno')
        print('2 - Editar aluno')
        print('3 - Remover aluno')
        print('4 - Buscar aluno')
        print('5 - Listar todos os alunos')
        print('6 - Sair do sistema')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            nome = input('Digite o nome do aluno: ')
            idade = input('Digite a idade do aluno: ')
            curso = input('Digite o curso do aluno: ')
            adicionarAluno(nome, idade, curso)
        elif opcao == '2':
            matricula = int(input('Digite a matricula: '))
            nome = input('Digite o nome do aluno: ')
            idade = input('Digite a idade do aluno: ')
            curso = input('Digite o curso do aluno: ')
            editarAluno(matricula,nome,curso)
        elif opcao == '3':
            matricula = int(input('Digite a matricula: '))
            removerAluno(matricula)
        elif opcao == '4':
            matricula = int(input('Digite a matricula: '))
            consultarAluno(matricula)
        elif opcao == '5':
            listarTodosAlunos()
        elif opcao == '6':
            break
        else:
            print('Opção inválida!')
            break
menu()
class PersonalTrainer:

    def __init__(self):
        self.alunos = []

    # CREATE - Cadastrar aluno

    def cadastrar_aluno(self):
        print("=-=-=-=- CADASTRO DE ALUNOS =-=-=-=-")

        nome = input("Digite o nome do aluno: ")

        idade = input("Digite a idade: ")

        if not idade.isdigit():
            print("Opção inválida! Digite uma idade válida.")
            return

        idade = int(idade)

        aluno = {
            "Nome": nome,
            "Idade": idade,
            "Meta": "",
            "Dias": 0,
            "Horas": 0,
            "Lesao": ""
        }

        self.alunos.append(aluno)

        print("Aluno cadastrado com sucesso!")

    # READ - Listar alunos

    def listar_alunos(self):
        print("=-=-=-=- LISTA DE ALUNOS =-=-=-=-")

        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return

        for i, aluno in enumerate(self.alunos):

            idade = aluno["Idade"]

            if idade <= 17:
                categoria = "Adolescente"
            elif idade <= 59:
                categoria = "Adulto"
            else:
                categoria = "Idoso"

            print(f"{i} - {aluno['Nome']} | {categoria}")

    # UPDATE - Atualizar aluno

    def atualizar_aluno(self):
        self.listar_alunos()

        if not self.alunos:
            return

        indice = input("Digite o índice do aluno que deseja atualizar: ")

        if not indice.isdigit():
            print("Opção inválida!")
            return

        indice = int(indice)

        if 0 <= indice < len(self.alunos):

            idade = input("Nova idade: ")

            if not idade.isdigit():
                print("Opção inválida!")
                return

            idade = int(idade)

            self.alunos[indice]["Idade"] = idade

            print("Dados atualizados com sucesso!")

        else:
            print("Aluno não encontrado.")

    # DELETE - Remover aluno

    def remover_aluno(self):
        self.listar_alunos()

        if not self.alunos:
            return

        indice = (input("Digite o índice do aluno que deseja remover: "))

        if not indice.isdigit():
            print("Opção inválida!")
            return

        indice = int(indice)

        if 0 <= indice < len(self.alunos):

            removido = self.alunos.pop(indice)

            print(f"Aluno {removido['Nome']} removido com sucesso!")

        else:
            print("Aluno não encontrado.")

    # ENTREVISTA DO ALUNO

    def entrevistar_aluno(self):
        self.listar_alunos()

        if not self.alunos:
            return

        indice = (input("Digite o índice do aluno para realizar a entrevista: "))

        if not indice.isdigit():
            print("Opção inválida!")
            return

        indice = int(indice)

        if 0 <= indice < len(self.alunos):

            print("=-=-=-=- ENTREVISTA DO ALUNO =-=-=-=-")

            print("\nEscolha sua meta de treino:")
            print("1 - Emagrecer")
            print("2 - Ganhar massa muscular")
            print("3 - Melhorar condicionamento físico")

            op = input("Digite uma opção: ")

            if not op.isdigit():
                print("Opção inválida! Tente novamente.")
                return

            op = int(op)

            if op == 1:
                meta = "Emagrecer"

            elif op == 2:
                meta = "Ganhar massa muscular"

            elif op == 3:
                meta = "Melhorar condicionamento físico"

            else:
                print("Opção inválida!")
                return

            dias = input("Quantos dias por semana pode treinar? ")

            if not dias.isdigit():
                print("Opção inválida!")
                return

            dias = int(dias)

            horas = (input("Quantas horas por dia disponíveis? "))

            if not horas.isdigit():
                print("Opção inválida!")
                return
            horas = int(horas)

            lesao = (input("Possui alguma lesão ou doença? (1-SIM / 2-NÃO) "))

            if not lesao.isdigit():
                print("Opção inválida!")
                return

            lesao = int(lesao)

            if lesao != 1 and lesao != 2:
                print("Opção inválida!")
                return

            self.alunos[indice]["Meta"] = meta
            self.alunos[indice]["Dias"] = dias
            self.alunos[indice]["Horas"] = horas
            self.alunos[indice]["Lesao"] = lesao

            print("Entrevista realizada com sucesso!")

        else:
            print("Aluno não encontrado.")

    # GERAR FICHA DE TREINO

    def gerar_treino(self):
        self.listar_alunos()

        if not self.alunos:
            return

        indice = (input("Digite o índice do aluno: "))

        if not indice.isdigit():
            print("Opção inválida!")
            return

        indice = int(indice)

        if 0 <= indice < len(self.alunos):

            aluno = self.alunos[indice]

            if not aluno["Meta"]:
                print("O aluno ainda não realizou a entrevista!")
                return

            idade = aluno["Idade"]
            meta = aluno["Meta"]

            print("\n=-=-=-=- FICHA DE TREINO =-=-=-=-")
            print(f"Aluno: {aluno['Nome']}")
            print(f"Meta: {meta}")
            print(f"Dias disponíveis: {aluno['Dias']}")
            print(f"Horas por dia: {aluno['Horas']}")

            if aluno["Lesao"] == 1:

                print("\nAtenção: aluno possui lesão ou doença.")
                print("Necessária avaliação profissional antes da definição do treino.")

            else:

                if idade <= 17:
                    print("\nCategoria: Adolescente")
                    print("Treino supervisionado e adaptado à idade.")

                elif idade <= 59:
                    print("\nCategoria: Adulto")
                    print("Treino de força e condicionamento físico.")

                else:
                    print("\nCategoria: Idoso")
                    print("Treino adaptado e supervisionado.")

                print("\nFOCO DO TREINO:")

                print("\nEXERCÍCIOS SUGERIDOS:")

                if meta == "Emagrecer":
                    exercicios = [
                        "Caminhada",
                        "Bicicleta ergométrica",
                        "Agachamento",
                        "Polichinelo adaptado",
                        "Exercícios de fortalecimento"
                    ]
                elif meta == "Ganhar massa muscular":
                    exercicios = [
                        "Agachamento",
                        "Supino",
                        "Remada",
                        "Desenvolvimento de ombros",
                        "Exercícios de fortalecimento muscular"
                    ]

                elif meta == "Melhorar condicionamento físico":
                    exercicios = [
                        "Caminhada rápida",
                        "Bicicleta ergométrica",
                        "Corrida leve",
                        "Corda adaptada",
                        "Circuito de exercícios"
                    ]

                for exercicio in exercicios:
                    print("- " + exercicio)

            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        else:
            print("Aluno não encontrado.")

    # MENU

    def menu(self):

        while True:

            print("\n===== UEMAFIT - SISTEMA DE TREINOS =====")
            print("1 - Cadastrar aluno")
            print("2 - Listar alunos")
            print("3 - Atualizar aluno")
            print("4 - Remover aluno")
            print("5 - Entrevistar aluno")
            print("6 - Gerar ficha de treino")
            print("7 - Sair")

            op = (input("Digite uma opção: "))

            if not op.isdigit():
                print("Opção inválida! Tente novamente.")
                continue

            op = int(op)

            if op == 1:
                self.cadastrar_aluno()

            elif op == 2:
                self.listar_alunos()

            elif op == 3:
                self.atualizar_aluno()

            elif op == 4:
                self.remover_aluno()

            elif op == 5:
                self.entrevistar_aluno()

            elif op == 6:
                self.gerar_treino()

            elif op == 7:
                print("Encerrando o sistema UEMAFIT...")
                break

            else:
                print("Opção inválida! Tente novamente.")

class Locadora:
    def __init__(self):
        # Inicializa os atributos da classe com listas de tuplas.
        # `carros_disponiveis` contém os carros disponíveis para aluguel, cada tupla tem (ID, modelo, preço da diária).
        # `carros_alugados` contém os carros já alugados com o mesmo formato.
        self.carros_disponiveis = [(1, "Agile", 250), (2, "Uno", 150)]
        self.carros_alugados = [(3, "March", 250), (4, "Jeep", 150)]

    def listar_carros(self, lista, titulo):
        # Método para exibir uma lista de carros com título personalizado.
        print(f"\n=== {titulo} ===")
        for carro in lista:
            # Exibe o ID, o modelo e o preço da diária de cada carro.
            print(f"ID: {carro[0]}, Modelo: {carro[1]}, Preço: {carro[2]}")

    def buscar_modelo_por_id(self, id_busca, lista_carros):
        # Busca um carro em uma lista pelo ID.
        for carro in lista_carros:
            if carro[0] == id_busca:  # Se o ID corresponde, retorna a tupla do carro.
                return carro
        return None  # Retorna None caso o ID não seja encontrado.

    def alugar_carro(self, id_carro):
        # Aluga um carro disponível, dado seu ID.
        carro = self.buscar_modelo_por_id(id_carro, self.carros_disponiveis)
        if carro:  # Verifica se o carro foi encontrado.
            dias = entrada_inteiro('Por quantos dias irá alugar? : ')
            valor = dias * carro[2]  # Calcula o custo total do aluguel.
            print(f"Você alugará o {carro[1]} por {dias} dias. Total: R$ {valor}")
            confirmar = input('Deseja confirmar? (sim/não): ').lower()
            if confirmar == "sim":
                # Remove o carro da lista de disponíveis e adiciona na lista de alugados.
                self.carros_disponiveis.remove(carro)
                self.carros_alugados.append(carro)
                print("Aluguel realizado com sucesso!")
        else:
            # Mensagem de erro caso o carro não seja encontrado.
            print("Carro não encontrado.")

    def devolver_carro(self, id_carro):
        # Devolve um carro alugado, dado seu ID.
        carro = self.buscar_modelo_por_id(id_carro, self.carros_alugados)
        if carro:  # Verifica se o carro foi encontrado.
            confirmar = input('Inspeção realizada? (sim/não): ').lower()
            if confirmar == "sim":
                # Remove o carro da lista de alugados e adiciona na lista de disponíveis.
                self.carros_alugados.remove(carro)
                self.carros_disponiveis.append(carro)
                print("Devolução realizada com sucesso!")
        else:
            # Mensagem de erro caso o carro não seja encontrado.
            print("Carro não encontrado.")
def entrada_inteiro(prompt):
    # Função para obter um número inteiro do usuário com validação.
    while True:
        try:
            return int(input(prompt))  # Tenta converter a entrada para inteiro.
        except ValueError:
            # Mostra uma mensagem de erro e solicita nova entrada se ocorrer um erro de conversão.
            print("Entrada inválida. Por favor, digite um número.")
def iniciar_locadora():
    # Inicializa uma instância da classe Locadora.
    locadora = Locadora()

    while True:
        # Exibe o menu principal com as opções disponíveis.
        print("\n=== MENU ===")
        print("1. Alugar carro")
        print("2. Devolver carro")
        print("3. Adicionar novo carro")
        print("4. Sair")

        # Solicita a escolha do usuário com validação de entrada.
        opcao = entrada_inteiro("Escolha uma opção: ")

        if opcao == 1:
            # Lista os carros disponíveis e solicita o ID para alugar.
            locadora.listar_carros(locadora.carros_disponiveis, "Carros Disponíveis")
            id_carro = entrada_inteiro("Digite o ID do carro para alugar: ")
            locadora.alugar_carro(id_carro)  # Aluga o carro.
        elif opcao == 2:
            # Lista os carros alugados e solicita o ID para devolver.
            locadora.listar_carros(locadora.carros_alugados, "Carros Alugados")
            id_carro = entrada_inteiro("Digite o ID do carro para devolver: ")
            locadora.devolver_carro(id_carro)  # Devolve o carro.
        elif opcao == 3:
            # Adiciona um novo carro à lista de disponíveis.
            id = entrada_inteiro("Digite o ID do carro: ")
            modelo = input("Digite o modelo do carro: ")
            valor = entrada_inteiro("Digite o valor da diária: ")
            locadora.carros_disponiveis.append((id, modelo, valor))  # Adiciona o carro.
            print("Carro adicionado com sucesso!")
        elif opcao == 4:
            # Encerra o programa.
            print("Encerrando programa...")
            break
        else:
            # Mostra mensagem de erro se o usuário escolher uma opção inválida.
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente.
    iniciar_locadora()  # Inicia o programa da locadora.


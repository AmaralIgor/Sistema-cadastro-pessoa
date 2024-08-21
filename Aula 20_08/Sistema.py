from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica
from Pessoa import Endereco, PessoaJuridica

def main():
    lista_pf = []
    lista_pj = []

    while True:
        opcao = int(input("Escolha uma Opção: 1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair: "))

        if opcao == 1:
            while True: 
                opcao_pf = int(input("Escolha uma opção: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Remover CPF da lista / 4 - Atualizar item da Lista / 0 - Voltar ao menu anterior: "))
                # Cadastro
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o Nome da Pessoa Fisica: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento  = float(input("Digite o rendimento mensal (somente números): "))

                    data_nascimento = input("Digite a data de nascimento (dd/MM/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade  = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("Tem mais de 18 anos.")
                    else: 
                        print("A pessoa tem menos de 18 anos: Retorne ao Menu...")
                        continue

                    novo_end_pf.logradouro =  input("Digite o Logradouro: ")
                    novo_end_pf.numero = input("Digite o Número: ")

                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pf.endereco_Comercial  = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!")

                # Listar pessoa física
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Data de Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto: R$ {cada_pf.calcular_imposto(cada_pf.rendimento):.2f}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")

                # Remover pessoa
                elif opcao_pf == 3:
                    cpf_para_remover = input("Digite o CPF da pessoa física que deseja remover:")

                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_remover:
                            lista_pf.remove(cada_pf)
                            pessoa_encontrada = True
                            print("Pessoa física removida!")

                            break

                    if not pessoa_encontrada:
                        print("Nenhuma pessoa encontrada")

                # Atualizar Lista
                if opcao_pf == 4:
                    cpf_para_atualizar = input("Digite o CPF que deseja atualizar: ")
                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_atualizar:
                            pessoa_encontrada = True

                            print("Escolha qual dado deseja atualizar")
                            print("N - Nome")
                            print("R - Rendimento")
                            print("L - Logradouro")
                            print("M - Numero")

                            escolha = input("Digite a inicial do atributo que deseja alterar:")

                            if escolha == "N":
                                novo_nome = input(f"O nome atual é {cada_pf.nome}. Digite o novo nome para atualizar: ")
                                cada_pf.nome = novo_nome
                            elif escolha == "R":
                                novo_rendimento = input(f"O rendimento atual é {cada_pf.rendimento}. Digite o novo valor do rendimento: ")
                                cada_pf.rendimento = novo_rendimento
                            elif escolha == "L":
                                novo_logradouro = input(f"O logradouro atual é {cada_pf.logradouro}. Digite o novo logradouro: ")
                                cada_pf.logradouro = novo_logradouro
                            elif escolha == "M":
                                novo_numero = input(f"O número atual é {cada_pf.numero}. Digite o novo número para atualizar")
                                cada_pf.numero = novo_numero
                            else:
                                print("Opção inválida!")
                                break

                            
                # Sair do menu Atual
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break 

                else: 
                    print("Opção inválida, por favor digite uma das opções abaixo indicadas.")


        elif opcao == 2:
            while True:
                opcao_pj = int(input("Escolha uma opção: 1 - Cadastrar Pessoa Jurídica / 2 - Listar Pessoa Jurídica / 3 - Remover CPF da lista / 4 - Atualizar item da Lista 0 - Voltar ao menu anterior: "))
                
                # Cadastro
                if opcao_pj == 1:
                   novapj = PessoaJuridica()
                   novo_end_pj = Endereco()


                   novapj.nome = input("Digite o Nome da Empresa: ")
                   novapj.cnpj = input("Digite o CNPJ: ")
                   novapj.rendimento  = float(input("Digite o rendimento mensal da empresa(somente números): "))
        

                   novo_end_pj.logradouro =  input("Digite o Logradouro da Empresa: ")
                   novo_end_pj.numero = input("Digite o Número: ")

                   novapj.endereco = novo_end_pj

                   lista_pj.append(novapj)
                   print("Cadastro realizado com sucesso!")
                
                
                # Listar pessoa física
                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome da Empresa: {cada_pj.nome}")
                            print(f"CNPJ: {cada_pj.cnpj}")
                            print(f"Imposto: R$ {cada_pj.calcular_imposto(cada_pj.rendimento):.2f}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")


                # Remover pessoa
                elif opcao_pj == 3:
                    cnpj_para_remover = input("Digite o CNPJ da pessoa Jurídica que deseja remover:")

                    empresa_encontrada = False

                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == cnpj_para_remover:
                            lista_pj.remove(cada_pj)
                            empresa_encontrada = True
                            print("Pessoa Jurídica removida!")

                            break

                    if not empresa_encontrada:
                        print("Nenhuma pessoa Jurídica encontrada")
                
                
                # Atualizar Lista
                if opcao_pj == 4:
                    if lista_pj:
                        cnpj_para_atualizar = input("Digite o CNPJ da Empresa que deseja atualizar:")
                        for cada_pj in lista_pj:
                            if cada_pj.cnpj == cnpj_para_atualizar:
                                novo_rendimento = float(input("Digite o novo rendimento: "))
                                cada_pj.rendimento = novo_rendimento
                                print("Rendimento atualizado com sucesso!")
                                break
                        else:
                            print("Nenhum CNPJ encontrado")


                # Sair do menu Atual
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break 

                else: 
                    print("Opção inválida, por favor digite uma das opções abaixo indicadas.")      

            print("Funcionalidades para pessoa jurídica não implementadas.")
            pass


        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema!")
            break

        else: 
            print("Opção Inválida, por favor digite uma das opções válidas.")

if __name__ == "__main__":
    main()  # Chama a função principal

        
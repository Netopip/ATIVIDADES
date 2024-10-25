class Calculadora:
    def __init__(self, numero_1=0, numero_2=0, operador = None, ligado= False):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.operador = operador
        self.ligado = ligado


    def ligar(self):
        self.ligado = True
        return 'Calculadora ligada'

    def desligar(self):
        self.ligado = False
        return 'Calculadora desligada'

    def reset(self):
        self.numero_1 = 0
        self.numero_2 = 0
        self.operador = None
        return 'calculadora resetada'


    def calcular(self):
        if not self.ligado:
            return 'Calculadora desligada'
        else:
            if self.operador == '+':
                resultado = self.numero_1 + self.numero_2
                return resultado
            elif self.operador == '-':
                resultado = self.numero_1 - self.numero_2
                return resultado
            elif self.operador == '*':
                resultado = self.numero_1 * self.numero_2
                return  resultado
            elif self.operador == '/':
                if self.numero_2 <= 0:
                    return 'Erro divisão por zero.'
                else:
                    resultado = self.numero_1 / self.numero_2
                    return resultado
            else:
                return 'Operador inválido'



    def continuarOperando(self, novo_numero, novo_operador):
        resultado = self.calcular()
        self.numero_1 = resultado
        self.numero_2 = novo_numero
        self.operador = novo_operador

        return self.calcular()

def main():
    calculadora = Calculadora()
    while True:
        ligar = input('Pressione L para ligar a calculadora e S para sair!\n').strip().upper()
        #loop principal o usuario liga ou sai da calculadora
        if ligar == 'L':
            print(calculadora.ligar()) #calculadora ligada
            
            while True:
                try:
                    number1 = str(input('Digite o primeiro numero:\n').strip())
                    while True:
                        op = str(input('Digite a operação\n').strip())
                        if op in ['-','+','/','*']:
                            break
                        else:
                            print('Operador Inválido')                  
                    number2 = str(input('Digite o segundo numero:\n')).strip()

                    calculadora.numero_1 = float(number1)
                    calculadora.numero_2 = float(number2) #definição dos valores da instancia
                    calculadora.operador = op
                    
                    resultado = calculadora.calcular() #chama o metodo calcular
                    if resultado == 'Erro divisão por zero.':
                        print(resultado)
                        print(calculadora.reset())
                        continue #caso o divisor for zero o loop reinicia pedindo os primeiros numeros
                    else:
                        print(f'RESULTADO: {resultado}')
                    
                except ValueError:
                    print('Valores invalidos')
                    continue #reinicia o loop caso os valores forem invalidos
                    

                while True: #loop dentro do primeiro while
                    opcao = str(input('Continuar Operando? (S - SIM/ N - NÃO/ C - RESET)')).strip().upper()
                    if opcao in ['SIM', 'S']:#caso o ususario queira continuar operando
                            try:
                                while True:
                                    novo_op = str(input('Digite o operador:\n')).strip()
                                    if novo_op in ['-','+','/','*']:
                                        break
                                    else:
                                        print('Operador Inválido')
                                novo_numero = str(input('Digite o numero:\n')).strip()
                                numero = float(novo_numero)
                                operador = str(novo_op)
                                
                                resultado = calculadora.continuarOperando(numero,operador)
                                if resultado == 'Erro divisão por zero.':
                                    print(resultado)
                                    print(calculadora.reset())
                                    break #se o divisor for zero encerra o loop e a calculadora é resetada e volta para o loop principal
                                else:      
                                    print(f'RESULTADO: {resultado}')

                            except ValueError:
                                print('Dados inválidos')
                                continue# se os valores forem inválidos ele repete o while e não transforma o resultado numa string as variaveis novo operador e novo numero não serão atribuidas
                                
                    elif opcao in ['NAO','NÃO','N']:
                        print(calculadora.desligar())
                        return #ele encerra a função main
                    elif opcao == 'C':
                        print(calculadora.reset())
                        break# encerra o loop while contido no while principal e volta a pedir os primeiros numeros
                    else:
                        print('Opção inválida')

        elif ligar == 'S':
            print(calculadora.desligar())
            break
        else:
            print('Opção inálida')

if __name__ == '__main__':
    main()












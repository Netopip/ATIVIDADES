class Calculadora:
    def __init__(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def atualizar(self,num1,num2,op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        
    def calcular(self):
        if self.op == '+':
            soma = self.num1 + self.num2
            return soma
        elif self.op == '-':
            subtracao = self.num1 - self.num2
            return subtracao
        elif self.op == '*':
            multiplicacao = self.num1 * self.num2
            return  multiplicacao
        elif self.op == '/':
            if self.num2 != 0:
                divisao = self.num1 / self.num2
                return divisao
            else:
                return 'Divisão por zero não é possível'
        else:
            return 'Operação Inválida'

def main():

    # objeto calculadora criado somente uma vez
    calculadora = None
    while True:
        if calculadora is None:
         try:
             numero1 = input('Digite o 1º número:\n').strip()
             numero2 = input('Digite o 2º número:\n').strip()
             operador = input('Digite a operação:\n').strip()
             number1 = int(numero1)
             number2 = int(numero2)
             op = str(operador)

             calculadora = Calculadora(number1,number2, op)
             print(f'O resultado é: {calculadora.calcular()}')

         except ValueError:
             print('Entrada de dados inválida!')

        else:
            try:
                opcao = input('Quer continuar: (1 - SIM/ 2 - NÃO)\n').strip()
                escolha = int(opcao)
                if escolha == 1:
                    novo_valor_a = input('Digite o novo número:\n').strip()
                    novo_valor_b = input('Digite o segundo número:\n').strip()
                    novo_op = input('Digite o operador:\n').strip()
                    number1 = int(novo_valor_a)
                    number2 = int(novo_valor_b)
                    operador = str(novo_op)

                    calculadora.atualizar(number1,number2,operador)
                    print(f'O resultado é: {calculadora.calcular()}')

                elif escolha == 2:
                    print('Fim do programa!')
                    return

                else:
                    print('Escolha não definida.')

            except ValueError:
                print('Entrada inválida!')


if __name__ == '__main__':
    main()

























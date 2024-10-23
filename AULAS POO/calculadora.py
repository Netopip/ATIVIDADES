class Calculadora:
    def __init__(self, num1=0, num2=0, op='+'):
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

    # objegto calculadora criado somente uma vez
    calculadora = Calculadora()

    while True:
        numero_1= input('Digite o primeiro numero:\n').strip()
        numero_2 = input('Digite o segundo numero:\n').strip()
        operacao = input('Digite o operador:\n').strip()
        try:
            num1 = float(numero_1)
            num2 = float(numero_2)
            operador = str(operacao)

            #atualiza os parametros para calculo
            calculadora.atualizar(num1, num2, operador)
            print(f'O resultado da operação de {operacao} dos números ({num1}) e ({num2}) é : {calculadora.calcular()}')#chama a função de calcular e mostra o resultado

            while True:
                escolha = input('Quer continuar: (1 - SIM/ 2 - NÃO)\n').strip()
                try:
                    opcao = int(escolha)
                    if opcao == 1:
                        break #encerra o while e volta para o while da função principal
                    elif opcao == 2:
                        print('Fim! Obrigado por usar a calculadra!')
                        return # encerra a função main e o while
                    else:
                        print('Opção inválida')

                except ValueError:
                    print('Entrada inválida.')

        except ValueError:
            print('Entrada inválida!')


if __name__ == '__main__':
    main()






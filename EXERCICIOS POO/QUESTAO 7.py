from random import randint
from datetime import datetime

class Ticket:
    def __init__(self):
        self.tickets = []

    def criarTicket(self):
        id = randint(1000,10000)
        hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        ticket = {'ID': id,'ENTRADA': hora}
        if ticket['ID'] not in self.tickets:
            self.tickets.append(ticket)
        return ticket

    def mostrarTicket(self):
        for ticket in self.tickets:
            print(f'ID_TICKET: {ticket['ID']}\nEntrada: {ticket['ENTRADA']}')


if __name__ == '__main__':
    ticket = Ticket()
    ticket.criarTicket()
    ticket.mostrarTicket()
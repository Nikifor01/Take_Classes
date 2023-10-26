from typing import Union, Any


class Bank:

    def __init__(self, bank_name: str, rate: Union[float, int]):
        self.__name: str = bank_name
        self.__rate: Union[float, int] = rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        self.__rate = rate

    def get_clients_list(self, name):
        pass


class Clients(Bank):

    def __init__(self, bank_name, rate):
        super().__init__(bank_name, rate)
        self.__clients: list = []
        self.__services: list = []

    def add_client(self, num: int, name: str, inc: Union[int, float], age: int) -> Any:
        self.__clients.append({
            "Number": num,
            "Name": name,
            "Income": inc,
            "Age": age
        })

    def get_clients(self, name):
        found = False

        for i in self.__clients:
            if i['Name'] == name:
                found = True
                return i

        if not found:
            print('Such client not found')

    def add_services(self, name, serv, long, amount):
        found = False

        for i in self.__clients:
            if i['Name'] == name:
                self.__services.append({
                    i['Name']: [serv, long, amount]
                })
                found = True

        if not found:
            print('No such clients')

    def get_service(self, name):
        found = False

        for i in self.__services:
            if name in i.keys():
                found = True
                return i[name]

        if not found:
            return 'Client not found'

    def get_name(self, name):
        for i in self.__clients:
            if i['Name'] == name:
                return i['Name']


class Accounts(Clients, Bank):
    def __init__(self, name, rate, clients, services):
        super().__init__(name, rate, clients, services)
        self.__accounts = {}

    def add_acc(self, name: str, id: str, ac_type: str, initial: Union[int, float] = 0):
        self.__accounts[name] = [id, ac_type, initial]


b = Bank('Sber', 10)
c = Clients(b.name, b.rate)
a = Accounts(b.name, b.rate, c.clients, c.servs)

d = Bank('VTB', 9.7)
e = Clients(d.name, d.rate)
aa = Accounts(d.name, d.rate)

c.add_client(1, 'Anya', 100000, 23)
c.add_client(2, 'Oleg', 150000, 25)

c.add_services('Anya', 'Depo', 5, 1000000)
c.add_services('Oleg', 'Credit', 3, 1000000)
# c.add_services('Leha', 'Credit', 3, 1000000)

print(c.get_clients('afsdfsdf'))
print(c.get_service('Anya'))

print(c.name)
print(e.name)

a.add_acc('Anya', '0001', 'Depo')
a.add_acc('Oleg', '0002', 'Cred')

print(b.__dict__)
print(c.__dict__)
print(a.__dict__)
# print(aa.__dict__)

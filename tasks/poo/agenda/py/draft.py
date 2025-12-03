class Fone: 
    def __init__ (self, id: str, number: str):
        self.__id = id
        self.__number = number
    
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
    def getId(self):
        return self.__id
    
    def getNumber(self):
        return self.__number


class Contact: 
    def __init__ (self, name: str):
        self.__fones: list[Fone] = []
        self.__name = name
        self.__favorited: bool = False
    
    def __str__(self):
        nome = "@ " + self.__name if self.__favorited else "- " + self.__name
        if self.__fones:
            nome += " [" + ", ".join(str(x) for x in self.__fones) + "]"
        return nome
    
    def getName (self):
        return self.__name
    
    def getFones(self):
        return self.__fones

    def addFone(self, fone: Fone):
        self.__fones.append(fone)

    def rmFone (self, index: int):
        if index <= 0 or index > len(self.__fones):
           self.__fones.pop(index)
           return True
        return False
    
    def toogleFavorited (self):
        self.__favorited = not self.__favorited

    def isFavorited (self):
        return self.__favorited
    

class Agenda:
    def __init__ (self):
        self.contacts: list [Contact] = []
    
    def __str__ (self):
        self.contacts.sort(key=lambda c: c.getName())
        return "\n".join(str(c) for c in self.contacts)
    
    def __findPosByName (self, name: str):
        for i, contato in enumerate(self.contacts):
            if contato.getName() == name:
                return i
        return None

    def addContact(self, name: str, fone: list[Fone]):
        if self.__findPosByName(name) != None:
            contato = self.contacts[self.__findPosByName(name)]
        else:
            contato = Contact(name)
            self.contacts.append(contato)
        for i in fone:
            contato.addFone(i)
    
    def removeFone (self, name: str, index: int):
        if self.__findPosByName(name) != None:
            self.contacts[self.__findPosByName(name)].rmFone(index)
        return None
    
    def rmContact(self, name: str):
        if self.__findPosByName(name) != None:
            self.contacts.pop(self.__findPosByName(name))
        return None
    
    def search (self, pattern: str):
        resultado = []
        for contact in self.contacts:  
            if (pattern in contact.getName()):
                resultado.append(contact)
            for fone in contact.getFones():
                if (pattern in fone.getId() or pattern in fone.getNumber()):
                    resultado.append(contact)
        return resultado
    
    def getFavorited (self, favoritado: str):
        for favorited in self.contacts:
            if favoritado != None and favorited.getName() == favoritado:
                favorited.toogleFavorited()
        return self.contacts
    
    def favorites (self):
        favorites = []
        for favorited in self.contacts:
            if favorited.isFavorited():
                favorites.append(favorited)
        return favorites

    


def main():
    agenda = Agenda()

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "add":
            nome = args[1]
            listaFones = []
            for i in range(2, len(args)):
                numero = args[i]
                id, number = numero.split(":")
                telefone = Fone(id, number)
                listaFones.append(telefone)
            agenda.addContact(nome, listaFones) 
        elif args [0] == "show":
            print (agenda)
        elif args [0] == "rmFone":
            nome = args[1]
            indice = int(args[2])
            agenda.removeFone(nome, indice)
        elif args [0] == "rm":
            name = args[1]
            agenda.rmContact(name)
        elif args [0] == "search":
            pattern = args[1]
            agenda.search(pattern)
            for contato in agenda.search(pattern):
                print(contato)
        elif args [0] == "tfav":
            favoritado = args[1]
            agenda.getFavorited(favoritado)
        elif args [0] == "favs":
            for favoritos in agenda.favorites():
                print(favoritos)
        else:
            print("fail: comando invalido")

main()
from config import *

class Produto(db.Model):
    # atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    valor = db.Column(db.Float(5,2))
    quantidade = db.Column(db.Integer)

    # formato texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            "valor: " + str(self.valor) + ", quantidade" + str(self.quantidade)
    # formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "valor": str(self.valor),
            "quantidade": str(self.quantidade)
        }

# teste    
if __name__ == "__main__":
    # criar a tabela
    db.create_all()

    # teste da classe 
    p1 = Produto(nome = "Caneca de café", valor = 50.00, 
        quantidade = 15)

    p2 = Produto(nome = "Caneca de Cerveja", valor = 50.00, 
        quantidade = 10)       
    
    # persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    # exibir o produto em String
    print(p1)
    print(p2)

    # exibir o produto no formato de json
    print(p1.json())
    print(p2.json())

    # drop da tabela 
    db.drop_all()
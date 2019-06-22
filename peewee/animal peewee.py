import peewee, os 

db= peewee.SqliteDatabase("animalia.db")

class Animal(peewee.Model):
    nomedono=peewee.CharField()
    tipo_animal=peewee.CharField()
    raca=peewee.CharField()
    class Meta:
        database= db 
    def __str__(self):
        return self.tipo_animal + "," + self.raca + "," + self.nomedono


class Cliente(peewee.Model):
    email=peewee.CharField()
    senha=peewee.CharField()
    telefone=peewee.CharField()
    class Meta:
        database= db 
    def __str__(self):
        return self.email + "," + self.senha + "," + self.telefone


class Consulta(peewee.Model):
    data=peewee.CharField()
    animal=peewee.ForeignKeyField(Animal)
    cliente=peewee.ForeignKeyField(Cliente)
    horario=peewee.CharField()
    class Meta:
        database= db 
    def __str__(self):
        return self.data + "," + str(self.animal) + "," + str(self.cliente) + "," + self.horario

if __name__=="__main__":
    arq="animalia.db"
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Animal,Cliente,Consulta])
    except peewee.OperationalError as e :
        print("Não foi possível operar"+ str(e))

    print("TESTE ANIMAL")
    animal=Animal(nomedono="José", tipo_animal="canguru", raca="australiano")
    print(animal)

    animal.save() 




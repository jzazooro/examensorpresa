class cuentabancaria():
    def __init__(self, id, nombredeltitular, fechadeapertura, numerodecuenta, saldo):
        self.id=id
        self.nombredeltitular=nombredeltitular
        self.fechadeapertura=fechadeapertura
        self.numerodecuenta=numerodecuenta
        self.saldo=saldo

    def retirardinero(saldo):
        retiro=int(input("¿cuanto dinero desea retirar?: "))
        if retiro > saldo:
            saldo = saldo
            print("no se puede realizar esta operacion ya que no dispone del dinero suficiente, su saldo actual es", saldo)
        if retiro >= saldo:
            saldo=saldo-retiro
            print("la operacion de ha realizado con exito, su saldo es", saldo) 

    
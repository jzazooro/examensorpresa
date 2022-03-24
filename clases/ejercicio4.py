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
            print("no se puede realizar esta operacion ya que no dispone del dinero suficiente, su saldo actual es: ", saldo)
        if retiro >= saldo:
            saldo=saldo-retiro
            print("la operacion de ha realizado con exito, su saldo es", saldo) 
    def ingresardinero(saldo):
        ingreso=int(input("¿cuanto dinero desea ingresar?: "))
        if ingreso <= 0:
            saldo=saldo
            print("no se puede realizar esta operacion, su saldo es: ", saldo)
        if ingreso > 0:
            saldo=saldo+ingreso
            print("la operacion se ha realizado con exito, su saldo es: ", saldo)


    
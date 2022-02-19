class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def exibe_data(self):
        print("A data de hoje é {0} {1} {2}".format(self.dia, self.mes, self.ano))


#from datas import Data
#d = Data(16,2,2022)
#d.exibe_data()
#A data de hoje é 16 2 2022



import json
import sys



class ThereIsNoCar(Exception):
    pass

class Dealer():
    def __init__(self, dataFile):
        self.loadFile(dataFile)
    
    def loadFile(self, dataFile):
        with open("data.json", "r+") as file:
            jsonData = json.load(file)
            self.brands = jsonData["cars"]
            self.clients = jsonData["clients"]
        return

    def showAll(self):
        pass
       
    
    def sell(self, data):
        # print(self.brands)
        print(data)
        flag = False
        for i in self.brands:
            if i["brand"] == data[1]: # checking if there is this brand in inventory
                if i["number"] > 0: # checking if there is enough cars to make a deal
                    i["number"] -= 1 # -= cars -1 car after sell 
                    flag = True
                    print(f'Udalo się dokonać sprzedazy za kwote {i["priceToSell"]}')
                    self.clients.append({ #appending new client to my array of clients with data
                        "name":f'{data[0]}',
                        "car": f'{data[1]}',
                        "transaction": "sell",
                        "sum": f'{i["priceToSell"]}'
                    })
                    print(self.clients)
                    break
                else:
                    raise ThereIsNoCar # raising errors
            if(flag): # using 'flag' method to make is quicker
                break
        else:
            raise ThereIsNoCar
                
        
        # print(self.brands)
        # print(i["number"])
        # print(type(data[2]))
        # if self.brands[data[2]][0] > 0 and data[2] in self.brands:
        #     self.names[data[1]] = [data[2], data[0]]
        #     self.names[data[1]].insert(0, self.brands[data[2]][1])
        #     self.brands[data[2]][0] -= 1
        #     print(self.brands)
        #     print(self.names)
        
    # def rent(self, data):
    #     print(type(data[2]))
    #     if self.brands[data[2]][0] > 0 and data[2] in self.brands:
    #         self.names[data[1]] = [data[2], data[0]]
    #         self.brands[data[2]][0] -= 1
    #         print(self.brands)

    # def return1(self, data):
    #     pass
        

if __name__ == "__main__":
    # x = sys.argv[1]
    dealer = Dealer('data.json')
    # dealer.pokaz()
    while True:
        try:    
                # [operacja, imie, marka]
            data = input().split()
            if data[0] == 'sell':
                dealer.sell(data[1:])
            elif data[0] == 'rent':
                dealer.rent(data)
            elif data[0] == 'return':
                dealer.return1(data)
            else:
                    print('Sorry there is no transaction like yours')
        except ThereIsNoCar:
            print('Sorry, There is no car in inventory, try again. ')
            continue
        except KeyboardInterrupt:
            dealer.showAll()
        except EOFError:
            dealer.showAll()
   
        
            
        
    



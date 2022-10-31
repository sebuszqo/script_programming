from datetime import date, timedelta
import json
import sys


class ThereIsNoCar(Exception):
    pass

class ThereIsNoCarToReturn(Exception):
    pass

class Dealer():
    numOfTransactions = 0
    sumOfTransactions = 0 
    def __init__(self, dataFile):
        self.loadFile(dataFile)
    
    # method to load cars and clients from textFile
    def loadFile(self, dataFile):
        with open(dataFile, "r+") as file:
            jsonData = json.load(file)
            self.brands = jsonData["cars"]
            self.clients = jsonData["clients"]
        return

    def showAll(self):
        pass
       
    
    def sell(self, data):
        # print(self.brands)
        # print(data)
        flag = False
        for i in self.brands:
            if i["brand"] == data[1]: # checking if there is this brand in inventory
                if i["number"] > 0: # checking if there is enough cars to make a deal
                    i["number"] -= 1 # -= cars -1 car after sell 
                    flag = True
                    print(f'Udalo się dokonać sprzedazy za kwote {i["priceToSell"]}')
                    self.clients.append({ #appending new client to my array of clients with data
                        "name":f'{data[0]}',
                        "brand": f'{data[1]}',
                        "transaction": "sell",
                        "startDate": date.today(), 
                        "endDate": "",
                        "days": 0,
                        "sum": f'{i["priceToSell"]}'
                    })
                    # using class attributes to store sum of every client
                    if hasattr(Dealer,f'{data[0]}'):
                        x = getattr(Dealer,f'{data[0]}')
                        setattr(Dealer,f'{data[0]}', x + i["priceToSell"])
                    else:
                        setattr(Dealer,f'{data[0]}', 0)
                    # changing some informations about Dealer stats 
                    Dealer.numOfTransactions += 1
                    Dealer.sumOfTransactions += i["priceToSell"]
                    print(Dealer.numOfTransactions)
                    print(Dealer.sumOfTransactions)
                    return True # to break function cuz it did what it should
                else:
                    raise ThereIsNoCar # raising errors
            if(flag): # using 'flag' method to make is quicker
                break
        else:
            raise ThereIsNoCarToReturn
    
        # print(self.brands)
        # print(i["number"])
        # print(type(data[2]))
        # if self.brands[data[2]][0] > 0 and data[2] in self.brands:
        #     self.names[data[1]] = [data[2], data[0]]
        #     self.names[data[1]].insert(0, self.brands[data[2]][1])
        #     self.brands[data[2]][0] -= 1
        #     print(self.brands)
        #     print(self.names)
        
    def rent(self, data):
        #[<name>, <brand>, days]
        flag = False
        for i in self.brands:
            if i["brand"] == data[1]: # checking if there is this brand in inventory
                if i["number"] > 0: # checking if there is enough cars to make a deal
                    i["number"] -= 1 # -= cars -1 car after sell 
                    flag = True
                    print(f'Udalo się dokonać wypozyczenia na kwote {i["priceToRent"]*data[2]}')
                    self.clients.append({ #appending new client to my array of clients with data
                        "name":f'{data[0]}',
                        "brand": f'{data[1]}',
                        "transaction": "rent",
                        "startDate": date.today(), 
                        "endDate": date.today() + timedelta(days=data[2]),
                        "days": data[2],
                        "sum": f'{i["priceToRent"]}'
                    })
                    # changing some informations about Dealer stats 
                    Dealer.numOfTransactions += 1
                    Dealer.sumOfTransactions += (i["priceToRent"]*data[2])
                    print(Dealer.numOfTransactions)
                    print(Dealer.sumOfTransactions)
                    # print(self.clients)
                    return True # to break function cuz it did what it should
                else:
                    raise ThereIsNoCar # raising errors
            if(flag): # using 'flag' method to make is quicker
                break
        else:
            raise ThereIsNoCar


        # print(type(data[2]))
        # if self.brands[data[2]][0] > 0 and data[2] in self.brands:
        #     self.names[data[1]] = [data[2], data[0]]
        #     self.brands[data[2]][0] -= 1
        #     print(self.brands)

    def returnTheCar(self, data):
        # [<name>, <brand>,]
        # print(len(self.clients))
        for i in range(len(self.clients) - 1):
            print(i)
            print(self.clients[i])
            if self.clients[i]["name"] == data[0] and self.clients[i]["transaction"] == "rent" and self.clients[i]["brand"] == data[1]:
                for car in self.brands:
                    if car["brand"] == data[1]:
                        car["number"] += 1
                #deleting the client who returned his car
                del self.clients[i]
                # changing some informations about Dealer stats 
                Dealer.numOfTransactions += 1
                print(Dealer.numOfTransactions)
                print('zakonczono proces zwortu')
        else:
            raise ThereIsNoCarToReturn 


def errors(error):
    match error:
        case 'FileNotFoundError':
            return 'You gave me wrong filename sorry, try again'
        case 'ThereIsNoCar':
            return 'Sorry, There is no car in inventory, try again. '
        case 'ThereIsNoCarToReturn':
            return 'Sorry you can\'t return this car try again. '
        case 'ValueError':
            return 'You`ve made a mistake try again. '


if __name__ == "__main__":
    try:
        if len(sys.argv) <= 1:
            raise FileNotFoundError
        x = sys.argv[1]
        # FileNotFoundError is raised by a 'system' when it can't find a file
        dealer = Dealer(sys.argv[1])
    except FileNotFoundError:
            print(errors('FileNotFoundError'))
            exit()
            
    # dealer.pokaz()
    while True:
        try:    
            # [operacja, imie, marka]
            data = input().split()
            data[1].capitalize()
            if data[0] == 'sell':
                dealer.sell(data[1:])
            elif data[0] == 'rent':
                data.append(int(input("Tell me how long you want to rent? ")))
                dealer.rent(data[1:])
            elif data[0] == 'return':
                dealer.returnTheCar(data[1:])
            else:
                print('Sorry there is no transaction like yours')
        except ThereIsNoCar:
            print(errors('ThereIsNoCar'))
            continue
        except ThereIsNoCarToReturn:
            print(errors('ThereIsNoCarToReturn'))
            # print('Sorry you can\'t return this car try again. ')
            continue
        except ValueError:
            print(errors('ValueError'))
            # print('You`ve made a mistake try again. ')
            continue
        except KeyboardInterrupt:
            print('koniecś')
            break
        #      dealer.showAll()
        except EOFError:
            print('nara')
            break
        
        #     print("koniecś")
        #     break
        #     dealer.showAll()
   
        
            
        
    



from tabulate import tabulate

class Transaction():
    def __init__(self):
        self.items = dict()
    
    def add_item(self, name, qty, price):
        self.items[name] = [qty, price]

        print('\nADD ITEM\'S')
        header = ['Nama Barang', 'Jumlah Barang', 'Harga Barang']
        table = [[name, str(self.items[name][0]), str(self.items[name][1])]]
        print(tabulate(table, header, tablefmt="github"))

    def update_item_name(self, name, name_update):
        print('\nUPDATE ITEM NAME')
        if name in self.items.keys():
            self.items[name_update] = self.items.pop(name)            
            print(f'{name} updated to {name_update}')
        else:
            raise Exception('Nama item tidak ada')  

    def update_item_qty(self, name, qty_update):
        print('\nUPDATE ITEM QUANTITY')
        if name in self.items.keys():
            self.items[name][0] = qty_update
            print(f'{name} quantity is updated to {qty_update}')
        else:
            raise Exception('Nama item tidak ada')  

    def update_item_price(self, name, price_update):
        print('\nUPDATE ITEM PRICE')
        if name in self.items.keys():
            self.items[name][1] = price_update
            print(f'{name} price is updated to {price_update}')
        else:
            raise Exception('Nama item tidak ada')

    def delete_item(self, name):
        print(f'\nDELETING {name}')
        if name in self.items.keys():
            del self.items[name]
        else:
            raise Exception('Nama item tidak ada')

    def reset_transaction(self):
        print('\nDELETE ALL ITEM\'S')
        self.items.clear()

    def check_order(self):
        print('\nCHECKING ORDER\'S')
        header = ['Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Total Harga']
        table = []
        for key, value in self.items.items():

            table.append([key, value[0], value[1], value[0]*value[1]])
        print(tabulate(table, header, tablefmt="github"))

    def total_price(self):
        print('\nCOUNTING TOTAL PRICE\'S')
        price = 0
        for key, value in self.items.items():
            price +=value[0]*value[1]
            
        print(f'Total Harga : {price}')
        if price >  500000:
            price = price-(price*0.1)
            print(f'Selamat, anda mendapatkan diskon sebesar 10%')
            print(f'Sehinggal Total harga : {price}')
        elif price > 300000:
            price = price-(price*0.08)
            print(f'Selamat, anda mendapatkan diskon sebesar 8%')
            print(f'Sehinggal Total harga : {price}')
        elif price > 200000:
            price = price-(price*0.05)
            print(f'Selamat, anda mendapatkan diskon sebesar 5%')
            print(f'Sehinggal Total harga : {price}')
        else:
            pass

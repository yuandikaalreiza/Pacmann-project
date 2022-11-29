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
        pass

    def reset_transaction(self):
        pass

    def check_order(self):
        pass

    def total_price(self):
        pass

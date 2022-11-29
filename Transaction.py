from tabulate import tabulate

class Transaction():
    def __init__(self):
        """
        construct necesary attributes for Transaction class
        """
        self.items = dict()
    
    def add_item(self, name, qty, price):
        """
        adding item to dictionary

        Args:
            name (str): string for name of the item
            qty (int): decimal quantity of the item
            price (int): decimal price of the item

        Raises:
            Exception: ValueError if not input int in qty and price
        """
        try:
            qty = int(qty)
            price = int(price)
        except:
            raise Exception('Masukkan angka  pada kuantiti dan harga')
        else:
            self.items[name] = [qty, price]
            header = ['Nama Barang', 'Jumlah Barang', 'Harga Barang']
            table = [[name, str(self.items[name][0]), str(self.items[name][1])]]
            
            print('\nADD ITEM\'S')
            print(tabulate(table, header, tablefmt="github"))

    def update_item_name(self, name, name_update):
        """
        Updating item name to dictionary

        Args:
            name (str): name of the item to be changed
            name_update (st): new item name

        Raises:
            Exception: if name is not in the items
        """
        print('\nUPDATE ITEM NAME')
        if name in self.items.keys():
            self.items[name_update] = self.items.pop(name)            
            print(f'{name} updated to {name_update}')
        else:
            raise Exception('Nama item tidak ada')  

    def update_item_qty(self, name, qty_update):
        """Updating item quantity  to dictionary

        Args:
            name (str): name of the item to be changged
            qty_update (int): new iten quantity

        Raises:
            Exception: if name is not in the items or qty is not integer
        """
        print('\nUPDATE ITEM QUANTITY')
        if name in self.items.keys():
            try:
                qty_update = int(qty_update)
            except:
                raise Exception('Masukkan angka pada kuantiti')
            else:
                self.items[name][0] = qty_update
                print(f'{name} quantity is updated to {qty_update}')
        else:
            raise Exception('Nama item tidak ada')  

    def update_item_price(self, name, price_update):
        """
        Updating item price to dictionary

        Args:
            name (str): name of the item to be changed
            price_update (int): new item price

        Raises:
            Exception: name is not in the items
            Exception: qty is not integer
        """
        print('\nUPDATE ITEM PRICE')
        if name in self.items.keys():
            try:
                price_update = int(price_update)
            except:
                raise Exception('Masukkan angka pada harga')
            else:
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


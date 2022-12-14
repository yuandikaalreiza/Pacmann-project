from tabulate import tabulate

class Transaction():
    def __init__(self):
        """
        construct necesary attributes for Transaction class
        """
        self.items = dict()
        self.catalog = {
            'Ayam Goreng': 20000,
            'Pasta Gigi': 15000,
            'Terpal' : 50000,
            'Mi Instan' : 3000,
            'Mainan Mobil': 200000
        }
    
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
            # make sure data type match
            qty = int(qty)
            price = int(price)

        except:
            raise Exception('Masukkan angka  pada kuantiti dan harga')

        else:
            # add item to items
            self.items[name] = [qty, price]

            # create header and table to be print
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

        # check if name is in items and update item name
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

        # check if name is in items and make sure data type match
        if name in self.items.keys():
            try:
                qty_update = int(qty_update)

            except:
                raise Exception('Masukkan angka pada kuantiti')

            else:
                # update item qty
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
        
        # check if name is in items and make sure data type match
        if name in self.items.keys():
            try:
                price_update = int(price_update)

            except:
                raise Exception('Masukkan angka pada harga')

            else:
                # update item price
                self.items[name][1] = price_update
                print(f'{name} price is updated to {price_update}')

        else:
            raise Exception('Nama item tidak ada')

    def delete_item(self, name):
        """
        deleting 1 item from dictionary

        Args:
            name (str): name of the item to be deleted

        Raises:
            Exception: name is not in the items
        """
        print(f'\nDELETING {name}')

        # check if name is in items
        if name in self.items.keys():
            # delete item
            del self.items[name]
            
        else:
            raise Exception('Nama item tidak ada')

    def reset_transaction(self):
        """
        deleting all the items in dictionary
        """
        print('\nDELETE ALL ITEM\'S')
        
        # clear all items
        self.items.clear()

    def check_order(self):
        print('\nCHECKING ORDER\'S')

        # create header and table
        header = ['Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Total Harga']
        table = []

        # iterate over items
        for key, value in self.items.items():

            # check if item name is not in catalog, if no continue the loop
            if key not in self.catalog.keys():
                print(f'Terdapat kesalahan pada input, {key} tidak tersedia pada katalog')
                continue

            # check if item price is same in catalog, if no continue the loop
            if value[1] != self.catalog[key]:
                print(f'Terdapat kesalahan pada input, {key} seharusnya memiliki harga {value[1]}')
                continue

            # create table for correct items
            table.append([key, value[0], value[1], value[0]*value[1]])
        print(tabulate(table, header, tablefmt="github"))

    def total_price(self):
        print('\nCOUNTING TOTAL PRICE\'S')
        price = 0

        # count total price
        for key, value in self.items.items():
            price +=value[0]*value[1]
            
        print(f'Total Harga : {price}')

        # if price > 500k, get 10% discount
        if price >  500000:
            price = price-(price*0.1)
            print(f'Selamat, anda mendapatkan diskon sebesar 10%')
            print(f'Sehinggal Total harga : {price}')

        # if price > 300k, get 8% discount
        elif price > 300000:
            price = price-(price*0.08)
            print(f'Selamat, anda mendapatkan diskon sebesar 8%')
            print(f'Sehinggal Total harga : {price}')

        # if price > 200k, get 5% discount
        elif price > 200000:
            price = price-(price*0.05)
            print(f'Selamat, anda mendapatkan diskon sebesar 5%')
            print(f'Sehinggal Total harga : {price}')
        else:
            print(f'Total harga : {price}')


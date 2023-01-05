class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan

    def getNamaPelanggan(self):
        return self._namaPelanggan

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def dequeue(self): #menghapus data paling depan, dan memajukan urutan data yang dibelakangnya
        data = self._data[0]
        self._data.remove(data)
        self._data.append(None)
        print("### Pelanggan {} selesai membayar ###" .format(NodePelanggan.getNamaPelanggan(data)))
        print()

    def enqueue(self, namaPelanggan): #menambah data ke list
        baru = NodePelanggan(namaPelanggan)
        if self.__len__() >= self.DEFAULT_CAPACITY:
            self.resizeBy3()

        for i, d in enumerate(self._data):
            if d == None:
                self._data[i] = baru
                self._size += 1
                return
    
    def resizeBy3(self): #menambah ukuran queue sebesar 3
        self.DEFAULT_CAPACITY += 3
        for i in range(3):
            self._data.append(None)
        print("=== Berhasil Diresize 3 ===")

    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")
        print()

# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()
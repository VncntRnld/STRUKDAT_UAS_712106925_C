class Node:
    def __init__(self,data,priority):
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None
    
class PQSTugas:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool:
        return self._size == 0

    def printAll(self):
        if self.isEmpty():
            print("Tidak ada tugas.")
            print()

        else:
            helper = self._head

            print("=== Prioritas : Tugas ===")
            while helper != None:
                print("[{}] : {}" .format(helper._priority, helper._data))
                helper = helper._next
            print()

    def _addHead(self, newNode):
        self._head._prev = newNode
        newNode._next = self._head
        self._head = newNode

    def _addTail(self, newNode):
        self._tail._next = newNode
        newNode._prev = self._tail
        self._tail = newNode

    def _addMiddle(self, newNode):
        helper = self._head
        while helper != None:
            if helper._priority <= newNode._priority:
                helper = helper._next
            else:
                temp = helper._prev
                helper._prev = newNode
                newNode._next = helper
                newNode._prev = temp
                temp._next = newNode
                break


    def add(self, data, priority):
        baru = Node(data, priority)
        if self.isEmpty():
            self._head = baru
            self._tail = baru
        else:
            if self._head._priority > priority:
                self._addHead(baru)
            elif self._tail._priority < priority:
                self._addTail(baru)
            else:
                self._addMiddle(baru)
        self._size += 1

    def remove(self):
        if self.isEmpty():
            print("Sudah tidak ada tugas yang bisa dihapus")
        else:
            temp = self._head
            print("Menghapus [{}] : {}" .format(temp._priority, temp._data))
            print()
            self._head = temp._next
            del temp

    def removePriority(self, priority):

        if self.isEmpty():
            print("Sudah tidak ada tugas yang bisa dihapus")
            print()
            return

        temp = None
        helper = self._head

        while helper != None:
            if helper._priority == priority:
                temp = helper
                break
            helper = helper._next

        if temp == None:
            print("Tidak terdapat tugas dengan prioritas {}" .format(priority))
            print()
        else:
            if self._size == 1:
                self._head = None
                self._tail = None
            else:
                if temp == self._head:
                    self._head = temp._next
                elif temp == self._tail:
                    self._tail = temp._prev
                else:
                    temp._next._prev = temp._prev
                    temp._prev._next = temp._next
            print("Menghapus [{}] : {}" .format(temp._priority, temp._data))
            print()
            del temp
                

if __name__ == "__main__":
 tugasKu = PQSTugas()
 tugasKu.add("StrukDat",1)
 tugasKu.add("Menyapu", 5)
 tugasKu.add("Cuci Baju", 4)
 tugasKu.add("Beli Alat Tulis", 3)
 tugasKu.add("Cuci Sepatu", 4)
 tugasKu.printAll()

 tugasKu.remove()
 tugasKu.printAll()

 tugasKu.removePriority(2)
 tugasKu.removePriority(4)
 tugasKu.printAll()
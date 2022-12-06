class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linklist:
    def __init__(self):
        self.head = None

    def add_at_begining(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def insert_by_indx(self, data, index):
        if index == 0:
            self.add_at_begining(data)
        else:
            itr = self.head
            count = 0
            while itr:
                count += 1
                if count == index:
                    itr.next = Node(data, itr.next)
                    break

                itr = itr.next

    def remove_by_indx(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            itr = self.head
            count = 0
            while itr:
                count += 1
                if count == index:
                    itr.next = itr.next.next
                    break

                itr = itr.next            

    def print(self):
        itr = self.head
        if not itr:
            print('It is empty')
        allof = ""
        while itr:
            allof += str(itr.data) + "-->"
            itr = itr.next
        print(allof)


if __name__=='__main__':
    link = Linklist()
    # link.add_at_begining(15)
    # link.add_at_begining(55)
    # link.print()
    link.add_at_end(39)
    link.add_at_end(48)
    link.add_at_end(51)
    link.print()
    link.insert_by_indx(55, 2)
    link.print()
    link.remove_by_indx(2)
    link.print()







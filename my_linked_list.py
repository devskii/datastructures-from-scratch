class MyLinkedList:
    def __init__(self, d):
        self.data = d
        self.next = None

    def append(self, data):
        if self.next == None:
            self.next = MyLinkedList(data)
        else:
            self.next.append(data)

    def remove(self, d):
        if self.data == d:
            return self.next
        elif self.next.data == d:
            self.next = self.next.next
            return self
        else:
            self.next = self.next.remove(d)
            return self

    def to_string(self):
        if self.next == None:
            return f"{self.data}"
        else:
            return f"{self.data} " + self.next.to_string()

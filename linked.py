class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.tail = Node(None, None) # create a null like in C
        self.head = Node(None, self.tail)
        self.length = 0
    def append(self, data):
        if self.length == 0:     # do not use self.head.next==self.tail, this is very interesting
            self.head.data = data
        else:
            current_position = self.head
            while (current_position.next != self.tail):
                current_position = current_position.next
            new_node = Node(data, self.tail)
            current_position.next = new_node
        self.length += 1

    def insert(self, data, i):
        if i == 0:
            new_node = Node(data, self.head)
            self.head = new_node
            self.length +=1
        else:
            before_i = self.head
            for index in range(self.length):
            
                if index == i-1:
                    new_node = Node(data, before_i.next)
                    before_i.next = new_node
                    self.length += 1
                before_i = before_i.next 

    def delete(self, i):
        if i > self.length-1 or i < 0:
            return
        if i == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            before_i = self.head
            for index in range(self.length):
                if index == i-1:
                    i = before_i.next
                    deleted_data = i.data
                    after_i = i.next
                    before_i.next = after_i
                    self.length -= 1
                    return deleted_data 
                before_i = before_i.next 
        
    def print(self):
        current_position = self.head
        for _ in range(self.length):
            if (current_position.next != self.tail):
                print(str(current_position.data)+" -> ", end="")
            else:
                print(current_position.data)
            current_position = current_position.next
    def index(self, data):
        current_position = self.head
        for index in range(self.length):
            if (current_position.data == data):
                return index 
            current_position = current_position.next
        return -1
    def swap(self, i, j):
        if i > self.length-1 or j > self.length-1 or i<0 or j<0:
            return
        current_position = self.head
        for index in range(self.length):
            if (i == index):
                i_data= current_position.data
            if (j == index):
                j_data= current_position.data
            current_position = current_position.next
        self.insert(i_data, j)
        self.delete(j+1)
        self.insert(j_data, i)
        self.delete(i+1)
    def fetch_data(self, i):
        if i > self.length-1:
            return
        current_position = self.head
        for index in range(self.length):
            if index == i:
                return current_position.data
            current_position = current_position.next
    def isort(self):
        for i in range(1, self.length):
            j = i-1
            while j>=0 and (self.fetch_data(j) > self.fetch_data(j+1)):
                self.swap(j, j+1)
                j = j-1
    



if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    L.isort()
    L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10
   
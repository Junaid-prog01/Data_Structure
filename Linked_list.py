class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next
        return None


if __name__ == "__main__":
    linked_list = Linked_list()
    linked_list.insert_beginning(30)
    linked_list.insert_beginning(20)
    linked_list.insert_beginning(10)
    linked_list.display()
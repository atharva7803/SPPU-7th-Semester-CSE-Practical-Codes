import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  
        self.symbol = symbol  
        self.left = left 
        self.right = right  
        self.huff = ""  

    def __lt__(self, other):
        return self.freq < other.freq

def printNodes(node, val=""):
    newval = val + node.huff  
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newval}")


def createHuffmanTree(chars, freqs):
    nodes = []
    
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freqs[i], chars[i]))
    
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = "0"  
        right.huff = "1"  
        newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)
    
    return nodes[0]


def main():
    while True:
        print("\nMenu:")
        print("1. Enter characters and their frequencies")
        print("2. Display Huffman Codes")
        print("3. Exit")
        
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            chars = input("Enter characters: ").split()
            freqs = list(map(int, input("Enter frequencies for the characters: ").split()))
            
            if len(chars) != len(freqs):
                print("Error: The number of characters and frequencies must match!")
                continue
            
            huffman_tree = createHuffmanTree(chars, freqs)
            print("\nHuffman Tree Created Successfully!")
        
        elif choice == 2:
            try:
                print("\nHuffman Codes:")
                printNodes(huffman_tree)
            except NameError:
                print("Error: Huffman Tree not created. Please choose option 1 first.")
        
        elif choice == 3:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()



####

# import heapq 
 
# class node: 
#     def __init__(self, freq, symbol, left=None, right=None): 
#         self.freq = freq 
#         self.symbol = symbol 
#         self.left = left 
#         self.right = right 
#         self.huff = ""
        
#     def __lt__(self, other): 
#         return self.freq < other.freq 
     
     
# def printNodes(node, val=""): 
#     newval = val + node.huff 
#     if node.left: 
#         printNodes(node.left, newval) 
#     if node.right: 
#         printNodes(node.right, newval) 
#     else: 
#         print(f"{node.symbol} -> {newval}") 
        
        
# chars = ["a", "b", "c", "d", "e", "f"]
# freqs = [5, 9, 12, 13, 16, 45]
# nodes = []

# for i in range(len(chars)): 
#     heapq.heappush(nodes, node(freqs[i], chars[i]))
    
# while len(nodes) > 1:
#     left = heapq.heappop(nodes)
#     right = heapq.heappop(nodes)
#     left.huff = "0"
#     right.huff = "1"
#     newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
#     heapq.heappush(nodes, newnode)
    
# printNodes(nodes[0])



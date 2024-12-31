class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        
        
def fractionalKnapsack(capacity, items):
    items.sort(key = lambda x: x.profit/x.weight, reverse = True)
    
    totalVal = 0.0
    
    for item in items:
        if capacity >= item.weight:
            totalVal += item.profit
            capacity -= item.weight
        else:
            totalVal += item.profit * (capacity / item.weight)
            break
        
    return totalVal


if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    
    items = []
    
    for i in range(n):
        profit = int(input(f"Enter profit of items {i+1}: "))
        weight = int(input(f"Enter weight of items {i+1}: "))
        items.append(Item(profit, weight))
        
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    maxVal = fractionalKnapsack(capacity, items)
    print(f"Maximum value in knapsack: {maxVal: } ")
    
# current inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# display inventory  
def display(inventory):
    numStored = 0
    for k , v in inventory.items():
        print("%s %s"  %(v,k))
        numStored = numStored + v


    print("Total: %s "%(numStored))

# add list to stuff dictornary 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for k, v in inventory.items():
        for i in range(len(addedItems)):       
            cur_item = addedItems[i]
            if cur_item == k:
               v = v + 1
        
            for key in inventory.keys():
                a = {cur_item: 1}
                print(a)
                




        print(k,v)

addToInventory(stuff,dragonLoot)

# display(stuff)

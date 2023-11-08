class HashLinear:

    def __init__(self, M):
        self.M = M
        self.T = [None] * M

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.M

    def insert(self, data):
        if None not in self.T and 'TombStone' not in self.T:
            return
        for i in range(self.M):
                if self.T[i] == data:
                    return 
                
        try:
            slot = self.hash(data)
            
        except Exception:
            print("Invalid Input")
            return
        
        if self.T[slot] == None or self.T[slot] == 'TombStone':
            self.T[slot] = data
        else:
            round = 1
            while (self.T[slot] != None and self.T[slot] != 'TombStone'): 
                slot = slot + 1
                if slot > self.M-1 and round < 3:
                    slot = 0
                    round += 1
                elif round >3:
                    return
                
            
            self.T[slot] = data

    def delete(self, data):
        for i in range(self.M):
            if self.T[i] == data:
                self.T[i] = 'TombStone'
    
    def print(self):
        output = ""
        for i in range(self.M):
            if self.T[i] == None or self.T[i] == 'TombStone':
                continue
            else:
                output += self.T[i]+" "
        output.rstrip(" ")
        print(output)

if __name__ == "__main__":
    table = HashLinear(10)
table.insert("buttermilk")
table.insert("shim")
table.insert("resolvend")
table.insert("cheiromegaly")
table.insert("premillennialise")
table.insert("finebent")
table.print()     #buttermilk shim cheiromegaly finebent resolvend premillennialise
table.delete("buttermilk")
table.delete("cores")
table.delete("cheiromegaly")
table.delete("iodations")
table.print()    #shim finebent resolvend premillennialise
table.insert("iodations")
table.insert("tirrlie")
table.insert("comous") #iodations discursiveness comous shim tirrlie finebent flabbergasts rename resolvend premillennialise 
table.insert("discursiveness")
table.insert("flabbergasts")
table.insert("rename")
table.insert("softhead")
table.print()

            
             
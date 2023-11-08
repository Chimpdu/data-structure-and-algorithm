class HashBucket:

    def __init__(self, M, B):
        self.M = M
        self.B = B
        self.T = [None]*M
        self.BA = []

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.B

    def insert(self, data):
        for i in range(self.M):
            if self.T[i] == data:
                return 
        for i in range(len(self.BA)):
            if self.BA[i] == data:
                return    
        try:
            bucket_size = int(self.M / self.B)
            bucket_index = self.hash(data)
            
        except Exception:
            print("Invalid Input")
            return
        
        slot = bucket_index * bucket_size
        if self.T[slot] == None:
            self.T[slot] = data
        else:
            while (self.T[slot] != None): 
                slot = slot + 1
                if slot >= (bucket_index+1)*bucket_size:
                    self.BA.append(data)
                    return
            self.T[slot] = data
                

    def delete(self, data):
        for i in range(self.M):
            if self.T[i] == data:
                self.T[i] = None
                return
        for i in range(len(self.BA)):
            if self.BA[i] == data:
                self.BA.pop(i)
                return
    
    def print(self):
        output = ""
        for i in range(self.M):
            if self.T[i] == None:
                continue
            else:
                output += self.T[i]+" "
        for i in range(len(self.BA)):
            output += self.BA[i]+" "
        output.rstrip(" ")
        print(output)

if __name__ == "__main__":
    
    table = HashBucket(10, 5)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    table.print()
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    table.print()

            
             
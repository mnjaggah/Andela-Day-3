class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a   #length of list
        self.b = b    #step

    #generate a ist of numbers
        for num in range(self.a):
            list.append(self, self.b)
            self.b += b
            
            self.length = self.a
        
    def search(self, item):
                count = 0
                first = 0
                last = (self.length - 1)
                found = False
                index = self.index(item)
                
                while first < last and not found:
                    midpoint = (first + last)//2
                    mid_value = self[midpoint]
                    if mid_value == item:
                        found = True
                        count += 1
                        break
                    elif item <= mid_value:
                            last = midpoint - 1
                            count += 1
                    else:
                        first = midpoint + 1
                        count += 1
                                   
                return {'count': count, 'index': index}

class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

        

    def findMedian(self) -> float:
        n = len(self.arr)
        self.arr.sort()
        if(n%2 == 0):
            num1 = math.floor(n/2) -1
            
            num2 = math.floor(n/2) 
            return (self.arr[num1]+self.arr[num2])/2

        else:
            return self.arr[math.floor(n/2)]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
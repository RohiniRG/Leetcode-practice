class ProductOfNumbers:
    data_stream = [1]
    
    def _init_(self):
        self.data_stream = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.data_stream = [1]
        else:
            self.data_stream.append(num * self.data_stream[-1])

    def getProduct(self, k: int) -> int:
        if k >= len(self.data_stream):
            return 0
        else:
            return (self.data_stream[-1]//self.data_stream[-(k+1)])
          

class Solution:
    def colName (self, n):
        # your code here
        col_name = ''
        while n > 0:
            rem = n % 26
            if rem == 0:
                col_name += 'Z'
                n = (n//26)-1
            else:
                col_name += chr(rem+64)
                n = n // 26
                
        return col_name[::-1]
                

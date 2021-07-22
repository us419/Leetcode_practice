class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_str = str(n)
        if self.isLargest(n_str):
            return -1
        
        sub_len = 1
        while sub_len <= len(n_str):
            idx = sub_len * -1
            sub_word = n_str[idx:]
            if self.isLargest(sub_word):
                sub_len += 1
                continue
            answer = int(n_str[:idx] + self.change(sub_word))
            if answer > 2147483647:
                return -1
            return int(n_str[:idx] + self.change(sub_word))
            
        
    def isLargest(self, n_str: str) -> bool:
        for i in range(len(n_str)-1):
            if n_str[i] < n_str[i+1]:
                return False
        return True
    
    
    def change(self, n:str) -> str:
        min_val = 99
        temp = []
        head = n[0]
        for idx in range(len(n)) :
            if ord(n[idx]) > ord(head) and ord(n[idx]) - ord(head) <= min_val:
                temp.append(idx)
                
        idx = temp[-1]
        new_str = n[1:idx] + n[0] + n[idx+1:]
        
        return n[idx] + ''.join(sorted(new_str))
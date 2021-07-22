class Solution:
    def maxProduct(self, words: List[str]) -> int:
        new_list = []
        for word in words:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - ord('a')] += 1
            new_list.append(temp)
            
        max_val = 0
        for idx1 in range(len(new_list)):
            for idx2 in range(idx1, len(new_list)):
                if not self.isShare(new_list[idx1], new_list[idx2]):
                    if sum(new_list[idx1]) * sum(new_list[idx2]) > max_val:
                        max_val = sum(new_list[idx1]) * sum(new_list[idx2])
        return max_val
                
    def isShare(self, list1, list2):
        for i in range(26):
            if list1[i] * list2[i] > 0:
                return True
        return False
                
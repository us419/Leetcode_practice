class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        r_map = {word[::-1]:idx for idx, word in enumerate(words)}
        
        answer = []
        for i, word in enumerate(words):
            r_word = word[::-1]
            if word in r_map:
                if r_map[word] != i:                   
                    answer.append((i,r_map[word]))
                    
            for j in range(1,len(word)+1):
                if word[:-j] in r_map and self.isPalindrome(word[-j:]):
                    answer.append((i, r_map[word[:-j]]))
                if word[j:] in r_map and self.isPalindrome(word[:j]):
                    answer.append((r_map[word[j:]], i))
                    
        return answer
    
    def isPalindrome(self, word):
        if word == word[::-1]:
            return True
        return False
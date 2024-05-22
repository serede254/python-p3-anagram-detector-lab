class Anagram:
    def __init__(self,word):
        self.word=word
    
    def match(self,word_list):
        sorted_word=sorted(self.word)
        matching=[]
        
        for word in word_list:
            if sorted_word==sorted(word):
                matching.append(word)
            
        return matching
    
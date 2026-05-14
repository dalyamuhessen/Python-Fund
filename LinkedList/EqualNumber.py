# # Given a string s, return true if s is a good string, or false otherwise.
#  A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).


class Solution(object): 
    def areOccurrencesEqual(self, s):     
           """     
                 :type s: str      
                 :rtype: bool 
            """     
           freq = {}   
           for c in s:   
               freq[c] = freq.get(c, 0) + 1  
           return len(set(freq.values())) == 1
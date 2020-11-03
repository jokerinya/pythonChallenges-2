class Solution:
    # Write your code here
    _stackpushed = ""
    _stackenqueued = ""
    _index = 0
    def pushCharacter(self, el):
        self._stackpushed += el
    def enqueueCharacter(self, el):
        self._stackenqueued = el + self._stackenqueued
    def popCharacter(self):
        poped_char = self._stackpushed[self._index]
        self._index += 1
        return poped_char
    def dequeueCharacter(self):
        dequeu_char = self._stackenqueued[self._index - 1]
        return dequeu_char

# read the string s
s=input().strip()
# s="racecar"
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
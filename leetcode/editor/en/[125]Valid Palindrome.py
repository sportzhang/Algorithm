# Given a string s, determine if it is a palindrome, considering only alphanumer
# ic characters and ignoring cases. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 105 
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 
<<<<<<< HEAD
#  👍 1834 👎 3686
=======
#  👍 1829 👎 3674
>>>>>>> 50dc4cf3ab95f8c900bba70d59b8d54f8e72b5db


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
<<<<<<< HEAD
        
# leetcode submit region end(Prohibit modification and deletion)
=======
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    s.isPalindrome("A man, a plan, a canal: Panama")
>>>>>>> 50dc4cf3ab95f8c900bba70d59b8d54f8e72b5db

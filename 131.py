class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(string, left, right):
            if left >= right:
                return True
            elif string[left] != string[right]:
                return False
            else:
                return is_palindrome(string, left + 1, right - 1)
            
        def generate_substring(substring_list, partition, string):
            if len(string) <= 0:
                return substring_list
            
            for i in range(len(string)):
                partition.push(string[:i])
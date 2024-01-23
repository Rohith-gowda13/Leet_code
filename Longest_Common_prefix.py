# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix= ''

        first_string=strs[0]

        for i in range(len(first_string)):
            char=first_string[i]
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return prefix


            prefix += char

        return prefix

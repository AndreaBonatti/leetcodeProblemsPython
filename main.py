# Problem 5.
# Longest Palindromic Substring.

class Solution:
    def isPalindorme(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        length = 1
        longestPalindrome = s[0]
        allSubstrings = []
        start = 0
        while start < len(s) - 1:
            for end in range(start + 1, len(s) + 1):
                if s[start:end] not in allSubstrings:
                    allSubstrings.append(s[start:end])
                    if self.isPalindorme(s[start:end]) and length < len(s[start:end]):
                        length = len(s[start:end])
                        longestPalindrome = s[start:end]
            start += 1
        return longestPalindrome


if __name__ == '__main__':
    # string = "bb"
    # print("Input: " + string + " Output: " + Solution().longestPalindrome(string))
    # string = "babad"
    # print("Input: " + string + " Output: " + Solution().longestPalindrome(string))
    # string = "cbbd"
    # print("Input: " + string + " Output: " + Solution().longestPalindrome(string))
    string = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print("Input: " + string + " Output: " + Solution().longestPalindrome(string))

# Problem 5.
# Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # To find the longest palindrome from a starting point
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        result = ""
        for i in range(len(s)):
            # The starting point is a single letter => odd string
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
            # The starting point is a couple of letter => even string
            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2
        return result


if __name__ == '__main__':
    # string = "bb"
    # print("Input: " + string + " Output: " + Solution().longestPalindrome(string))
    # string = "babad"
    # print("Input: " + string + " Output: " + Solution().longestPalindrome(string))
    # string = "cbbd"
    # print("Input: " + string + " Output: " + Solution().longestPalindrome(string))
    string = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print("Input: " + string + " Output: " + Solution().longestPalindrome(string))

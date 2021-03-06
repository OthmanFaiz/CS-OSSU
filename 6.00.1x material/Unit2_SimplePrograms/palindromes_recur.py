def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        answer = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                answer = answer + c
        return answer

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

print(isPalindrome("assfa"))
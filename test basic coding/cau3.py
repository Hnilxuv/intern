from difflib import SequenceMatcher


class MyString:
    def __init__(self, my_string):
        self.my_string = my_string

    def get_sum_ASCII(self):
        print(sum(map(ord, self.my_string)))

    def get_sum_ASCII_upper(self):
        li = [char for char in self.my_string if char.isupper()]
        result = []
        for i in range(len(li)):
            result.append(ord(li[i]))
            result = list(set(result))
        print(sum(result))

    def check_freq(self, n):
        x = self.my_string
        freq = {}
        for c in set(x):
            freq[c] = x.count(c)
        print(freq)

        for i, j in freq.items():
            if j >= n:
                print(i + ":", j)


s1 = 'adadadadaaaaaddd'
s2 = 'adadssdddaaaaaddd'
ms = MyString(s1)
ms2 = MyString(s2)
ms.get_sum_ASCII()
ms.get_sum_ASCII_upper()
ms.check_freq(2)

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp] == string2[j+lcs_temp]):
                match += string2[j+lcs_temp]
                lcs_temp += 1
            if len(match) > len(answer):
                answer = match
    return answer


print(longestSubstringFinder(s1, s2))




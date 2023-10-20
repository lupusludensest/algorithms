# Pankay Kumar from AutoNation dt 14 oct 2023, 6:00am cdt, Saturday
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

s = "cbaebabacd"
p = "abc"
def findAnagrams(s, p):
    pLen = len(p)
    sLen = len(s)

    if sLen < pLen:
        return []

    pChars = [0] * 26
    sChars = [0] * 26

    for i in range(pLen):
        pChars[ord(p[i]) - ord('a')] += 1
        sChars[ord(s[i]) - ord('a')] += 1

    anagramIndices = []
    if pChars == sChars:
        anagramIndices.append(0)

    for i in range(pLen, sLen):
        sChars[ord(s[i]) - ord('a')] += 1
        sChars[ord(s[i - pLen]) - ord('a')] -= 1
        if pChars == sChars:
            anagramIndices.append(i - pLen + 1)

    return anagramIndices

print(findAnagrams(s, p))

# write get request from https://reqres.in/

import requests

def test_sendsafely_api_get_text_security_1():
    r=requests.get('https://reqres.in/api/users?page=2')

    if r.status_code == 200:
        print(f"\nPASS_STATUS = {r.status_code}")
    else:
        print(f'\nFAIL_STATUS ="{r.status_code}"')

    whole_txt = r.json()
    wrd = [7, 8, 9, 10, 11, 12]
    for i in wrd:
        if i in whole_txt:
            print('Ok')


    print(f'\nurl of the response: {r.url}\n{wrd} is in {whole_txt}')  # url of the response
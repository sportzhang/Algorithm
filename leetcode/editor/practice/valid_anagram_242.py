# -*- coding: utf-8 -*-
import collections

"""
Given two strings s and t , write a function to determine if t is an anagram of s.
You may assume the string contains only lowercase alphabets.
"""


def isAnagram1(s, t):
    return sorted(s) == sorted(t)


def isAnagram2(s, t):
    dict1, dict2 = {}, {}
    for i in s:
        dict1[i] = dict1.get(i, 0) + 1
    for j in t:
        dict2[i] = dict2.get(j, 0) + 1
    return dict1 == dict2


def groupAnagram(strs):
    """
    将字符串拆分排序，作为key，互为anagram的字符串保存在同一个key下
    :param strs:
    :return:
    """
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.keys()


if __name__ == '__main__':
    a = 'hello'
    b = 'ehllo'
    print(isAnagram2(a, b))
    g_strs = [a, b, 'hjao', 'oahj', 'wekjv', 'hi', 'ih']
    print(groupAnagram(g_strs))


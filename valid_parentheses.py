# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

solution:
Use stack to judge the characters,
(1)if the current char is the back one, then judge is it the corresponding one that last added in the stack
(2)if thr current char is the front one,add it to the stack
"""


class Solution(object):
    def is_valid_parentheses(self, s):
        pairs, stack = {'[': ']', '{': '}', '(': ')'}, []
        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) == 0 or pairs[stack.pop()] != char:
                return False
        return len(stack) == 0


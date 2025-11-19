""" Chapter6: Dynamic Programming
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:
len = [0 , ..., 0] pred = [none , ..., none]
for i = 1 , ..., m:
    for j = 1, ...,i -1:
        if len(i) < len(j) + 1 and pred(i) := j
        len(i) := max(len(i) , len(j) + 1)

return max(len)

Example 2:
fir(n):
    array F = [0, 1, 1, ....1](length n+1)
    for j = 2, ..., n:
        F_j = F_j-1 + F_j-2
    return F_n
0->2     2->4    
0 -> 1 -> 2 -> 3 -> 4
    1->3      3-> 

Edit distance
input two strings S = s1...sm, T = t1...tn
prefix s_1...i = s_1, ..., s_i
prefix t_1...j = t_1, ..., t_j

how easy is it to get from s to t by:
    1. deleting a character
    2. inserting a character
    3. changing a character
edit distance = # steps
"""
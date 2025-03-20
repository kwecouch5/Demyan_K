def lengthOfLongestSubstring(s):
    fin_res = 0
    dict_of_ind = {}
    i=0
    while i!=len(s):
        if s[i] in dict_of_ind:
            if fin_res <= len(dict_of_ind):
                fin_res = len(dict_of_ind)
            i = dict_of_ind[s[i]] + 1
            dict_of_ind = {}
            dict_of_ind[s[i]] = i
        else:
            dict_of_ind[s[i]] = i
            print(dict_of_ind)
        i+=1
    if fin_res >= len(dict_of_ind):
        return fin_res
    else:
        return len(dict_of_ind)
print(lengthOfLongestSubstring(""))
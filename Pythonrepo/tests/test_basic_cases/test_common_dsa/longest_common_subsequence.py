"""
str1 = "abxyzmnopqr"
str2 = "mnopqrxyzfg"

find the length of the longest common contiguous substring between two input strings
"""


def Check_act_sub(str1ind, str2ind, str1, str2 , lenr, maxlen):

    actual_start = str1ind
    for i in range(str1ind, len(str1)):
        if  str1[i] == str2[str2ind] and i != len(str1) :
            lenr += 1
            if str2ind < len(str2) and i != len(str1) -1:
                str2ind += 1
                maxlen = max(maxlen, lenr)
                continue
            else:
                maxlen = max(maxlen, lenr)  # Update maxlen if lenr is greater
                return maxlen

        else:
            maxlen = max(maxlen, lenr)  # Update maxlen if lenr is greater
            return maxlen


def longest_subsequence(string1, string2):
    """
    Function to find the length of the longest common contiguous substring
    """
    maxlen = 0
    prevmax = 0

    for  i in range(0,len(string1)):

        for j in range(0, len(string2)):

            if string1[i] == string2[j] :


                lenr = 0

                # print("startindex: {}, endindex: {}, match : {}".format(idx_str1_start,  idx_str2_start, match))

                maxlenret  =  Check_act_sub(i, j , string1, string2, lenr, maxlen)

                if prevmax < maxlenret:
                    prevmax = maxlenret
                else:
                    print("already greater")

                print("max len returned is: ",maxlenret)


    return prevmax


str1 = "abxyzmnopqr"
str2 = "mnopqrxyzfg"

max = longest_subsequence(str1, str2)
print("\nlenght of logest substring is :", max)








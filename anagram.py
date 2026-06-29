word1 = input("Enetr the first word")
word2 = input("Enter the second word")
len1 = len(word1)
len2 = len(word2)
if len1 == len2:
    flag = True
    for i in word1:
        if word1.count(i) != word2.count(i):
            flag = False
            break
    if flag:
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")

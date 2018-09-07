def count_substring(input, sub):
    count = 0
    input_len = len(input)
    sub_len = len(sub)
    
    for ch in range(0, input_len):
        if input[ch] == sub[0]:
            if input[ch:ch + sub_len] == sub:
                count += 1
    return count

a = input("Input string : ")
b = input("Input sub string : ")
print(count_substring(a,b))

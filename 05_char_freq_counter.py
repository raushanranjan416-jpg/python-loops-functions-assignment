def char_freq_counter(text:str):
    occurance = {}
    for i in range(len(text)):
        char = text[i]
        if char in occurance:
            occurance[char] +=1
        else:
            occurance[char] = 1

    print(occurance)

char_freq_counter("banana")
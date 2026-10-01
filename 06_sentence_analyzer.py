def sentence_analyzer(sentence:str):

    vowel_count = 0 
    consonants_count = 0
    digits_count = 0
    spaces_count = 0
    special_count = 0
    for ch in sentence:
        if ch.isdigit():
            digits_count +=1
        elif ch.isspace():
            spaces_count +=1
        elif ch.isalpha():
            ch = ch.lower()
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                vowel_count +=1
            else:
                consonants_count += 1
        else:
            special_count +=1

    print(f"Vowel count: {vowel_count}, Consonants count: {consonants_count}, Digit count: {digits_count}, Space count: {spaces_count}, Special count : {special_count}")

        
sentence_analyzer("Hello, World. Welcome to Earth.")

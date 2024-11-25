#print("hello world")
dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    count = 0
    chars = 0
    #print(file_contents)
    words = file_contents.split()
    for word in words:
        count += 1
        chars += len(word)
        low_word = word.lower()
        for w in low_word:
        

            if (w == 'a' or w == 'b' or w == 'c' or w == 'd' or w == 'e' or 
                w == 'f' or w == 'g' or w == 'h' or w == 'i' or w == 'j' or 
                w == 'k' or w == 'l' or w == 'm' or w == 'n' or w == 'o' or 
                w == 'p' or w == 'q' or w == 'r' or w == 's' or w == 't' or 
                w == 'u' or w == 'v' or w == 'w' or w == 'x' or w == 'y' or 
                w == 'z'):

                dict[w] +=1 
    
    print("\n\n--- Startar rapport på books/frankenstein.txt ---")
    print(count, "ord finns i boken.\n")
    #print("")
    for letter in dict:
        print ("bokstaven", letter, "finns med", dict[letter], "gånger")

    print("--- Slut på rapporten ---")
    #print("ord:", count, "karaktärer:", chars)
    #print(dict)
#main()
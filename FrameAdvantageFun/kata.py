def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i < length(spl)):
        if (spl(i).length > longest): 
            longest = spl[i].length
    return longest


find_longest("The quick white fox jumped around the massive dog")


import sys
word = (sys.argv[1])


def is_palindrome(word):
    letters = list(word)
    is_palindrome = True
    i = 0

    while len(letters) > 0 and is_palindrome:
        if letters[0] != letters[(len(letters) - 1)]:
            is_palindrome = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop((len(letters) - 1))

    if is_palindrome == True:
      print " is a palindrome."
    else:
      print " is no palindrome."
    return is_palindrome


is_palindrome(word)

# sys.stdout

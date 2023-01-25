def is_palindrome_iterative(word):
    palindromo = reversed(word[: len(word)])

    if len(word) == 0:
        return False
    elif word == "".join(palindromo):
        return True

    return False

def is_palindrome(phrase):
    if not isinstance(phrase, str):
        raise TypeError("phrase must be a string")

    cleaned = ""
    for ch in phrase.lower():
        if ch.isalnum():
            cleaned = cleaned + ch
    return cleaned == cleaned[::-1]

tests = [
    "A man, a plan, a canal: Panama",
    "Racecar",
    "No 'x' in 'Nixon'",
    "hello",
    "12321",
    "12345",
    "",
    "!!! ???",
    "a"
]
for t in tests:
    print(repr(t), "->", is_palindrome(t))

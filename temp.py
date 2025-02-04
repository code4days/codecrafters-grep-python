def match(pattern, text):
    """If pattern starts with '^', match from beginning;
    otherwise, try to match at every position in text."""
    if pattern.startswith("^"):
        return match_here(pattern[1:], text)
    # Try matching at each position
    for i in range(len(text) + 1):
        if match_here(pattern, text[i:]):
            return True
    return False


def match_here(pattern, text):
    """Recursively match pattern against text."""
    # If pattern is empty, we have matched everything
    if pattern == "":
        return True

    # Handle a quantifier (if the second char is '*' or '+')
    if len(pattern) >= 2 and pattern[1] in "*+":
        op = pattern[1]
        if op == "*":
            return match_star(pattern[0], pattern[2:], text)
        else:  # op == '+'
            return match_plus(pattern[0], pattern[2:], text)

    # If pattern is '$', it only matches the end of text.
    if pattern == "$":
        return text == ""

    # Match a single literal or dot ('.') and continue recursively.
    if text and (pattern[0] == "." or pattern[0] == text[0]):
        return match_here(pattern[1:], text[1:])

    return False


def match_star(c, pattern, text):
    """Match zero or more occurrences of character c followed by pattern."""
    i = 0
    # Try all possible prefixes of text that are c
    while True:
        if match_here(pattern, text[i:]):
            return True
        if i >= len(text) or (text[i] != c and c != "."):
            return False
        i += 1


def match_plus(c, pattern, text):
    print(f"c: {c}, pattern {pattern}, text {text}")
    """Match one or more occurrences of character c followed by pattern.

    First, we require that the first character of text matches c.
    Then, we behave similarly to match_star.
    """
    # Must have at least one matching character.
    if not text or (text[0] != c and c != "."):
        return False

    i = 1  # We already matched one instance.
    while True:
        if match_here(pattern, text[i:]):
            return True
        if i >= len(text) or (text[i] != c and c != "."):
            break
        i += 1
    return False


# Example usage:
if __name__ == "__main__":
    tests = [
        # pattern, text, expected_result
        # ("a+", "aaa", True),
        # ("a+", "b", False),
        # ("^a+", "aaab", True),
        ("a+b$", "caaaab", True),
        # ("a+b$", "caaaac", False),
    ]
    for pat, txt, expected in tests:
        result = match(pat, txt)
        print(f"Pattern: {pat!r}, Text: {txt!r} -> {result} (expected {expected})")

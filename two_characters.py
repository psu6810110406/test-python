def twoCharacters(s):
    unique_chars = list(set(s))
    max_len = 0
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1, c2 = unique_chars[i], unique_chars[j]
            filtered = [c for c in s if c == c1 or c == c2]
            if all(filtered[k] != filtered[k+1] for k in range(len(filtered)-1)):
                if len(filtered) > 1:
                    max_len = max(max_len, len(filtered))
    return max_len
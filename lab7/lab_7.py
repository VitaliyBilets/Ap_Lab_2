def rabin_karp(haystack: str, needle: str) -> list:
    if not needle or not haystack or len(needle) > len(haystack):
        return []


    base = 256
    mod = 10**9 + 7

    n = len(haystack)
    m = len(needle)


    needle_hash = 0
    window_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * base) % mod


    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []


    for i in range(n - m + 1):
        if needle_hash == window_hash:

            if haystack[i:i + m] == needle:
                result.append(i)


        if i < n - m:
            window_hash = (window_hash - ord(haystack[i]) * h) * base + ord(haystack[i + m])
            window_hash %= mod

    return result
haystack = "abracadabra"
needle = "abra"
print(rabin_karp(haystack, needle))

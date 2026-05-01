"""
BPE Implementation - Byte Pair Encoding
- Compressing data for much shorter lengths of contexts and shorter vocabulary table

Process:
Step-1: Iterate and check for most occuring byte pairs in a sequence
Step-2: Replace the most occured byte pairs with a new token
Step-3: Recursively repeat the process until no byte pairs are left to be replaced

Working:
Step-1: Example_text = "aaabdaaabac"
        We have length '11' sequence with a vocabulary length '4'
        vocabulary = {a, b, c, d}

Step-2: Most occuring byte pair = 'aa'
        Replace it with 'Z' (a new token)

        we get = "ZabdZabac"
        replacement table: 'Z' = 'aa'

Step-3: Most occuring byte pair = 'ab'
        Replace it with 'Y' (a new token)

        we get = "ZYdZYac"
        replacement table:  'Y' = 'ab'
                            'Z' = 'aa'

Step-4: Now recursively applying BPE
        Most occuring byte pair = 'ZY'
        Replace it with 'X' (a new token)

        we get = "XdXac"
        replacement table:  'X' = 'ZY'
                            'Y' = 'ab'
                            'Z' = 'aa'

Step-5: Compressed_text = "XdXac"
        Now we have length '%' sequence with a vocabulary length '3'
        vocabulary = {X, Y, Z}

"""

text: str = "aaabdaaabac"
tokens: list = list(text.encode("utf-8"))
print("text = ", list(text))
print("lenth: ", len(text))
print("encoded tokens = ", tokens)
print("length", len(tokens))

def get_stats(ids: list) -> dict:
    count: dict = {}
    for pair in zip(ids, ids[1:]):
        count[pair] = count.get(pair, 0) + 1
    return count

stats: dict = get_stats(tokens)
print(stats)
top_pair = max(stats, key = stats.get)
print(top_pair)


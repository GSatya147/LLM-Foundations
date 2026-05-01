"""
BPE Implementation - Byte Pair Encoding
- Compressing data for much shorter lengths of contexts and shorter vocabulary table

process:
Step-1: Iterate and check for most occuring byte pairs in a sequence
Step-2: Replace the most occured byte pairs with a new token
Step-3: Recursicely repeat the process until no byte pairs are left to be replaced

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


"""
BPE Implementation - Byte Pair Encoding
- Compressing data for much shorter lengths of contexts and shorter vocabulary table

step-1: 
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


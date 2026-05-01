"""
BPE Implementation - Byte Pair Encoding
- Compressing data for much shorter lengths of contexts and shorter vocabulary table

Process:
Step-1: Iterate and check for most occuring byte pairs in a sequence
Step-2: Replace the most occured byte pairs with a new token
Step-3: Recursively repeat the process

Note: The number of times we repeat the process is the hyperparameter we tune
we set desired vocabulary size, and hyperparameter is the difference between final vocabulary size to present vocabulary size
number_of_iters = desired_vocab_size - present_vocab_size

Here desired vocabulary size is carefully selected, considering cost & context management and natural language capabilities as much as possible.

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
        Now we have length '5' sequence with a vocabulary length '3'
        vocabulary = {X, Y, Z, a, c, d} (meaning only frequently occuring ones are eligible for compression, maintaining base chars is also seen here)

Note: For decompressing just apply the replacing methods in reverse
"""

# GPT-4 has 100k
VOCAB_SIZE = 276

# iters, nuo of merges to be done to reach desired state
NUM_MERGES = VOCAB_SIZE - 256 # 256 is the initial vocab size

text: str = "aaabdaaabac" # try to give a big text
encodes: bytes = text.encode("utf-8") # raw bytes
tokens: list = list(map(int, encodes)) # convert to a list of ints in range 0..255 for conveninence

print("text = ", list(text))
print("length: ", len(text))
print("encoded tokens = ", tokens)
print("length", len(tokens))

def get_stats(ids: list) -> dict:
    count: dict = {}
    for pair in zip(ids, ids[1:]):
        count[pair] = count.get(pair, 0) + 1
    return count

stats: dict = get_stats(tokens)
print(stats)
 
# List of tuples of (count, byte pairs) descending order, most occured at index 0
print(sorted(((v, k) for k, v in stats.items()), reverse = True))

top_pair: tuple = max(stats, key = stats.get)
print(top_pair)

def merge(ids: list, pair: tuple, idx: str) -> list:
    new_ids: list = []
    i: int = 0
    while i < len(ids):

        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            new_ids.append(idx)
        else:
            new_ids.append(ids[i])
        
        i+=1
    return new_ids


print(merge([5, 6, 6, 7, 9, 1], (6, 7), 99))
compressed_tokens: list = merge(tokens, top_pair, ord('Z'))
print(compressed_tokens)
print(len(compressed_tokens))

#---------------------------------------------------------------------------------------------------------------------
# iterate, hyperparamater tuning to decide optimal number of times performing merge is  good on a text
# the more times we merge the larger the vocabulary gonna be, but the shorter the data will be i.e context data
#---------------------------------------------------------------------------------------------------------------------
ids: list = list(tokens) # copy, to avoid losing original list

# stores key: pair replaced (int, int) and value: new token int
merges: dict = {} # (int, int) -> int

for i in range(NUM_MERGES):
    stats: dict = get_stats(ids)
    pair: tuple = max(stats, key = stats.get)
    idx: int = 256 + i
    print(f"Merging {pair} into {idx}")
    ids: list = merge(ids, pair, idx)
    merges[pair] = idx

print(f"tokens size before compression: {len(tokens)}\ntokens after compression: {len(ids)}\ncompression ratio: {len(tokens) / len(ids):.2f}x")


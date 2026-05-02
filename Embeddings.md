## Converting words to vectors
- word2vec is a method to convert words to vectors in the filed of NLP.
- Well it has contributed even in non NLP fields like recommndation engines of enterprises like airbnb, alibaba etc..

* Similarity between two vectors can be given by `cosine_similarity(v1, v2)`, vectors pointing in same direction have higher similarity.

* Two important understandings:
- Representing people & things as vectors of numbers (high dimensions) - word embeddings
- Calculating how similar two vectors are high-positive being the most similar 

* We use cosine similarity cus we only need direction for semantics, learning magnitude doesn't help eg: word occuring frequently in data has large magnitude doesn't mean it's simlar to everything
* The smaller the angle the closer they are pointing hence cosine close to 1, and 0 if perpendicular and if in opposite direction it's negative.

#### Open questions

1. Why do similar words cluster together in embedding space?
During training, the model learns to predict a word from its surrounding context (or vice versa). Words that appear in similar contexts - "doctor" and "physician" both appear near "hospital", "patient", "diagnosis", end up getting pushed toward similar positions in vector space because they produced similar prediction signals during training. The embedding is essentially a compressed summary of "what contexts does this word appear in?" Similar contexts → similar vectors → nearby positions in the space. It's not that the model was explicitly told these words are similar, it fell out of the training objective naturally.

2. What does cosine similarity actually measure geometrically?
It measures the angle between two vectors, ignoring their magnitude. Two vectors pointing in roughly the same direction have a small angle between them → cosine similarity close to 1. Two vectors pointing in opposite directions → cosine similarity close to -1. Perpendicular vectors → 0.
The reason you use angle rather than raw distance (Euclidean) is that magnitude in embedding space doesn't carry meaningful semantic information, a word that appeared more frequently in training might have a larger magnitude vector, but that doesn't make it more "similar" to anything. Cosine similarity strips that out and asks purely: are these two vectors pointing the same way? That's the right question for semantic similarity.

3. Why is a word's embedding different depending on context, the move from Word2Vec to contextual embeddings?
Word2Vec gives every word exactly one vector regardless of context. "Bank" gets one fixed vector whether you're talking about a river bank or a financial bank. That's the fundamental limitation: it's a lookup table, not a computation.
Transformers fix this by computing the embedding dynamically at inference time. Every token's representation gets updated by the attention mechanism, it looks at all the other tokens in the sequence and incorporates information from them. So "bank" in "he sat by the river bank" ends up with a completely different vector than "bank" in "he deposited money at the bank" because the surrounding tokens pull it in different directions during the attention computation. The embedding isn't looked up, it's computed fresh for each input. That's the core shift, and it's why contextual embeddings are so much more powerful for downstream tasks.
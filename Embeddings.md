## Converting words to vectors
- word2vec is a method to convert words to vectors in the filed of NLP.
- Well it has contributed even in non NLP fields like recommndation engines of enterprises like airbnb, alibaba etc..

* Similarity between two vectors can be given by `cosine_similarity(v1, v2)`, vectors pointing in same direction have higher similarity.

* Two important understandings:
- Representing people & things as vectors of numbers (high dimensions) - word embeddings
- Calculating how similar two vectors are high-positive being the most similar 

* We use cosine similarity cus we only need direction for semantics, learning magnitude doesn't help eg: word occuring frequently in data has large magnitude doesn't mean it's simlar to everything
* The smaller the angle the closer they are pointing hence cosine close to 1, and 0 if perpendicular and if in opposite direction it's negative.


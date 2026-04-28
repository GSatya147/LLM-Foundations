# LLMs - What They Are and How They Work

- LLMs are specialised machine learning models which are trained on huge sets of data to predict next word (token) without explicitly coded.

#### Working Mechanism:
- LLMs rely on underlying algorithm/model called 'Transformers'.
- Transformers are essentially nueral nets with different underneath layers:
1. Tokenisation, which deals with handling input processing
2. Embeddings, where words are arranged based on thier semantic meaning in a high dimensional space
3. Attention, an underlying algorithm/mechanism where tokens communicate with each other establishing connections, relationships and useful contexts
4. MLP/feed forward, a nueral network for individual token to fact check the knowledge or derive needy info from existing knowledge base
5. Multiple repetitions of steps 3 and 4 to establish sense/sematics in different directions, all the directions are combined in the end to produce a final change in embedding.
6. Final probability distribution determines which word/token is being selected.
7. These 1-6 steps are repeatedly performed in parallel for every word which gets predicted using specialised computers called GPUs.


## Intuition

- Basically think of it like - LLMs are nothing but sophisticated mathematical function which rely on transformers architecture to predict next word in a sequence, here the sequence can be any natural language.
- LLMs undergo long sessions of training using huge chunks of data hence the name 'large', trying to imitate our natural language as much as possible hence the name 'language', with out being explicitly coded hence named a ml 'model'. we call this a base model which is trained to predict next word.
- The second stage before an LLM can be commercially used is called 'Fine-tuning' stage, this is where the power of predicting next token/word is actually gets useful for users. Fine tuning is a process of changing the way an LLM acts through labeling instructions, LLM gets fed with labelled instructions from either a very large group of experts or orgnaizations like scale.ai etc..
- For instance say an LLM to act as an virtual assistant gets fed with chunks of expert Q&A writings, to format its output both explicit system prompts and labeled data.
- Since a model which has been trained on experts data gets only as good as the best human out there, and to best this a type of self improvement is needed which is achieved through RLHF (Reinforcement Learning Human Feedback). But LLMs specifically doesn't have a explicit reward analogy here hence human intervention is needed.
- After getting the fine-tuned model, RLHF is used to repeated improve the performance of the commercial model.

## Analogy


## How it connects to AI Engineering

## Key capabilities (Karpathy's list)

## Security and failure modes

## Open questions
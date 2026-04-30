# LLMs - What They Are and How They Work

- LLMs are specialised machine learning models which are trained on huge sets of data to predict next word (token) without explicitly coded.

#### Working Mechanism:
- LLMs rely on underlying algorithm/model called 'Transformers'.
- Transformers are essentially nueral nets with different underneath layers:
1. Tokenisation, which deals with handling input processing
2. Embeddings, where words are arranged based on thier semantic meaning in a high dimensional space
3. Attention, an underlying algorithm/mechanism where tokens communicate with each other establishing connections, relationships and useful contexts.
4. MLP/feed forward, a nueral network for individual token to fact check the knowledge or derive needy info from existing knowledge base (Linear & Non-linear(ReLU) actiavtions are used and output is combined with the input)
5. Multiple repetitions of steps 3 and 4 to establish sense/sematics in different directions, all the directions are combined in the end to produce a final change in embedding.
6. Final probability distribution (Softmax) determines which word/token is will be selected.
7. These 1-6 steps are repeatedly performed in parallel for every word which gets predicted using specialised computers called GPUs.


**Math:**
Step-1: Pre tuned weight/parameters matrices like 
We = embedding matrix (Vocab)
Wq = query matrix (cluster of queries)
Wk = keys matrix (cluster of responses)
Wv = value matrix (cluster of words to direct the responses semantically)
Wn = MLP matrix (knowledge base for NN activation)

Step-2 (Tokenisation): Sentences to tokens 

Step-3: Tokens to vector embeddings

Step-4: Attention Mechanism
A(Q, K, V) = Softmax(Transpose(K).Q/(Sqrt(dk)))
Q = Query vectors
K = Key vectors
V = Value vectors
Transpose(K).Q = Is nothing but the context grid, hence O(n^2)
dk = temperature constant introduced

- Techniques like masking are used, if applicable

Step-5: MLP/feed forward layer (Linear -> Non-linear(ReLU, GeLU) -> Linear -> Sum(MLP output + input))

Step-6: Repetitions of steps 4 & 5 (multi heads)

Step-7: Softmax probability distribution on last most vector embedding 
Softmax = (e^x/T)/Sum(e^n/T) from n = 0 to n-1
T is temperature constant

## Intuition

- Basically think of it like - LLMs are nothing but sophisticated mathematical function which rely on transformers architecture to predict next word in a sequence, here the sequence can be any natural language.
- LLMs undergo long sessions of training using huge chunks of data hence the name 'large', trying to imitate our natural language as much as possible hence the name 'language', with out being explicitly coded hence named a ml 'model'. we call this a base model which is trained to predict next word.
- The second stage before an LLM can be commercially used is called 'Fine-tuning' stage, this is where the power of predicting next token/word is actually gets useful for users. Fine tuning is a process of changing the way an LLM acts through labeling instructions, LLM gets fed with labelled instructions from either a very large group of experts or orgnaizations like scale.ai etc..
- For instance say an LLM to act as an virtual assistant gets fed with chunks of expert Q&A writings, to format its output both explicit system prompts and labeled data.
- Since a model which has been trained on experts data gets only as good as the best human out there, and to best this a type of self improvement is needed which is achieved through RLHF (Reinforcement Learning Human Feedback). But LLMs specifically doesn't have a explicit reward analogy here hence human intervention is needed.
- After getting the fine-tuned model, RLHF is used repeatedly improve the performance of the commercial model.

## How it connects to AI Engineering
- AI engineer is a person who leverages the use and capabilities of an LLM for either commercial or goal purposes. It's like a person who is master at excel calculations for a finance comapny which uses excel for calculations. 
- Cus of complex available capablities of an LLM, using it efficiently is an essential task, it can be anything like creating agents/multi-agents to do a particular action after an LLM interaction, or retrieving particular context which may not be available in LLM's context, creating a formatted output response to satisfy user needs.
- This is what more than 90% of companies are leaning towards, due to lack of proprietary model maintenance environment, they rely on these frontier models.
- Since these frontier models can give natural responses to almost anything hence tuning that response is ultimately a need.

## Key capabilities
 - Can generate texts
 - Can process audio/video/img inputs (Multi-Modal capabilities)
 - Can use pre existing tools like browser, calculator, terminal, interpreters/compilers through ethernet
 - Can talk with other LLMs
 - Can manage memory/disk related tasks
## Security and failure modes
There are various concerning security areas to handle failure/unexpected LLM behaviour
 - Prompt injection
 - Jailbreak
 - Data poisioning 
## Open questions
1. Is it really necessary to create such powerful digital weapon using all those investment, resources etc?
A. We will know about this when the capabilities > investment, in the present market it's already leaning towards above mentioned constraint
2. How computationally expensive is high-level vector embeddings space
3. What is the optimal dimension for embeddings, when does it show diminishing results
4. Can we implement any pruning methods without actually loosing much on areas like embedding matrix, MLP layer etc..
5. What is the optimal area of loss to parameters/weights size 
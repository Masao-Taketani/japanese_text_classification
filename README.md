# Text Classification with Various DNN Methods
While trying various DNN text classifier methods for a **Japanese corpus**, [**livedoor corpus**](https://www.rondhuit.com/download.html#ldcc),  I aim to gain some knowledge and experice of DNN for NLP.
<br>
## Tokenizer
Two major tokenizers below are experimented.<br>
[1][**MeCab**](https://taku910.github.io/mecab/) + [**mecab-ipadic-neologd**](https://github.com/neologd/mecab-ipadic-neologd)<br>
Since the program is implemented in [Python](https://github.com/python), [**mecab-python3**](https://github.com/SamuraiT/mecab-python3) is also required to execute the program.<br>
[2][**SentencePiece**](https://github.com/google/sentencepiece)<br>
SentencePiece is trained on the [**Japanese Wikipedia Data dumps**](https://dumps.wikimedia.org/jawiki/latest/).<br>
To train this, I referred to the webpage titled ["Wikipediaから日本語コーパスを利用してSentencePieceでトークナイズ(分かち書き)"](https://applingo.tokyo/article/1252).
<br>
## Word Embedding
- As for case [1] above, **pretrained fastText embedding(Japanese)** is used, which can be found here [URL]https://drive.google.com/open?id=0ByFQ96A4DgSPUm9wVWRLdm5qbmc.<br>
- As for case [2] above, a word embedding matrix is trained while training each end-to-end DNN model.<br>
## Results

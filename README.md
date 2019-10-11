# Text Classification with Various DNN Methods
While trying various DNN text classifier methods for a **Japanese corpus**, [**livedoor corpus**](https://www.rondhuit.com/download.html#ldcc),  I aim to gain some knowledge and experice of DNN for NLP.
<br>
## Tokenizer
Two major tokenizers below are experimented.<br>
[1][**MeCab**](https://taku910.github.io/mecab/) + [**mecab-ipadicNEologd**](https://github.com/neologd/mecab-ipadic-neologd)<br>
Since the program is implemented in [Python](https://github.com/python), [**mecab-python3**](https://github.com/SamuraiT/mecab-python3) is also required to execute the program.<br>
[2][**SentencePiece**](https://github.com/google/sentencepiece)<br>
SentencePiece is trained on the [**Japanese Wikipedia Data dumps**](https://dumps.wikimedia.org/jawiki/latest/).<br>
To train this, I referred to the webpage titled ["Wikipediaから日本語コーパスを利用してSentencePieceでトークナイズ(分かち書き)"](https://applingo.tokyo/article/1252).
<br>
## Word Embedding
- As for case [1] above, **pretrained fastText embedding(Japanese)** is used, which can be found here [URL]https://drive.google.com/open?id=0ByFQ96A4DgSPUm9wVWRLdm5qbmc.<br>
- As for case [2] above, a word embedding matrix is trained while training each end-to-end DNN model.<br>
## Japanese BERT
I used [**bert-japanese**](https://github.com/yoheikikuta/bert-japanese) implemented by **"yoheikikuta"**.
## Results
**[1]MeCab + ipadicNEologd + fastText**
- MLP(Multi-layer Perceptron)
```
                precision    recall  f1-score   support           

dokujo-tsushin      0.721     0.886     0.795       175
  it-life-hack      0.789     0.825     0.806       154
 kaden-channel      0.856     0.856     0.856       167
livedoor-homme      0.820     0.439     0.571       114
   movie-enter      0.848     0.931     0.888       174
        peachy      0.801     0.701     0.748       184
          smax      0.930     0.930     0.930       186
  sports-watch      0.980     0.890     0.932       163
    topic-news      0.832     0.975     0.897       157

     micro avg      0.839     0.839     0.839      1474
     macro avg      0.842     0.826     0.825      1474
  weighted avg      0.843     0.839     0.834      1474
```
- CNN
```
                  precision    recall  f1-score   support

dokujo-tsushin      0.935     0.909     0.922       175
  it-life-hack      0.906     1.000     0.951       154
 kaden-channel      1.000     0.970     0.985       167
livedoor-homme      0.968     0.798     0.875       114
   movie-enter      0.939     0.977     0.958       174
        peachy      0.900     0.929     0.914       184
          smax      0.984     0.978     0.981       186
  sports-watch      0.994     1.000     0.997       163
    topic-news      0.981     0.987     0.984       157

     micro avg      0.955     0.955     0.955      1474
     macro avg      0.956     0.950     0.952      1474
  weighted avg      0.956     0.955     0.954      1474
```
- BiLSTM
```
                precision    recall  f1-score   support

dokujo-tsushin      0.850     0.874     0.862       175
  it-life-hack      0.851     0.929     0.888       154
 kaden-channel      0.957     0.928     0.942       167
livedoor-homme      0.786     0.675     0.726       114
   movie-enter      0.860     0.989     0.920       174
        peachy      0.886     0.761     0.819       184
          smax      0.957     0.957     0.957       186
  sports-watch      0.969     0.957     0.963       163
    topic-news      0.950     0.975     0.962       157

     micro avg      0.900     0.900     0.900      1474
     macro avg      0.896     0.894     0.893      1474
  weighted avg      0.900     0.900     0.899      1474
```
**[2]SentencePiece**
- MLP
```
                precision    recall  f1-score   support

dokujo-tsushin      0.862     0.926     0.893       175
  it-life-hack      0.911     0.929     0.920       154
 kaden-channel      0.931     0.970     0.950       167
livedoor-homme      0.886     0.684     0.772       114
   movie-enter      0.945     0.983     0.963       174
        peachy      0.893     0.864     0.878       184
          smax      0.974     0.995     0.984       186
  sports-watch      0.974     0.914     0.943       163
    topic-news      0.909     0.955     0.932       157

     micro avg      0.922     0.922     0.922      1474
     macro avg      0.921     0.913     0.915      1474
  weighted avg      0.922     0.922     0.920      1474
```
- CNN
```
                precision    recall  f1-score   support

dokujo-tsushin      0.965     0.937     0.951       175
  it-life-hack      0.962     0.994     0.978       154
 kaden-channel      1.000     0.982     0.991       167
livedoor-homme      0.903     0.816     0.857       114
   movie-enter      0.956     0.994     0.975       174
        peachy      0.937     0.962     0.949       184
          smax      0.989     1.000     0.995       186
  sports-watch      0.975     0.975     0.975       163
    topic-news      0.981     0.981     0.981       157

     micro avg      0.965     0.965     0.965      1474
     macro avg      0.963     0.960     0.961      1474
  weighted avg      0.965     0.965     0.965      1474
```
- BiLSTM
```
                precision    recall  f1-score   support

dokujo-tsushin      0.927     0.943     0.935       175
  it-life-hack      0.936     0.955     0.945       154
 kaden-channel      0.970     0.964     0.967       167
livedoor-homme      0.930     0.702     0.800       114
   movie-enter      0.919     0.983     0.950       174
        peachy      0.891     0.935     0.912       184
          smax      0.969     0.995     0.981       186
  sports-watch      0.969     0.957     0.963       163
    topic-news      0.955     0.949     0.952       157

     micro avg      0.940     0.940     0.940      1474
     macro avg      0.941     0.931     0.934      1474
  weighted avg      0.941     0.940     0.939      1474
```
- BERT<br>
```
                precision    recall  f1-score   support

dokujo-tsushin      0.953     0.931     0.942       175
  it-life-hack      0.974     0.955     0.964       154
 kaden-channel      0.982     0.982     0.982       167
livedoor-homme      0.943     0.868     0.904       114
   movie-enter      0.956     0.989     0.972       174
        peachy      0.920     0.940     0.930       184
          smax      0.969     0.995     0.981       186
  sports-watch      0.994     0.982     0.988       163
    topic-news      0.969     0.987     0.978       157

     micro avg      0.962     0.962     0.962      1474
     macro avg      0.962     0.959     0.960      1474
  weighted avg      0.962     0.962     0.962      1474
```

## Conclusion
The best model among the 7 models above is **CNN with Sentence Piece**.<br>
Results may be changed if you do more complicated classification tasks.<br>
For each DNN model tested on both MeCab and Sentence Piece, such as MLP, CNN or biLSTM, a model that used **Sentence Piece** outperformed the one that used fastText+MeCab+ipadicNEologd.

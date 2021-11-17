# text-processing-indexing

## Statistics

### Max time possible
Tamanho 0 com porter stemmer e sem stopwords 

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Video_Games_v1_00.tsv -l 0 -w -s
```
| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 110| |
| Indexing time (s) | 201.43 | |
| Total index size on disk (MB) | 60.55| |
| Vocabulary size | 51188 ||
|Index searcher start up time (s) | 0.63 ||


### Average 
tamanho 3 com porter stemmer e com stopwords default

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Video_Games_v1_00.tsv -l 3 -w 
```

### comparar porter stemmer
tamanho 3 sem porter stemmer e com stopwords default

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Video_Games_v1_00.tsv -l 3 -w -p
```

### 
tamanho 3 sem porter stemmer e com stopwords default com poucas palavras
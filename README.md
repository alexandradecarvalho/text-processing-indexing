# text-processing-indexing

## Running options

| ||
|:-----|:--------:|
| -f  [string] |  Path of the file of the dataset to be used  |
| -l [int] | Minimum required length of words to be indexed (default 3) | |
| -s [string]| Path of the file for stopword list (default stop.txt) if no file is passed no list will be used|
| -p | Deactivate porter stemmer|
| -w [int] | Set the temporary index segment write criteria to be number of words read (default 100000) instead of memory usage  |
| -d | Set the number of documents to be read each time from the dataset (default 500)|



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

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Music_Purchase_v1_00.tsv -l 0 -w -s
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 861| |
| Indexing time (s) | 1956.55 | |
| Total index size on disk (MB) | 600.54| |
| Vocabulary size | 302801||
|Index searcher start up time (s) | 8.11 ||

```
python3 main.py -f datasets/amazon_reviews_us_Music_v1_00.tsv -l 0 -s
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 861| |
| Indexing time (s) | 36851.92 | |
| Total index size on disk (MB) | 3602.25| |
| Vocabulary size | 958413||
|Index searcher start up time (s) | 48.40 ||

### Average 
tamanho 3 com porter stemmer e com stopwords default

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Video_Games_v1_00.tsv -l 3 -w 
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 62| |
| Indexing time (s) | 177.82 | |
| Total index size on disk (MB) | 41.23| |
| Vocabulary size | 47401 ||
|Index searcher start up time (s) | 0.43 ||

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Music_Purchase_v1_00.tsv -l 3 -w 
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 498| |
| Indexing time (s) | 1478.16 | |
| Total index size on disk (MB) | 397.68| |
| Vocabulary size | 292964 ||
|Index searcher start up time (s) | 4.49 ||

```
python3 main.py -f datasets/amazon_reviews_us_Books_v1_00.tsv -l 3
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 3| |
| Indexing time (s) | 11637.22 | |
| Total index size on disk (MB) | 4489.20| |
| Vocabulary size | 1146385 ||
|Index searcher start up time (s) | 59.06 ||



### Comparar porter stemmer
tamanho 3 sem porter stemmer e com stopwords default

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Video_Games_v1_00.tsv -l 3 -w -p
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 62| |
| Indexing time (s) | 62.90 | |
| Total index size on disk (MB) | 43.00| |
| Vocabulary size | 67905 ||
|Index searcher start up time (s) | 0.47 ||

```
python3 main.py -f datasets/amazon_reviews_us_Digital_Music_Purchase_v1_00.tsv -l 3 -w -p
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 498| |
| Indexing time (s) | 547.28 | |
| Total index size on disk (MB) | 407.40| |
| Vocabulary size | 360326 ||
|Index searcher start up time (s) | 4.69 ||


```
python3 main.py -f datasets/amazon_reviews_us_Music_v1_00.tsv -l 3  -p
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 2| |
| Indexing time (s) | 2079.60 | |
| Total index size on disk (MB) | 2611.59| |
| Vocabulary size | 1162931 ||
|Index searcher start up time (s) | 37.19 ||

```
python3 main.py -f datasets/amazon_reviews_us_Books_v1_00.tsv -l 3 -p
```

| |Margarida| Alexandra |
|:-----|:--------:|------:|
| Temporary index segments | 5| |
| Indexing time (s) | 7782.40 | |
| Total index size on disk (MB) | 4668.44 | |
| Vocabulary size | 1417663 ||
|Index searcher start up time (s) | 63.93 ||


### 
tamanho 3 sem porter stemmer e com stopwords default com poucas palavras
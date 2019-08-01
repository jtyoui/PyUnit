import numpy
from collections import Counter
from keras.preprocessing.sequence import pad_sequences


def load_data(train_path, dev_path):
    train = _parse_data(open('data/train.txt', 'rb'))
    word_counts = Counter(row[0].lower() for sample in train for row in sample)
    vocab = [w for w, f in iter(word_counts.items()) if f >= 2]
    chunk_tags = ['O', 'B-a', 'I-a', 'B-b', 'I-b', "B-c", "I-c"]
    train = _process_data(train, vocab, chunk_tags)
    # test = _parse_data(open('data/test_data.data', 'rb'))
    # test = _process_data(vocab, chunk_tags)
    return train, (vocab, chunk_tags)


def _parse_data(fh, split_text='\n'):
    string = fh.read().decode('utf-8')
    data = [[row.split() for row in sample.split(split_text)] for sample in
            string.strip().split(split_text + split_text)]
    fh.close()
    return data


def _process_data(data, vocab, chunk_tags, maxlen=None, onehot=False):
    if maxlen is None:
        maxlen = max(len(s) for s in data)
    word2idx = dict((w, i) for i, w in enumerate(vocab))
    x = [[word2idx.get(w[0].lower(), 1) for w in s] for s in data]  # set to <unk> (index 1) if not in vocab
    y_chunk = [[chunk_tags.index(w[1]) for w in s] for s in data]
    x = pad_sequences(x, maxlen)  # left padding
    y_chunk = pad_sequences(y_chunk, maxlen, value=-1)
    if onehot:
        y_chunk = numpy.eye(len(chunk_tags), dtype='float32')[y_chunk]
    else:
        y_chunk = numpy.expand_dims(y_chunk, 2)
    return x, y_chunk


def process_data(data, vocab, maxlen=100):
    word2idx = dict((w, i) for i, w in enumerate(vocab))
    x = [word2idx.get(w[0].lower(), 1) for w in data]
    length = len(x)
    x = pad_sequences([x], maxlen)  # left padding
    return x, length

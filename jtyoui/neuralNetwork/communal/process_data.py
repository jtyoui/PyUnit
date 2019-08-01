import numpy
from collections import Counter
from keras.preprocessing.sequence import pad_sequences


def load_data(train_path, dev_path=None):
    train = _parse_data(open(train_path, 'rb'))
    word_counts = Counter(row[0].lower() for sample in train for row in sample)
    vocab = [w for w, f in iter(word_counts.items()) if f >= 2]
    chunk_tags = ['O', 'B-a', 'I-a', 'B-b', 'I-b', "B-c", "I-c"]
    train = _process_data(train, vocab, chunk_tags)
    if dev_path:
        dev = _parse_data(open(dev_path, 'rb'))
        dev = _process_data(dev, vocab, chunk_tags)
        return train, dev, (vocab, chunk_tags)
    return train, (vocab, chunk_tags)


def _parse_data(fh, split_text='\n'):
    string = fh.read().decode('utf-8')
    data = [[row.split() for row in sample.split(split_text)] for sample in
            string.strip().split(split_text + split_text)]
    fh.close()
    return data


def _process_data(data, vocab, chunk_tags, max_len=None, one_hot=False):
    if max_len is None:
        max_len = max(len(s) for s in data)
    word2idx = dict((w, i) for i, w in enumerate(vocab))
    x = [[word2idx.get(w[0].lower(), 1) for w in s] for s in data]
    y_chunk = [[chunk_tags.index(w[1]) for w in s] for s in data]
    x = pad_sequences(x, max_len)
    y_chunk = pad_sequences(y_chunk, max_len, value=-1)
    if one_hot:
        y_chunk = numpy.eye(len(chunk_tags), dtype='float32')[y_chunk]
    else:
        y_chunk = numpy.expand_dims(y_chunk, 2)
    return x, y_chunk


def process_data(data, vocab, max_len=100):
    word2idx = dict((w, i) for i, w in enumerate(vocab))
    x = [word2idx.get(w[0].lower(), 1) for w in data]
    length = len(x)
    x = pad_sequences([x], max_len)
    return x, length

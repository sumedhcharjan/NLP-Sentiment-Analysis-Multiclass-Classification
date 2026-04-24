from collections import Counter


def build_vocab(texts, max_size=10000):
    all_words = []

    for text in texts:
        words = text.split()  # split sentence into words
        all_words.extend(words)

    # count word frequency
    word_counts = Counter(all_words)

    # take most common words
    most_common = word_counts.most_common(max_size)

    # assign index (start from 1)
    vocab = {word: idx + 1 for idx, (word, _) in enumerate(most_common)}

    return vocab



def text_to_sequence(text, vocab):
    words = text.split()
    sequence = [vocab.get(word, 0) for word in words]  # 0 for unknown words
    return sequence


def texts_to_sequences(texts, vocab):
    sequences = [text_to_sequence(text, vocab) for text in texts]
    return sequences
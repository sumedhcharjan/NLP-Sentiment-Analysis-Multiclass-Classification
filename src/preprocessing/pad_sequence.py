def pad_sequences(sequences, max_len):
    padded_sequences = []

    for seq in sequences:
        if len(seq) < max_len:
            # add zeros at beginning
            padded = [0] * (max_len - len(seq)) + seq
        else:
            # truncate if too long
            padded = seq[:max_len]

        padded_sequences.append(padded)

    return padded_sequences
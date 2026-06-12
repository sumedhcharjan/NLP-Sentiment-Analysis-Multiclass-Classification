import torch
import torch.nn as nn


class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim):
        super(LSTMModel, self).__init__()

        # Embedding layer
        self.embedding = nn.Embedding(vocab_size, embed_dim)

        # Changed to BiLSTM
        self.lstm = nn.LSTM(
            embed_dim,
            hidden_dim,
            batch_first=True,
            bidirectional=True
        )

        # Attention layers
        self.attn = nn.Linear(hidden_dim * 2, hidden_dim)
        self.v = nn.Linear(hidden_dim, 1, bias=False)

        # FC input changes because BiLSTM output = hidden_dim*2
        self.fc = nn.Linear(hidden_dim * 2, output_dim)

    def forward(self, x):

        # Step 1: Embedding
        x = self.embedding(x)
        # shape: (batch, seq_len, embed_dim)

        # Step 2: BiLSTM output
        lstm_out, _ = self.lstm(x)
        # shape: (batch, seq_len, hidden_dim*2)

        # Step 3: Attention energy
        energy = torch.tanh(self.attn(lstm_out))
        # shape: (batch, seq_len, hidden_dim)

        # Step 4: Convert to attention scores
        attention = self.v(energy).squeeze(-1)
        # shape: (batch, seq_len)

        # Step 5: Normalize
        weights = torch.softmax(attention, dim=1)
        # shape: (batch, seq_len)

        # Step 6: Weighted sum (context vector)
        context = torch.sum(
            lstm_out * weights.unsqueeze(-1),
            dim=1
        )
        # shape: (batch, hidden_dim*2)

        # Step 7: Classification
        out = self.fc(context)

        return out
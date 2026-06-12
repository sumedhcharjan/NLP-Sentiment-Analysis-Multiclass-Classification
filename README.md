# Sentiment Analysis using BiLSTM + Attention

A Deep Learning based NLP project for **Trinary Sentiment Classification** (**Positive, Neutral, Negative**) using **Bidirectional LSTM (BiLSTM)** and an **Attention Mechanism**.

This project improves a baseline LSTM model by capturing context from both forward and backward directions while learning to focus on the most important words in a sentence.

---

## Overview

Sentiment analysis is one of the fundamental tasks in Natural Language Processing (NLP), where the goal is to determine the emotional tone behind a piece of text.

Traditional LSTM models rely mainly on the final hidden state, which can lead to information loss from earlier important words.

This project addresses that limitation by:

- Implementing a **Bidirectional LSTM** for richer contextual understanding.
- Using an **Attention Mechanism** to dynamically assign importance to words.
- Comparing performance against a standard LSTM baseline.

---

## Features

- Trinary sentiment classification:
  - Positive
  - Neutral
  - Negative
- Text preprocessing pipeline
- Tokenization and vocabulary building
- Sequence padding
- Baseline LSTM model
- Improved BiLSTM + Attention model
- Comparative model evaluation
- Performance metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score

---

## Model Architecture

```text
Input Text
   ↓
Embedding Layer
   ↓
BiLSTM Layer
   ↓
Attention Layer
   ↓
Context Vector
   ↓
Fully Connected Layer
   ↓
Softmax
   ↓
Output (3 Classes)
```

---

## Why BiLSTM + Attention?

### BiLSTM

Unlike traditional LSTM, BiLSTM processes text in both directions:

- Left → Right
- Right → Left

This allows the model to understand both past and future context.

Example:

```text
"The movie was not good"
```

Understanding the word **not** becomes easier when future context is available.

---

### Attention Mechanism

Attention helps the model focus on the most relevant words instead of depending only on the final hidden state.

Example:

```text
"The movie was boring but the ending was amazing"
```

The attention layer can assign higher importance to:

- **boring**
- **amazing**

which improves prediction quality.

---

## Tech Stack

- Python
- PyTorch
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

---

## Project Structure

```bash
Sentiment-Analysis-BiLSTM-Attention/
│── data/
│── models/
│── notebooks/
│── train.py
│── evaluate.py
│── preprocess.py
│── model.py
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-repo-link>
cd Sentiment-Analysis-BiLSTM-Attention
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Training

Run:

```bash
python train.py
```

---

## Evaluation

Run:

```bash
python evaluate.py
```

Metrics evaluated:

- Accuracy
- Precision
- Recall
- F1-score

---

## Results

| Model | Accuracy | F1 Score |
|---|---|---|
| LSTM | XX% | XX% |
| BiLSTM + Attention | XX% | XX% |

> Replace with your actual results after training.

---

## Future Improvements

- Pretrained embeddings (Word2Vec / GloVe)
- Transformer-based sentiment classification
- Attention visualization
- Real-time inference API
- Deployment

---

## Learning Outcomes

Through this project, I learned:

- Sequence modeling using LSTM and BiLSTM
- Attention mechanism fundamentals
- Context-aware text classification
- Model evaluation techniques
- Comparative deep learning experimentation

---

## Author

**Sumedh Charjan**

GitHub: your-github-link  
LinkedIn: your-linkedin-link
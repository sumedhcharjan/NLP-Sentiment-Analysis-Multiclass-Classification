# 🧠 Sentiment Analysis using LSTM (PyTorch)

## 📌 Overview

This project implements a **3-class sentiment analysis model** (Negative, Neutral, Positive) using an LSTM-based neural network built with PyTorch. The model is trained on real-world Twitter data and processes noisy text through a complete NLP pipeline.

---

## 🚀 Features

* Text preprocessing (cleaning, normalization)
* Custom tokenizer and vocabulary builder
* Sequence padding for LSTM input
* LSTM-based deep learning model (PyTorch)
* Multi-class classification (3 sentiments)
* Model saving and inference-ready pipeline

---

## 🏗️ Architecture

```
Raw Text
   ↓
Text Cleaning
   ↓
Tokenization (word → index)
   ↓
Padding (fixed length)
   ↓
Embedding Layer
   ↓
LSTM
   ↓
Fully Connected Layer
   ↓
Output (Negative / Neutral / Positive)
```

---

## 📂 Project Structure

```
sentiment-analysis-lstm/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── preprocessing/
│   │   ├── clean_text.py
│   │   ├── tokenizer.py
│   │   └── pad_sequences.py
│   │
│   ├── model/
│   │   └── lstm_model.py
│   │
│   └── evaluation/
│
├── models/
│   ├── lstm.pth
│   ├── vocab.pkl
│   └── config.pkl
│
├── outputs/
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

* Twitter US Airline Sentiment Dataset
* Contains tweets labeled as:

  * Negative
  * Neutral
  * Positive

---

## ⚙️ Installation

```bash
git clone <your-repo-link>
cd sentiment-analysis-lstm

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Usage

Run the notebook:

```bash
jupyter notebook
```

---

## 🧪 Model Details

* Embedding Size: 128
* Hidden Size: 128
* Output Classes: 3
* Loss Function: CrossEntropyLoss
* Optimizer: Adam

---

## 📈 Results

* Achieved ~70–80% accuracy on test data
* Strong performance on negative sentiment
* Neutral class remains challenging due to ambiguity

---

## 🔍 Key Learnings

* Importance of preprocessing in NLP
* Handling class imbalance
* Sequence modeling with LSTM
* Tokenization and padding strategies
* Evaluation beyond accuracy

---

## 📦 Future Improvements

* Add attention mechanism
* Use pre-trained embeddings (GloVe, Word2Vec)
* Deploy using FastAPI
* Improve neutral class classification

---

## 🤝 Contributing

Feel free to fork and improve this project.

---

## 📜 License

This project is for educational purposes.

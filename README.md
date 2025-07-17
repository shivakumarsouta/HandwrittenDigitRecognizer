# ✍️ Handwritten Digit Recognizer

A machine learning-based web app that predicts handwritten **digits (0–9)** from user-drawn input using a trained **Convolutional Neural Network (CNN)** model.

---

## 🚀 Features

* Predicts handwritten digits in real time using a simple canvas interface.
* Uses a **pre-trained TensorFlow CNN model** (`model.h5`) trained using the `training.py`.
* Interactive **Gradio UI** where users can draw directly on the canvas.

---

## 💠 Setup

```bash
git clone https://github.com/shivkumars005/HandwrittenDigitRecognizer
cd HandwrittenDigitRecognizer
pip install -r requirements.txt
```

Ensure that `model.h5` is placed in the project root directory.

---

## 📆 Running the App

```bash
python app.py
```

---

## 📈 Model Details

* **Preprocessing:** Reshape to `(28, 28, 1)`, grayscale conversion, pixel normalization (0–1 scale).
* **Model Used:** `Convolutional Neural Network (CNN)` trained on the MNIST dataset.
* **Evaluation Metric:** Model accuracy on validation data.

---

## 🏗️ Project Structure

```
├── app.py
├── training.py
├── model.h5
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

* 🖌️ Gradio Canvas UI
* 🤖 TensorFlow / Keras – Model training & prediction

---

## 🙏 Credits

* 📊 Dataset: MNIST Handwritten Digits
* 💡 Inspired by real-world image classification problems

---

## 🙋‍♂️ Connect

[LinkedIn](https://www.linkedin.com/in/shivakumarsouta)
[Portfolio](https://shivakumarsouta-portfolio.vercel.app)
[Mail](shivakumarsouta18@gmail.com)

---
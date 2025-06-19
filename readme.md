# 💬 Local CLI Chatbot

A simple command-line chatbot built with Hugging Face Transformers and Python. This chatbot maintains short-term memory of conversations and provides responses using a pre-trained language model.

## 📁 Project Structure

```
.
├── interface.py        # Main script to run the chatbot
├── chat_memory.py      # Manages recent chat history
├── model_loader.py     # Loads the NLP model from Hugging Face
```

---

## ✅ Features

- Chat with a language model locally
- Maintains context of last few interactions
- Built using Hugging Face Transformers (`flan-t5-small`)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cli-chatbot.git
cd cli-chatbot
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install transformers
```

> Optional: If you don’t have `pip` or `Python` set up properly, install them from [python.org](https://www.python.org/downloads/).

---

## ▶️ Running the Chatbot

```bash
python interface.py
```

### Example Interaction:

```
Welcome to Local CLI Chatbot! Type /exit to quit.

User: What is the capital of France?
Bot: The capital of France is Paris.

User: What language do they speak?
Bot: They speak French in France.

User: /exit
Exiting chatbot. Goodbye!
```

---

## ⚙️ How It Works

- `model_loader.py`: Loads a pre-trained T5 model (`google/flan-t5-small`).
- `chat_memory.py`: Stores the last few (default 3) turns of the conversation.
- `interface.py`: CLI loop that gets user input, constructs a prompt with context, generates response, and displays output.

---

## 🛠️ Customization

- **Use a Different Model:** Edit `model_loader.py`:

  ```python
  def load_model(model_name="google/flan-t5-small"):
      ...
  ```

  Replace with another compatible text-to-text model from [Hugging Face](https://huggingface.co/models).

- **Change Memory Size:** In `interface.py`, modify:

  ```python
  memory = ChatMemory(max_turns=3)
  ```

---

## 📟 License

This project is licensed under the MIT License.


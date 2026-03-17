# DM Buddy RAG

An AI companion designed to help diabetic patients understand and manage their condition by answering relevant diabetes-related questions.

## Features

- **Intelligent Q&A**: Get accurate answers to diabetes-related questions
- **RAG Technology**: Retrieval-Augmented Generation for contextually relevant responses
- **Patient-Focused**: Designed with diabetes management in mind

## Getting Started

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

```bash
git clone <repository-url>
cd dm-buddy-rag
pip install -r requirements.txt
```

### Usage

```python
# Example usage
from dm_buddy import DmBuddy

buddy = DmBuddy()
response = buddy.answer("What is a normal blood sugar level?")
print(response)
```

## Project Structure

```
dm-buddy-rag/
├── README.md
├── requirements.txt
├── src/
│   └── dm_buddy/
└── tests/
```

## Contributing

Contributions are welcome. Please submit pull requests or open issues.

## Disclaimer

This tool is for informational purposes only and should not replace professional medical advice.


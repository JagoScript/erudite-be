# Erudite API

A lightweight FastAPI-based backend for Erudite AI, text generation using Unsloth LLama 3.2 Instruct 1.

---

## Project Structure
```
erudite-be/
├── app/
│   ├── __init__.py             
│   ├── main.py                 # Entry point
│   ├── api/
│   │   ├── __init__.py         
│   │   ├── endpoints.py        # API route definitions
│   ├── core/
│   │   ├── __init__.py        
│   │   ├── config.py           # Application configuration
│   ├── services/
│   │   ├── __init__.py         
│   │   ├── generator.py        # Text generation logic
│   └── models/
│       ├── __init__.py         
│       └── schemas.py          # Request/response validation schemas
├── tests/
│   ├── __init__.py             
│   ├── test_endpoints.py       # Tests for API endpoints
├── requirements.txt            # Python deps
├── README.md                   
└── run.py                      # Run script
```

---

## Requirements
- Python 3.8+
- Pip

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JagoScript/erudite-be
   cd erudite-be
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Linux: source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the API

1. **Start the API:**
   ```bash
   python run.py
   ```
---

## API Endpoints

### `POST /generate`
Generates text based on a given prompt.

- **Request Body:**
  ```json
  {
    "prompt": "Your input prompt here"
  }
  ```

---

## Testing

1. **Run Unit Tests:**
   ```bash
   pytest
   ```

---

## Customization
- **Model Configuration:** Update `app/core/config.py` to change the default language model.
- **Add New Endpoints:** Define additional routes in `app/api/endpoints.py` and corresponding logic in `app/services/`.

---

## Acknowledgments
- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)

---

## License
MIT License. See `LICENSE` for details.

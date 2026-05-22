# Quelora Detoxify API

FastAPI-based REST service that wraps the Detoxify multilingual model to provide real-time text toxicity detection.

Designed for local deployment, this service exposes a simple API to evaluate user-generated content and return structured toxicity scores, making it easy to integrate into moderation pipelines.

---

## 🚀 Features

* Multilingual toxicity detection
* FastAPI-powered REST API
* Lightweight and easy to deploy
* JSON responses with multiple toxicity categories
* Optimized for local execution (no external API calls)

---

## 📦 Requirements

* Python 3.9+
* pip

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

Start the server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```
http://localhost:8000
```

---

## 🧪 Usage Example

### Request

```bash
curl -X POST http://localhost:8000/moderate \
  -H "Content-Type: application/json" \
  -d '{"text": "Eres un completo imbécil, te voy a destruir."}'
```

---

### Response

```json
{
  "toxicity": 0.985,
  "severe_toxicity": 0.125,
  "obscene": 0.052,
  "threat": 0.875,
  "insult": 0.963,
  "identity_attack": 0.012
}
```

---

## 📡 API Reference

### POST `/moderate`

Evaluates the toxicity of a given text.

#### Request Body

```json
{
  "text": "string"
}
```

#### Response

Returns a JSON object with toxicity scores:

| Field           | Description               |
| --------------- | ------------------------- |
| toxicity        | General toxicity level    |
| severe_toxicity | Highly toxic content      |
| obscene         | Obscene language          |
| threat          | Threatening language      |
| insult          | Insulting content         |
| identity_attack | Attacks based on identity |

All values range from **0.0 to 1.0**.

---

## ⚙️ Implementation Details

* Uses the **Detoxify multilingual model**
* Model is loaded at startup to avoid repeated downloads
* Predictions run in a threadpool to prevent blocking the main event loop
* Outputs are normalized to standard Python floats for JSON compatibility

---

## 🧩 Use Cases

* Content moderation systems
* Chat platforms
* Social networks
* Comment filtering pipelines
* AI safety layers

---

## 📄 License

[AGPL-3.0-only](./LICENSE) — Copyright (C) 2026 Germán Zelaya.

Part of the **[Quelora](https://github.com/Quelora)** project.


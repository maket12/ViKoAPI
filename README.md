# 🧩 ViKoAPI

<p align="center">
  <img src=".github/ViKoAPI main-logo.png" alt="ViKoAPI MainLogo" width="50%"/>
</p>

**ViKoAPI** is a modern, lightweight, and fully-featured framework for interacting with the [VK API](https://dev.vk.com/ru/reference).
It provides a convenient interface for VK developers with automatic error handling, validation, and data class serialization.

---

## 🚀 Key Features

- 🔐 **Authorization** via `client.authorize()` — automatic token retrieval if not provided.
- 🧠 **Full VK API error handling** — all API errors are processed and raised as custom exceptions.
- 🧩 **Data classes** for all major VK objects (`User`, `Group`, `Message`, etc.).
- ⚙️ **`.to_dict()`** method on all entities to obtain raw VK API response format.
- 🧾 **Data validation** and type checking.
- 🌐 **Proxy support** on client initialization.
- 🧱 **Core modular architecture** for flexibility and extensibility.

---

## 📦 Installation

```bash
pip install git+https://github.com/maket12/ViKoAPI.git
```

---

## 🧰 Basic Usage Example

```python
from vikoapi import ViKoClient

# Authorization (token will be automatically retrieved and stored)
client = ViKoClient(api_token="vk1.xxxx")

# Get user information
user = client.users.get(user_ids=[1])

print(user.first_name, user.last_name)
print(user.to_dict())
```

---

## ⚙️ Proxy Support

```python
client = ViKoClient(api_token="...", proxy="http://127.0.0.1:8080")
```

---

## 🧠 Error Handling

ViKoAPI wraps VK API responses into its own structured exceptions:

```python
from vikoapi.errors.exceptions import ViKoAPIResponseError, AuthorisationError

try:
    user = client.users.get(user_ids=-1)
except ViKoAPIResponseError as e:
    print(f"VK API error: {e.code} - {e.msg}")
except AuthorisationError:
    print("Authorization failed!")
```

---

## 🧩 Project Structure

```
ViKoAPI/
├── core/                      # Framework core logic
│   ├── object_factory/         # Object construction and management
│   ├── base_session.py         # Core session class
│   ├── response_middleware.py  # Response parsing and validation
│   └── session_mixin.py        # Session mixins and extensions
│
├── enums/                     # Enumerations for VK object constants
│
├── errors/                    # Custom exception classes
│   └── exceptions.py
│
├── methods/                   # VK API method handlers
│
├── vk_types/                  # Data classes representing VK API objects
│   ├── album/
│   ├── attachments/
│   ├── button/
│   ├── chat/
│   ├── comment/
│   ├── discussion/
│   ├── friends/
│   ├── group/
│   ├── post/
│   ├── price/
│   ├── reaction/
│   ├── user/
│   └── voice_message/
│
└── README.md
```

---

## 🧱 Architecture Overview

- **`core/`** – The main framework engine (authorization, sessions, middleware).
- **`methods/`** – VK API method implementations (users, groups, wall, messages, etc.).
- **`vk_types/`** – Typed Python data models representing VK objects, each with `to_dict()` for serialization.
- **`errors/`** – All VK and internal exceptions are defined here.
- **`enums/`** – Enumerations for VK constants (e.g., `Sex`, `RelationStatus`, `Platform`, etc.).

---

## 📄 License

**MIT License** — feel free to use, modify, and distribute.

---

> Made with ❤️ by [maket12](https://github.com/maket12)

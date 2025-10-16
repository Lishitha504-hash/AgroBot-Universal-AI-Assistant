## AgroBot-AI agricultural assistant

overview
---------
This project is an agriculture chatbot web application that helps users get farming-related information in multiple languages. Users can create accounts, log in, and chat with the assistant to ask about soil types, fertilizers, pests, and harvesting. The chatbot provides answers using built-in knowledge or by connecting to an AI service. All conversations are saved for users to review later. There is also a special admin area where chats and users can be managed easily.

## Features

* User registration, login, and logout with secure password hashing
* Chat interface to interact with the agriculture chatbot
* Offline knowledge base for farming info (soil, fertilizer, pests, harvesting)
* OpenAI GPT fallback for unanswered queries
* Automatic language detection and translation of responses
* Chat history saved per user in SQLite database
* Admin panel to view and manage chat histories

---

## Key Components and Files

### `app.py`

*  Handles user and admin login, registration, chat, and logout operations through various routes.
*  Manages the chat interface, processes user messages, and stores chat history for later access.


### `chatbot_model.py`

* Handles language detection, greeting/farewell detection, offline knowledge queries, and calls OpenAI API if needed.
* Translates answers to user's language.

### `database.py`

* Defines `User` and `ChatHistory` models using SQLAlchemy.
* Manages password hashing and retrieval.

### `translator_util.py`

* Detects language and translates chatbot responses.

---


##  Outputs

### 1. User Registration


<img width="1366" height="768" alt="Screenshot (55)" src="https://github.com/user-attachments/assets/e295aa59-b21f-43ed-aabd-e5ba336ab2eb" />

### 2. User Login


<img width="1366" height="768" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/b7a4f102-5e91-4df5-8f09-01da5e6e3459" />

### 3. Chat Interaction


<img width="1366" height="768" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/45a86b60-0c0f-4606-941e-6f0826c6893b" />

<img width="1366" height="768" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/ede5952b-2aec-422a-b617-9fec4cbf5a65" />

## logout


<img width="1366" height="768" alt="Screenshot (59)" src="https://github.com/user-attachments/assets/01fc01ca-91bc-472e-8205-14cbe96d2a33" />


---

## Additional Notes

* If OpenAI API key is missing or fails, offline knowledge base is used.
* Passwords are securely hashed.
* Multilingual support allows chatting in Tamil, Hindi, Malayalam, Telugu, and English.


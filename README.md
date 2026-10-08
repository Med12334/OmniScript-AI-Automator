# 🤖 OmniScript AI Automator

OmniScript is a multi-tiered backend architecture designed to act as the "brain" for an automated mobile agent. Built with Python and FastAPI, the system ingests raw on-screen text from an Android device, processes it through Google's Gemini 2.5 Flash AI, and calculates the precise next action the automated bot should take. 

The project also includes a frontend telemetry dashboard to visualize execution metrics, success rates, and API latency.

## ⚡ Core Features
* **AI Decision Engine:** Integrates the Google Gemini (`gemini-2.5-flash`) Generative AI model to analyze UI context and map out logical user flows.
* **High-Performance Routing:** Utilizes FastAPI and Uvicorn for rapid, asynchronous local network requests.
* **Secure Credential Management:** Implements `python-dotenv` and `.gitignore` protocols to strictly isolate API keys from the source code, adhering to secure development lifecycles.
* **Telemetry Dashboard:** Features a responsive HTML/JS frontend utilizing `Chart.js` to render visual analytics of the bot's historical performance.

## 🛠️ Tech Stack
* **Backend:** Python 3, FastAPI, Uvicorn, Pydantic
* **AI Integration:** Google Generative AI SDK (`google-generativeai`)
* **Security:** `python-dotenv`
* **Frontend Visualization:** HTML5, CSS3, Chart.js

## 🚀 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Med12334/OmniScript-AI-Automator.git](https://github.com/Med12334/OmniScript-AI-Automator.git)
   cd OmniScript-AI-Automator

# 🌦️ Weather App using Python and OpenWeather API

This is a simple command-line weather application built in Python. It fetches and displays real-time weather data for any city using the **OpenWeather API**.

---

## 🧰 Requirements

- Python 3.6 or above
- `requests` package
- A free API key from [OpenWeather](https://home.openweathermap.org/)

---

## 📥 Installation & Setup

### 1. Clone or download the project

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app

2. Install dependencies
bash

pip install -r requirements.txt
If requirements.txt is not available, just run:

bash

pip install requests python-dotenv
🔐 Add Your API Key
To use this app, you must get a free API key from OpenWeather:

How to get your API key:
Go to OpenWeather Sign Up

Create an account and log in

Navigate to the "API keys" section

Copy your default API key

3. Create a .env file in the root directory:
ini

OPENWEATHER_API_KEY=your_api_key_here
❗ Important: Do NOT upload your .env file publicly or commit it to GitHub. Your API key is private and must be kept secure.

▶️ Running the App
bash

python app.py
Then enter a city name when prompted.

⚠️ Common Errors
Error: API key not found!
→ You forgot to create the .env file or the OPENWEATHER_API_KEY is missing inside it.

Invalid API key
→ Make sure you copied the correct key from your OpenWeather account.

👨‍💻 Developed By
Sofia Ibrahim


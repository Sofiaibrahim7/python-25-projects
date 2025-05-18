# Discord Bot Setup Guide

## Requirements
- Python 3.6 or above
- `python-dotenv` package (install with `pip install python-dotenv`)
- A Discord Bot token from Discord Developer Portal

## Setup Instructions

1. **Clone or download the project code**

2. **Create a `.env` file in the root folder of the project**

3. **Add your Discord Bot token to the `.env` file like this:**

   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

   > **Note:** Replace `your_discord_bot_token_here` with your actual token.  
   > Do **not** add quotes (" ") around the token.

4. **Install dependencies (if not installed yet):**

   ```bash
   pip install -r requirements.txt
   ```

   *(If you don't have a `requirements.txt` file, just run:)*

   ```bash
   pip install python-dotenv discord
   ```

5. **Run the bot:**

   ```bash
   python app.py
   ```

---

## Important

- Do **not** share your `.env` file publicly or push it to GitHub.  
- Your token is secret and should be kept safe to prevent misuse.

---

If you face any issues with token or running the bot, check your `.env` file and token validity first.
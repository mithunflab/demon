# Mithun's Telegram AI AutoChat Bot

This is a Telegram auto-reply bot using Telethon and Groq's AI hosted on Railway.

## 🚀 Deployment Instructions

1. Go to [https://railway.app](https://railway.app)
2. Click **New Project** → **Deploy from GitHub Repo or ZIP**
3. Upload this ZIP
4. Set Environment Variables:
   - TELEGRAM_API_ID
   - TELEGRAM_API_HASH
   - TELEGRAM_PHONE (like +919876543210)
   - GROQ_API_KEY (your Groq key: starts with `gsk_`)

## 🧠 Features
- Uses LLaMA 3 via Groq for replies
- Only replies when you're offline or not chatting
- Logs interactions to console
- Flask server for 24/7 uptime (use with UptimeRobot if needed)
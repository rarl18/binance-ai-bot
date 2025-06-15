
# Binance AI Trading Bot 🚀

This is a Dockerized bot that uses AI to generate trading signals for Binance Futures.

## Features
- Uses Binance API
- Calculates indicators (RSI, MACD, EMA)
- AI model (Random Forest or similar)
- Sends BUY/SELL signal every 15 minutes

## Deploy to Render

1. Push this repo to GitHub
2. Go to https://render.com
3. New → Web Service → Connect your repo
4. Choose Docker environment
5. Set environment variables:
   - BINANCE_API_KEY
   - BINANCE_API_SECRET
6. Hit Deploy 🎉

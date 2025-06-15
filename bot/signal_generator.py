
import joblib
from bot.fetch_data import get_klines
from bot.indicators import add_indicators

model = joblib.load('models/signal_model.pkl')

def generate_signal(symbol="BTCUSDT"):
    df = get_klines(symbol)
    df = add_indicators(df)
    X = df[['rsi', 'macd', 'ema_signal']].tail(1)
    prediction = model.predict(X)[0]
    return "BUY" if prediction == 1 else "SELL"

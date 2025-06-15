
import ta

def add_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['macd'] = ta.trend.MACD(df['close']).macd()
    df['ema'] = ta.trend.EMAIndicator(df['close'], window=21).ema_indicator()
    df['ema_signal'] = df['close'] > df['ema']
    return df.dropna()

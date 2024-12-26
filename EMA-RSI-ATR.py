import pandas as pd
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange
from ta.trend import EMAIndicator

# Define the input and output file paths
input_file = 'BTCUSDT-1m.csv'
output_file = 'NEW_btcusdt_rsi_ema_atr_data-1m.csv'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Convert the 'timestamp' column to datetime if it's not already
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Calculate additional columns for new data
df['Turnover'] = round(df['close'] * df['volume'], 2)
df['Amplitude'] = round((df['high'] - df['low']) / df['open'] * 100, 2)
df['Percentage Change'] = round(((df['close'] - df['open']) / df['open']) * 100, 2)
df['Change in Price'] = round(df['close'] - df['open'], 2)
df['Turnover Rate'] = round((df['volume'] / df['volume'].shift(1)) * 100, 2)

# Sort the DataFrame by timestamp (if not already sorted)
df.sort_values(by='timestamp', inplace=True)

# Calculate RSI with a 14-period window
rsi_period = 14
rsi_indicator = RSIIndicator(df['close'], window=rsi_period)
df['rsi'] = rsi_indicator.rsi()

# Calculate ATR with length 14 using RMA as smoothing
atr_period = 14
atr_indicator = AverageTrueRange(df['high'], df['low'], df['close'], window=atr_period, fillna=True)
df['atr'] = atr_indicator.average_true_range()

# Calculate 50-period EMA
ema_fast_period = 50
ema_fast_indicator = EMAIndicator(df['close'], window=ema_fast_period)
df['ema_fast'] = ema_fast_indicator.ema_indicator()

# Calculate 200-period EMA
ema_slow_period = 200
ema_slow_indicator = EMAIndicator(df['close'], window=ema_slow_period)
df['ema_slow'] = ema_slow_indicator.ema_indicator()

# Save the DataFrame with RSI, ATR, and EMA data to a new CSV file
df.to_csv(output_file, index=False)

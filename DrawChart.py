# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Read the CSV data into a DataFrame while skipping the header row
# data = pd.read_csv('NEW_btcusdt_rsi_ema_atr_data-1m.csv', names=["timestamp", "open", "high", "low", "close", "volume", "Turnover", "Amplitude", "Percentage Change", "Change in Price", "Turnover Rate", "rsi", "atr", "fast_ema", "slow_ema"], skiprows=1)
#
# # Convert the 'timestamp' column to a datetime object
# data['timestamp'] = pd.to_datetime(data['timestamp'])
#
# # Create a new figure and axis for the plot
# fig, ax1 = plt.subplots(figsize=(12, 6))
#
# # Plot the close price
# ax1.plot(data['timestamp'], data['close'], label='Close', color='black', alpha=0.7)
# ax1.set_xlabel('Timestamp')
# ax1.set_ylabel('Price (USD)')
#
# # Plot the fast EMA line
# ax1.plot(data['timestamp'], data['fast_ema'], label='Fast EMA', color='blue')
#
# # Plot the slow EMA line
# ax1.plot(data['timestamp'], data['slow_ema'], label='Slow EMA', color='red')
#
# # Format the x-axis to show
# # dates
# plt.xticks(rotation=45)
# ax1.xaxis.set_major_locator(plt.MaxNLocator(10))  # Show a maximum of 10 ticks on the x-axis
#
# # Add a legend
# ax1.legend()
#
# fig2, ax2 = plt.subplots(figsize=(12, 6))
# ax2.plot(data['timestamp'], data['atr'], label='ATR', color='black', alpha=0.7)
# ax2.set_xlabel('Timestamp')
# ax2.set_ylabel('ATR')
# ax2.xaxis.set_major_locator(plt.MaxNLocator(10))
# ax2.legend()
#
# # Show the plot
# plt.show()
#
#
# # Initialize variables to track crossover and crossunder
# crossover_points = []
# crossunder_points = []
#
# # Detect crossover and crossunder points
# for i in range(1, len(data)):
#     if data['fast_ema'][i] > data['slow_ema'][i] and data['fast_ema'][i - 1] <= data['slow_ema'][i - 1]:
#         crossover_points.append(data['timestamp'][i])
#         print(f"Crossover at {data['timestamp'][i]}")
#     elif data['fast_ema'][i] < data['slow_ema'][i] and data['fast_ema'][i - 1] >= data['slow_ema'][i - 1]:
#         crossunder_points.append(data['timestamp'][i])
#         print(f"Crossunder at {data['timestamp'][i]}")
#
#
# # Print crossover and crossunder points
# print("\nCrossover Points:")
# for point in crossover_points:
#     print(point)
#
# print("\nCrossunder Points:")
# for point in crossunder_points:
#     print(point)

# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Read the CSV data into a DataFrame while skipping the header row
# data = pd.read_csv('NEW_btcusdt_rsi_ema_atr_data-1m.csv', names=["timestamp", "open", "high", "low", "close", "volume", "Turnover", "Amplitude", "Percentage Change", "Change in Price", "Turnover Rate", "rsi", "atr", "fast_ema", "slow_ema"], skiprows=1)
#
# # Convert the 'timestamp' column to a datetime object with the specified format
# data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')
#
# # Define the specific starting timestamps for the two timelines
# start_time_1 = pd.to_datetime('8/27/2023 9:00', format='%m/%d/%Y %H:%M')
# start_time_2 = pd.to_datetime('8/27/2023 20:00', format='%m/%d/%Y %H:%M')
#
# # Calculate the ending timestamps by adding 2 hours to the start times
# end_time_1 = start_time_1 + pd.DateOffset(hours=3)
# end_time_2 = start_time_2 + pd.DateOffset(hours=3)
#
# # Filter the data for the two timelines
# data_1 = data[(data['timestamp'] >= start_time_1) & (data['timestamp'] <= end_time_1)]
# data_2 = data[(data['timestamp'] >= start_time_2) & (data['timestamp'] <= end_time_2)]
#
# # Extract the 'close' values for both timelines
# close_1 = data_1['close'].reset_index(drop=True)
# close_2 = data_2['close'].reset_index(drop=True)
#
# # Calculate the correlation between the 'close' data sets
# correlation = close_1.corr(close_2)
#
# # Create a new figure for the plot
# plt.figure(figsize=(12, 6))
#
# # Plot the 'close' data for the first timeline in blue
# plt.plot(close_1, label='Close - Timeline 1', color='blue', alpha=0.7)
#
# # Plot the 'close' data for the second timeline in red
# plt.plot(close_2, label='Close - Timeline 2', color='red', alpha=0.7)
#
# plt.xlabel('Data Point')
# plt.ylabel('Price (USD)')
# plt.title('Comparison of Similarity - Price Trends')
# plt.legend()
# plt.tight_layout()
#
# # Add correlation coefficient as text annotation
# plt.annotate(f'Correlation: {correlation:.2f}', xy=(0.5, 0.9), xycoords='axes fraction', ha='center')
#
# # Show the plot
# plt.show()
#

import mpf as mpf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import plotly.graph_objs as go

# Read the CSV data into a DataFrame while skipping the header row
data = pd.read_csv('NEW_btcusdt_rsi_ema_atr_data-1m.csv', names=["timestamp", "open", "high", "low", "close", "volume", "Turnover", "Amplitude", "Percentage Change", "Change in Price", "Turnover Rate", "rsi", "atr", "fast_ema", "slow_ema"], skiprows=1)

# Convert the 'timestamp' column to a datetime object with the specified format
data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')

# Define the specific starting timestamps for the two timelines
start_time_1 = pd.to_datetime('8/27/2023 9:00', format='%m/%d/%Y %H:%M')
start_time_2 = pd.to_datetime('8/27/2023 20:00', format='%m/%d/%Y %H:%M')

# Calculate the ending timestamps by adding 3 hours to the start times
end_time_1 = start_time_1 + pd.DateOffset(hours=3)
end_time_2 = start_time_2 + pd.DateOffset(hours=3)

# Filter the data for the two timelines
data_1 = data[(data['timestamp'] >= start_time_1) & (data['timestamp'] <= end_time_1)]
data_2 = data[(data['timestamp'] >= start_time_2) & (data['timestamp'] <= end_time_2)]

# Extract the 'close' values for both timelines
close_1 = data_1['close'].reset_index(drop=True)
close_2 = data_2['close'].reset_index(drop=True)

# Calculate the correlation between the 'close' data sets
correlation = close_1.corr(close_2)

# Create a new figure for the plot
plt.figure(figsize=(12, 6))

# Plot the 'close' data for the first timeline with a solid blue line
plt.plot(close_1, label='Close - Timeline 1', color='blue', linestyle='-', linewidth=2, alpha=0.7)

# Plot the 'close' data for the second timeline with a dashed red line
plt.plot(close_2, label='Close - Timeline 2', color='red', linestyle='--', linewidth=2, alpha=0.7)

plt.xlabel('Data Point')
plt.ylabel('Price (USD)')
plt.title('Comparison of Similarity - Price Trends\n(8/27/2023 9:00 - 8/27/2023 12:00 VS. 8/27/2023 20:00 - 8/27/2023 23:00)')
plt.legend()
plt.tight_layout()

# Add correlation coefficient as text annotation
plt.annotate(f'Correlation: {correlation:.2f}', xy=(0.15, 0.8), xycoords='axes fraction', ha='center', fontsize=12, color='green')

# Add labels to the lines
plt.gca().add_line(Line2D([0], [0], color='blue', linewidth=2, linestyle='-', label='Close - Timeline 1'))
plt.gca().add_line(Line2D([0], [0], color='red', linewidth=2, linestyle='--', label='Close - Timeline 2'))

# Create a DataFrame with the 'timestamp' as the index
data_1.set_index('timestamp', inplace=True)
data_2.set_index('timestamp', inplace=True)

# Show the plot
plt.show()






# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.lines import Line2D
# import numpy as np
#
# # Read the CSV data into a DataFrame while skipping the header row
# data = pd.read_csv('NEW_btcusdt_rsi_ema_atr_data-1m.csv', names=["timestamp", "open", "high", "low", "close", "volume", "Turnover", "Amplitude", "Percentage Change", "Change in Price", "Turnover Rate", "rsi", "atr", "fast_ema", "slow_ema"], skiprows=1)
#
# # Convert the 'timestamp' column to a datetime object with the specified format
# data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')
#
# # Define the specific starting timestamps for the two timelines
# start_time_1 = pd.to_datetime('8/27/2023 9:00', format='%m/%d/%Y %H:%M')
# start_time_2 = pd.to_datetime('8/27/2023 20:00', format='%m/%d/%Y %H:%M')
#
# # Calculate the ending timestamps by adding 3 hours to the start times
# end_time_1 = start_time_1 + pd.DateOffset(hours=3)
# end_time_2 = start_time_2 + pd.DateOffset(hours=3)
#
# # Filter the data for the two timelines
# data_1 = data[(data['timestamp'] >= start_time_1) & (data['timestamp'] <= end_time_1)]
# data_2 = data[(data['timestamp'] >= start_time_2) & (data['timestamp'] <= end_time_2)]
#
# # Extract the 'close' values for both timelines
# close_1 = data_1['close'].reset_index(drop=True)
# close_2 = data_2['close'].reset_index(drop=True)
#
# # Calculate the correlation between the 'close' data sets
# correlation = close_1.corr(close_2)
#
# # 计算趋势线的起点和终点
# trendline_start = 0  # 从数据的第一个点开始
# trendline_end = len(close_1) - 1  # 到数据的最后一个点结束
#
# # 计算趋势线的斜率和截距
# slope, intercept = np.polyfit(range(trendline_start, trendline_end + 1), close_1, 1)
#
# # 使用斜率和截距计算趋势线的值
# trendline_values = [slope * i + intercept for i in range(trendline_start, trendline_end + 1)]
#
# # 创建一个新的图形
# plt.figure(figsize=(12, 6))
#
# # 绘制 'close' 数据的趋势线
# plt.plot(close_1, label='Close - Timeline 1', color='blue', linestyle='-', linewidth=2, alpha=0.7)
# plt.plot(range(trendline_start, trendline_end + 1), trendline_values, label='Trendline', color='green', linestyle='--', linewidth=2, alpha=0.7)
#
# # 绘制 'close' 数据的趋势线的起点和终点
# plt.scatter(trendline_start, close_1.iloc[trendline_start], color='green', marker='o', label='Trendline Start', s=100)
# plt.scatter(trendline_end, close_1.iloc[trendline_end], color='red', marker='x', label='Trendline End', s=100)
#
# # 其余的代码保持不变
#
# # Show the plot
# plt.show()



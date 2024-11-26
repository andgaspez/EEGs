import pandas as pd
import matplotlib.pyplot as plt

""""The data source is the file with the name UnicornRecorder_AntC1_Rostros_08_11_2024_10_32_290"""

# Replace 'your_file.csv' with the path to your CSV file
eeg_data = pd.read_csv('EEGdata.csv', header=None)

# Display the first few rows of the DataFrame
eeg_data

# Define the sampling rate (250 Hz)
sampling_rate = 250  # Hz
time_increment = 1 / sampling_rate  # seconds per sample

# Add a "Time (s)" column
eeg_data['Time'] = eeg_data.index * time_increment

# Define new column labels
new_column_labels = [
    'Electrode 0', 'Electrode 1', 'Electrode 2', 'Electrode 3',
    'Electrode 4', 'Electrode 5', 'Electrode 6', 'Electrode 7',
    'Trigger', 'Time'
]

# Replace column names with the new labels
eeg_data.columns = new_column_labels

# Save the updated dataset back to a new file if needed
eeg_data.to_csv('EEGdata_wtime.csv', index=False)  # Replace with your desired save location

# Replace 'your_file.csv' with the path to your CSV file
eeg_data = pd.read_csv('EEGdata_wtime.csv', header=None)

# Display the first few rows of the DataFrame
eeg_data

# Select the "Time (s)" column for the x-axis using its index (-1 for the last column)
time = eeg_data.iloc[:, -1]

# Select one of the electrode columns for the y-axis (e.g., column 0 for "Electrode 1")
electrode_1 = eeg_data.iloc[:, 0]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time, electrode_1, label='Electrode 1')

# Add labels and title
plt.xlabel('Time (s)')
plt.ylabel('Signal Amplitude')
plt.title('Electrode 1 Signal Over Time')
plt.legend()
plt.grid()

# Show the plot
plt.show()
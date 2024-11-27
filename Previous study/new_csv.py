import pandas as pd

# Load the original CSV file
input_file = 'data/previous_data.csv'  # Change this to your input CSV file path
output_file = 'data/previous_data_2.csv'  # Change this to your desired output CSV file path

# Define the features you want to keep
features = ["X2", "X3", "X4", "X5", "X6", "X7", "X8", "X11.1", "X11.2",
            "X14.8", "X14.9", "X14.10", "X17.4", "X17.5", "X17.6",
            "X18.1", "X18.2", "X18.3", "X18.4", "X18.5", "X18.6",
            "X18.7", "X19.1", "X19.2", "X19.3", "X20.1", "X20.2",
            "X20.3", "X21", "X22.1", "X22.2", "X22.3", "X22.4",
            "X22.5", "X22.6", "X24", "X25"]

# Read the CSV file
df = pd.read_csv(input_file)

# Filter the DataFrame to only include the specified features
df_filtered = df[features]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv(output_file, index=False)

print(f"Filtered CSV file saved as: {output_file}")
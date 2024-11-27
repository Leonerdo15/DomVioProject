import pandas as pd
import numpy as np

red_flags = {"Suicide Attempt": 0.15, "Weapon": 0.05, "Gang": 0.06, "Depressed": 0.045, "Community Violence": 0.23,
             "Sexual Abuse": 0.29, "Physical Abuse": 0.07, "Hard Drug Use": 0.07}

red_flags = {key: value / 2 for key, value in red_flags.items()}


def generate_data(number_of_people):
    data = {
        "Age": np.random.randint(16, 90, size=number_of_people),
        "Exchange_Sex": np.random.choice([0, 1], size=number_of_people, p=[0.15, 0.85]),
        "Children": np.random.choice([0, 1, 2, 3], size=number_of_people),
        "Suicide_Attempt": np.random.choice([0, 1], size=number_of_people, p=[0.8, 0.2]),
        "Jail": np.random.choice([0, 1], size=number_of_people, p=[0.7, 0.3]),
        "Male": np.random.choice([0, 1], size=number_of_people),
        "LGBQ": np.random.choice([0, 1], size=number_of_people, p=[0.8, 0.2]),
        "White": np.random.choice([0, 1], size=number_of_people),
        "Literal_Homeless": np.random.choice([0, 1], size=number_of_people, p=[0.9, 0.1]),
        "Weapon": np.random.choice([0, 1], size=number_of_people),
        "Gang": np.random.choice([0, 1], size=number_of_people, p=[0.85, 0.15]),
        "PTSD": np.random.choice([0, 1], size=number_of_people, p=[0.7, 0.3]),
        "Depressed": np.random.choice([0, 1], size=number_of_people, p=[0.6, 0.4]),
        "Community_Violence": np.random.choice([0, 1], size=number_of_people, p=[0.6, 0.4]),
        "Sexual_Abuse": np.random.choice([0, 1], size=number_of_people, p=[0.75, 0.25]),
        "Physical_Abuse": np.random.choice([0, 1], size=number_of_people, p=[0.7, 0.3]),
        "Hard_Drug_Use": np.random.choice([0, 1], size=number_of_people, p=[0.6, 0.4]),
        "Foster_Care": np.random.choice([0, 1], size=number_of_people, p=[0.8, 0.2]),
        "Job": np.random.choice([0, 1], size=number_of_people, p=[0.2, 0.8])
    }
    return pd.DataFrame(data)


def calculate_score(data):
    # Create a column to store the sum of the red flags
    data['Red_Flag_Score'] = (data['Suicide_Attempt'] * red_flags['Suicide Attempt'] +
                              data['Weapon'] * red_flags['Weapon'] +
                              data['Gang'] * red_flags['Gang'] +
                              data['Depressed'] * red_flags['Depressed'] +
                              data['Community_Violence'] * red_flags['Community Violence'] +
                              data['Sexual_Abuse'] * red_flags['Sexual Abuse'] +
                              data['Physical_Abuse'] * red_flags['Physical Abuse'] +
                              data['Hard_Drug_Use'] * red_flags['Hard Drug Use'])

    # Generate the 'Victim' column using the red flag score
    data['Victim'] = data['Red_Flag_Score'].apply(lambda x: np.random.choice([0, 1], p=[1 - x, x]))

    return data


def calculate_combinations_score(data):
    # Adding combination scores to Red_Flag_Score based on conditions

    # Condition 1: Weapon and Gang and Hard_Drug_Use combination
    data['Red_Flag_Score'] += np.where(
        (data['Weapon'] == 1) & (data['Gang'] == 1) & (data['Hard_Drug_Use'] == 1),
        0.15, 0
    )

    # Condition 2: PTSD and Depressed combination
    data['Red_Flag_Score'] += np.where(
        (data['PTSD'] == 1) & (data['Depressed'] == 1),
        0.1, 0
    )

    # Condition 3: Community_Violence and Sexual_Abuse and Physical_Abuse combination
    data['Red_Flag_Score'] += np.where(
        (data['Community_Violence'] == 1) & (data['Sexual_Abuse'] == 1) & (data['Physical_Abuse'] == 1),
        0.25, 0
    )

    return data

def percentage_of_victims(data):
    total = 0
    victims = data["Victim"]
    for victim in victims:
        total += victim

    print(f"The total is {total} = {total/len(victims)*100}%")

# remove the column Red_Flag_Score and save in a csv file named 'domestic_violence_fake_data.csv'
def generate_csv(data):
    # Remove the Red_Flag_Score column
    data = data.drop(columns=['Red_Flag_Score'])

    # Save the DataFrame to a CSV file
    data.to_csv('domestic_violence_fake_data.csv', index=False)

    print("CSV file 'domestic_violence_fake_data.csv' has been generated.")


if __name__ == '__main__':
    # Step 1: Generate the initial dataset
    df = generate_data(10000)  # Generate data for 10,000 people
    print(df.head())  # Display first few rows of generated data for inspection

    # Step 2: Calculate the basic red flag score
    scored_df = calculate_score(df)  # Add basic risk scores
    print(scored_df.head())  # Display first few rows with basic scores

    # Step 3: Calculate combination scores based on the specific conditions
    scored_df1 = calculate_combinations_score(scored_df)  # Add combination scores
    print(scored_df.head())  # Display first few rows with updated scores

    # Step 4: Save the DataFrame to a CSV file (without the 'Red_Flag_Score' column)
    generate_csv(scored_df)  # Save the DataFrame to a CSV file

    # Step 5: Print total red flags score
    red_flags_total = sum(red_flags.values())
    print(f"Total of red flags: {red_flags_total}")

    # Step 6: Calculate and print the percentage of victims
    percentage_of_victims(scored_df)  # Calculate the percentage of victims

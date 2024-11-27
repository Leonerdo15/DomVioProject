import pandas as pd
import numpy as np


"""
Types of violence: 
physical - 1
sexual - 2
economic - 3

no violance - 0
"""

"""
physical abuse characteristics:
-More likely to be women ✔️
-Between 30 and 39 years old ️✔️
-unemployed ✔️
-more them minimum wage ✔️
-at least 2 child ✔️
-married ✔️
"""



"""
sexual abuse characteristics:
-Women ✔️
-parents are together ✔️
-age doesn't matter ✔️
-Victims with mental or physical disabilities may be more vulnerable to abuse ✔️
-Individuals from minority groups or lower socio-economic statuses are at higher risk ❌
"""

"""
economic abuse characteristics:
-More likely to be women ✔️
-Often economically dependent on their partner ✔️
-Frequently experience restricted access to financial resources ❌
-More likely to have debts ✔️
"""


red_flags_physical = {
    "women": 0.15,
    "age": 0.15,
    "unemployed": 0.15,
    "minimum wage": 0.15,
    "children": 0.15,
    "married": 0.15
}

red_flags_sexual = {
    "women": 0.15,
    "parents together": 0.15,
    "mental disabilities": 0.15,
    "physical disabilities": 0.15
}

red_flags_economic = {
    "women": 0.15,
    "economically dependent": 0.15,
    "debt": 0.15
}



def generate_data(number_of_people):
    data = {
        "age": np.random.randint(16, 90, size=number_of_people),
        "women": np.random.choice([0, 1], size=number_of_people),
        "children": np.random.choice([0, 1, 2, 3], size=number_of_people),
        "unemployed": np.random.choice([0, 1], size=number_of_people, p=[0.8, 0.2]),
        "minimum wage": np.random.choice([0, 1], size=number_of_people, p=[0.6, 0.4]),
        "married": np.random.choice([0, 1], size=number_of_people),
        "parents together": np.random.choice([0, 1], size=number_of_people, p=[0.3, 0.7]),
        "mental disabilities": np.random.choice([0, 1], size=number_of_people,  p=[0.9, 0.1]),
        "physical disabilities": np.random.choice([0, 1], size=number_of_people, p=[0.9, 0.1]),
        "economically dependent": np.random.choice([0, 1], size=number_of_people),
        "debt": np.random.choice([0, 1], size=number_of_people, p=[0.85, 0.15]),
    }
    return pd.DataFrame(data)


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
    pass
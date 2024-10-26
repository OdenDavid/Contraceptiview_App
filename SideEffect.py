import pandas as pd
from collections import Counter

data = pd.read_csv("side_effects_data.csv")

age_groups = {
    "19-24": list(range(19, 25)),
    "25-34": list(range(25, 35)),
    "35-44": list(range(35, 45)),
    "13-18": list(range(13, 19)),
    "45-54": list(range(45, 55)),
    "55-64": list(range(55, 65)),
    "0-2": list(range(0, 3)),
    "7-12": list(range(7, 13))
}

def describe_age(age: int):
    """Descriptive analysis on the dataset based on a users age"""

    group = [key for key, list_ in age_groups.items() if age in list_] # Age group based on single age value

    side_effects = []
    filtered = data[data["Age"] == group[0]]
    dirty_side_effects = filtered["Sides"].to_list()

    for item in dirty_side_effects:
        for word in item.split(","):
            side_effects.append(word)

    string_counter = Counter(side_effects)
    most_common_side_effects = string_counter.most_common(10)
    top_10 = [string for string, count in most_common_side_effects] # Extract only the strings from the tuples
    top_side_effects = [i.replace("or","").strip() for i in top_10] # Remove trailing and preceeding white spaces

    # Filter our data by the most useful reviews
    sorted_reviews = filtered.nlargest(5, 'UsefulCount')
    sorted_reviews = sorted_reviews[["Reviews","Drug"]].reset_index().drop(columns=["index"])

    #respond = """Based on your age group {}, the most complained side effects are {}. \nHere are the top 5 most useful contraceptive reviews from people with your age group: \n""".format(group[0], top_side_effects)
    
    response = {
        "age_group" : group[0],
        "side_effects" : top_side_effects,
        "sorted_reviews" : {
            "Reviews" : sorted_reviews["Reviews"].to_list(),
            "Drugs" : sorted_reviews["Drug"].to_list()
        }
    }

    return response
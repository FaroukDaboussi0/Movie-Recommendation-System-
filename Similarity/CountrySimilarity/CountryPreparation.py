
import pickle
import pandas as pd
def calculate_country_similarity(movie_country, all_movies_countries, groups):
    # Find the group to which movie_country belongs
    movie_country_group = None
    for group_name, group_countries in groups.items():
        if movie_country in group_countries:
            movie_country_group = group_name
            break

    # If movie_country is not in any group, return an empty dictionary
    if movie_country_group is None:
        return {}

    similarity_scores = {movie_country_group: []}

    for other_movie_id, other_movie_country in all_movies_countries.items():
        score = 1 if other_movie_country in groups[movie_country_group] else 0
        similarity_scores[movie_country_group].append((other_movie_id, score))

    return similarity_scores



def read_movie_data(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Ensure the 'country' column is treated as strings
    df['country'] = df['country'].astype(str)

    # Create a dictionary to store movie data
    all_movies_countries = {}

    # Populate the dictionary with movie data
    for movie_id, row in df.iterrows():
        movie_id_str = f'{movie_id + 1}'  # Adjust the movie ID format as needed
        all_movies_countries[movie_id_str] = row['country']

    return all_movies_countries

# Example usage:
csv_file_path = '../../imdb_movies.csv'  # Replace with the actual path to your CSV file
all_movies_countries = read_movie_data(csv_file_path)

groups = {
    'group1': ['AU', 'US', 'GB', 'CA', 'BE', 'FR', 'DE', 'IT'],
    'group2': ['CL', 'MX', 'AR', 'CO'],
    'group3': ['NO', 'DK', 'FI', 'IS', 'SE'],
    'group4': ['KR', 'HK', 'UA', 'JP', 'ID', 'TH'],
    'group5': ['ES', 'RU', 'BR', 'TR'],
}
def save_data_to_file(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

# Save all_movies_countries to a file
all_movies_countries_file_path = 'all_movies_countries.pkl'
save_data_to_file(all_movies_countries, all_movies_countries_file_path)

# Save groups to a file
groups_file_path = 'groups.pkl'
save_data_to_file(groups, groups_file_path)


import pickle
import pandas as pd
all_movies_country_path = r'C:\MovieRecommandation\Similarity\CountrySimilarity\all_movies_countries.pkl'
groupspath = r'C:\MovieRecommandation\Similarity\CountrySimilarity\groups.pkl'
def load_data_from_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

# Load all_movies_countries 
all_movies_countries = load_data_from_file(all_movies_country_path)

# Load groups from Countries
groups = load_data_from_file(groupspath)

def similar_movies_base_country_score(movie_id):
    movie_country =all_movies_countries[movie_id]
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




similarity_scores = similar_movies_base_country_score("19")

#print(f"Movies similar to 19: {similarity_scores}")
def count_zeros(similarity_scores):
    zero_count = 0
    for group_name, scores in similarity_scores.items():
        for _, score in scores:
            if score == 0:
                zero_count += 1
    return zero_count
zero_count = count_zeros(similarity_scores)
print(f"Number of 0 scores: {zero_count}")
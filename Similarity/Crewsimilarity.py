import numpy as np
import pandas as pd
import pickle
movie_vector_path='C:\MovieRecommandation\Similarity\CrewSimilarity\movie_vectors.pkl'
def calculate_movie_similarity(movie_vector1, movie_vector2):
    # Initialize the final score
    final_score = 0

    # Create dictionaries for faster lookup
    vector1_dict = dict(movie_vector1)
    vector2_dict = dict(movie_vector2)

    # Iterate through the indices present in both vectors and calculate the similarity
    common_indices = set(vector1_dict.keys()) & set(vector2_dict.keys())
    for index in common_indices:
        score1 = vector1_dict[index]
        score2 = vector2_dict[index]
        final_score += score1 * score2

    return final_score

def similar_movies_base_actors_score(idmovie):
    # To load the movie_vectors from the file
    with open(movie_vector_path, 'rb') as file:
        loaded_movie_vectors = pickle.load(file)

    # Find the vector for the specified movie ID
    new_movie_vector = loaded_movie_vectors.get(idmovie, None)

    if new_movie_vector is not None:
        # Calculate similarity scores
        recommendations = []
        for movie, vector in loaded_movie_vectors.items():
            score = calculate_movie_similarity(new_movie_vector, vector)
            recommendations.append((movie, score))

        # Calculate the minimum and maximum scores
        min_score = min(recommendations, key=lambda x: x[1])[1]
        max_score = max(recommendations, key=lambda x: x[1])[1]

        # Normalize the similarity scores using Min-Max scaling
        normalized_recommendations = [(movie, (score - min_score) / (max_score - min_score)) for movie, score in recommendations]

        # Sort the normalized recommendations by score (descending order)
        normalized_recommendations.sort(key=lambda x: x[1], reverse=True)

        return normalized_recommendations

    else:
        print(f"Movie with ID {idmovie} not found.")
        return []

# Assuming idmovie is a string representing the movie ID
idmovie = "90"

# Get normalized recommendations for the specified movie ID
normalized_recommendations = similar_movies_base_actors_score(idmovie)

# Print the top 10 normalized recommendations
'''print("Normalized Recommendations:")
for movie_index, normalized_score in normalized_recommendations:
    print(f"Movie {movie_index}:  Score = {normalized_score}")'''

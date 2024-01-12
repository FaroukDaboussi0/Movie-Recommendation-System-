import pandas as pd
import pickle
movies_data_file_path = 'C:\MovieRecommandation\Similarity\GenreSimilarity\movies_genders.pkl'  # Replace with the actual path to your saved file
def load_data_from_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def similar_movies_base_genre_score(movie_id):
    all_movies = load_data_from_file(movies_data_file_path)
    # Get the genres of the input movie
    input_genres = set(all_movies[movie_id]['genres'])

    # Calculate Jaccard similarity with other movies
    similarity_scores = []
    for other_movie_id, other_movie_data in all_movies.items():
        if other_movie_id == movie_id:
            continue  # Skip comparing with itself

        other_genres = set(other_movie_data['genres'])

        intersection_size = len(input_genres.intersection(other_genres))
        union_size = len(input_genres.union(other_genres))

        # Avoid division by zero
        similarity_score = intersection_size / union_size if union_size != 0 else 0.0

        similarity_scores.append((other_movie_id, similarity_score))

    # Sort the results by similarity score in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    return similarity_scores

movies_data_file_path = 'C:\MovieRecommandation\Similarity\GenreSimilarity\movies_genders.pkl'  # Replace with the actual path to your saved file
'''
input_movie_id = '1'
similarities = similar_movies_base_genre_score(input_movie_id)
print(f"Movies similar to movie {input_movie_id}: {similarities}")
'''

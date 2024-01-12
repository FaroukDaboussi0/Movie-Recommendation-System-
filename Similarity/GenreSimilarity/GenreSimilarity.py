import pandas as pd
import pickle
def save_data_to_file(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
def calculate_genre_similarity(movie_id, all_movies):
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

def clean_and_extract_genres(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Ensure the 'genre' column is treated as strings
    df['genre'] = df['genre'].astype(str)

    # Clean and extract genres
    df['genres'] = df['genre'].apply(lambda x: [genre.strip() for genre in x.split(',')])

    # Create a dictionary to store movie data
    all_movies_data = {}

    # Populate the dictionary with movie data
    for movie_id, row in df.iterrows():
        all_movies_data[str(movie_id)] = {'genres': row['genres']}

    return all_movies_data

# Example usage:
csv_file_path = '../imdb_movies.csv'  # Replace with the actual path to your CSV file
movies_data = clean_and_extract_genres(csv_file_path)
# Save movies_data to a file
movies_data_file_path = 'movies_genders.pkl'
save_data_to_file(movies_data, movies_data_file_path)
input_movie_id = '1'
similarities = calculate_genre_similarity(input_movie_id, movies_data)
print(f"Movies similar to movie {input_movie_id}: {similarities}")


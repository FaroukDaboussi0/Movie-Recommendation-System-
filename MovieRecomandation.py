from cmath import log
from Similarity.CountrySimilarity import similar_movies_base_country_score
from Similarity.Crewsimilarity import similar_movies_base_actors_score
from Similarity.DescriptionSimilarity import similar_movies_base_description_score
from Similarity.GenreSimilarity import similar_movies_base_genre_score
import random
trainintime = 50
average_actors_scores=[]
average_country_scores =[]
average_genre_scores = []
average_description_scores = []
min_movies = 2
max_movies = 100

for i in range( trainintime) :
    # Define the number of watched movies
    num_watched_movies = random.randint(min_movies, max_movies)
    print(i)
    # Generate random movie IDs and scores
    watched_movies = [(str(random.randint(0, 10000)), random.uniform(0.5, 1)) for _ in range(num_watched_movies)]

    '''# Print the generated list
    print("Generated Watched Movies:")
    print(watched_movies)'''
    # Initialize dictionaries to store similarity scores for each dimension
    description_dict = {}
    genre_dict = {}
    actors_dict = {}
    country_dict = {}


    # Call each similarity function to get the list of similar movies for each dimension
    for movie_id, importance in watched_movies:
        description_similarity = similar_movies_base_description_score(movie_id)
        genre_similarity = similar_movies_base_genre_score(movie_id)
        actors_similarity = similar_movies_base_actors_score(movie_id)
        country_similarity = similar_movies_base_country_score(movie_id)

        # Store the similarity scores in the dictionaries
        description_dict[movie_id] = dict(description_similarity)
        genre_dict[movie_id] = dict(genre_similarity)
        actors_dict[movie_id] = dict(actors_similarity)
        country_dict[movie_id] = dict(country_similarity)

    # Initialize variables to store the total scores for each dimension
    total_description_score = 0
    total_genre_score = 0
    total_actors_score = 0
    total_country_score = 0

    # Iterate through watched_movies
    for i in range(len(watched_movies)):
        movie_id_i , importance_i = watched_movies[i]

        # Accumulate scores for each dimension
        for j in range(len(watched_movies)):
            if i != j:  # Exclude self-comparison
                movie_id_j ,imporatce_j  = watched_movies[j]

                # Accumulate scores for each dimension
                total_description_score += description_dict[movie_id_i].get(int(movie_id_j), 0)*importance_i
                total_genre_score += genre_dict[movie_id_i].get(movie_id_j, 0)*importance_i
                total_actors_score += actors_dict[movie_id_i].get(movie_id_j, 0)*importance_i
                total_country_score += country_dict[movie_id_i].get(int(movie_id_j), 1)*importance_i

    # Calculate the average scores for each dimension
    num_pairs = len(watched_movies) * (len(watched_movies) - 1)
    average_description_score = total_description_score / num_pairs
    average_genre_score = total_genre_score / num_pairs
    average_actors_score = total_actors_score / num_pairs
    average_country_score = total_country_score / num_pairs
    average_actors_scores.append(average_genre_score)
    average_country_scores.append(average_actors_score)
    average_description_scores.append(average_description_score)
    average_genre_scores.append(average_genre_score)
    

# Print the final average scores for each dimension
print("Average Description Score:", min(average_description_scores),max(average_description_scores))
print("Average Genre Score:", min(average_genre_scores),max(average_genre_scores))
print("Average Actors Score:", min(average_actors_scores),max(average_actors_scores))
print("Average Country Score:", min(average_country_scores),max(average_country_scores))



#-----------------------------------------------
# Initialize a list to store the combined similarity scores
'''
            combined_scores = []
def calculate_average_similarity(watched_movies, weights):
    # Initialize dictionaries to store similarity scores for each dimension
    genre_dict = {}
    description_dict = {}
    actors_dict = {}
    country_dict = {}

    # Call each similarity function to get the list of similar movies for each dimension
    for movie_id in watched_movies:
        genre_similarity = similar_movies_base_genre_score(movie_id)
        description_similarity = similar_movies_base_description_score(movie_id)
        actors_similarity = similar_movies_base_actors_score(movie_id)
        country_similarity = similar_movies_base_country_score(movie_id)

        # Store the similarity scores in the dictionaries
        genre_dict[movie_id] = dict(genre_similarity)
        description_dict[movie_id] = dict(description_similarity)
        actors_dict[movie_id] = dict(actors_similarity)
        country_dict[movie_id] = dict(country_similarity)

    # Initialize a list to store the combined similarity scores
    combined_scores = []

    # Iterate through the watched movies
    for watched_movie_id in watched_movies:
        # Calculate the average similarity for each dimension
        avg_genre_similarity = sum(genre_dict[watched_movie_id].values()) / len(genre_dict[watched_movie_id])
        avg_description_similarity = sum(description_dict[watched_movie_id].values()) / len(description_dict[watched_movie_id])
        avg_actors_similarity = sum(actors_dict[watched_movie_id].values()) / len(actors_dict[watched_movie_id])
        avg_country_similarity = sum(country_dict[watched_movie_id].values()) / len(country_dict[watched_movie_id])

        # Combine the similarity scores based on weights
        combined_score = (
            watched_movie_id,
            weights['genre'] * avg_genre_similarity +
            weights['description'] * avg_description_similarity +
            weights['actors'] * avg_actors_similarity +
            weights['country'] * avg_country_similarity
        )

        combined_scores.append(combined_score)

    return combined_scores

# Example usage:
watched_movies = ['4', '6', '40']  # Replace with the list of watched movie IDs
weights = {'genre': 0.4, 'description': 0.3, 'actors': 0.2, 'country': 0.1}  # Replace with the weights for each dimension

combined_scores = calculate_average_similarity(watched_movies, weights)
print("Combined Similarity Scores:")
for movie_id, score in combined_scores:
    print(f"Movie {movie_id}: Combined Similarity Score = {score}")
'''
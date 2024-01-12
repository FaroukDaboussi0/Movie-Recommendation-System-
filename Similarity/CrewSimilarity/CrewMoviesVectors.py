import pandas as pd

def read_movie_data(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Ensure the 'crew' column is treated as strings
    df['crew'] = df['crew'].astype(str)

    # Create a dictionary to store movie data
    all_movies_crews = {}

    # Populate the dictionary with movie data
    for movie_id, row in df.iterrows():
        movie_id_str = f'{movie_id + 1}'  # Adjust the movie ID format as needed

        # Split crew members into a list of actors
        crew_list = [member.strip() for member in row['crew'].split(',')]
        
        # Update the dictionary with movie crew data
        all_movies_crews[movie_id_str] = crew_list

    return all_movies_crews

# Create a dictionary of all actors with unique index
csv_file_path = 'C:\MovieRecommandation\imdb_movies.csv'  # Replace with the actual path to your CSV file
all_movies_crews = read_movie_data(csv_file_path)

# Create a set to store all unique actors
all_actors_set = set()

# Iterate through movies and crew to update the set of all actors
for movie, crew_list in all_movies_crews.items():
    for actor in crew_list:
        # Add the actor to the set
        all_actors_set.add(actor)
        
        
        

# Convert the set of all actors to a dictionary with unique indices
all_actors_dict = {index: actor for index, actor in enumerate(all_actors_set)}

# Create a function to find the index of an actor in the dictionary
def find_index_by_actor_name(actor_name):
    for index, actor in all_actors_dict.items():
        if actor == actor_name:
            return index
    return None  # Return None if the actor is not found

# Generate vectors for each movie based on actor importance scores

movie_vectors = {}
for movie, crew_list in all_movies_crews.items():
    # Initialize the vector with zeros
    movie_vector = [(find_index_by_actor_name(actor), 0) for actor in crew_list]

    # Update the vector with actor importance scores
    for actor_index, actor in enumerate(crew_list):
        if actor_index < len(movie_vector):
            # Update the score in the vector
            actor_importance = 1 / (actor_index + 1)
            movie_vector[actor_index] = (find_index_by_actor_name(actor), actor_importance)

    # Store the movie vector in the dictionary
    movie_vectors[movie] = movie_vector

# Print the resulting movie vectors
for movie, vector in movie_vectors.items():
    print(f"Movie {movie} Vector: {vector}")


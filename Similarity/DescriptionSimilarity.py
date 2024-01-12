from gensim.models import Doc2Vec

# Assuming you have loaded your model
model = Doc2Vec.load("C:\MovieRecommandation\Similarity\DescriptionSimilarity\doc2vec_model")

def similar_movies_base_description_score(movie_index):
    try:
        # Infer vector for the given movie index
        query_vector = model.dv[str(int(movie_index) - 1)]

        # Find most similar documents to the query vector
        similar_documents = model.dv.most_similar([query_vector], topn=len(model.dv))

        # Extract movie indexes and similarity scores from the results
        similar_movie_info = [(int(movie_tag) + 1, similarity_score) for movie_tag, similarity_score in similar_documents]

        return similar_movie_info
    except KeyError:
        print(f"Movie with index {movie_index} not found.")
        return []

# Example: Get similarity scores for all movies based on movie with index 10
#movie_index_to_search = '10'
#all_similar_movies = similar_movies_base_description_score(movie_index_to_search)

#print(f"Similarity scores for all movies based on movie {movie_index_to_search}: {all_similar_movies}")

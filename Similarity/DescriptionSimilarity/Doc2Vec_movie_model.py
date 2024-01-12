import pandas as pd
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
csv_file_path = 'C:\MovieRecommandation\imdb_movies.csv' 
# Load your CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Create a new DataFrame with only the "overview" column
overviews_df = df[["overview"]]
print(overviews_df)
# Filter rows where "overview" is not null and is a string or list of words
filtered_overviews_df = overviews_df[overviews_df["overview"].apply(lambda x: isinstance(x, str) or (isinstance(x, list) and all(isinstance(word, str) for word in x)))]

# Preprocess and tag documents with an ID sequence
tagged_data = [TaggedDocument(words=str(overview).lower().split(), tags=[str(i)]) for i, overview in enumerate(filtered_overviews_df["overview"])]

# Initialize and train the Doc2Vec model
model = Doc2Vec(vector_size=100, window=5, min_count=1, workers=4, epochs=10)
model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

# Save the trained model to a file
model.save("doc2vec_model")

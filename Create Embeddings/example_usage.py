from create_embed import get_embeddings

get_embeddings(
    data_csv_path="path to your CSV file",
    embeddings_file_name="new_embeddings.csv",
    env_path="path to your .env file"
)

"""
Call above creates a CSV file named "new_embeddings.csv" and 
with a structure like this:
index;embedding
"""
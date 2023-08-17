# How to use
```
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
```

Your CSV file structure must be of the form:

`index;header;description;content;...`

Don't forget to do

`pip install -r requirements.txt`

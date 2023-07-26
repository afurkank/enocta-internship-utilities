import os
import openai
import csv
import tiktoken
from dotenv import load_dotenv, find_dotenv

MAX_NUM_TOKENS = 16000

def get_embeddings(
        data_csv_path: str,
        embeddings_file_name: str,
        env_path: str
    ) -> None:

    """
    This functions takes a CSV file and creates a CSV file containing embeddings.

    If the data does not have any description, the content is used for 
    the embeddings. If the content is not given, then the header is used for the 
    embeddings(assuming all data have headers.)

    data_csv_path: Path to the CSV file containing data. The format must be \
    like this: index;header;description;content;...

    embeddings_file_name: Name for the .csv file which will store the created embeddings.

    environment_path: Path to the .env file containing the 'OPENAI_API_KEY'.
    """

    _ = load_dotenv(find_dotenv(filename=env_path))

    openai.api_key = os.environ['OPENAI_API_KEY']
    
    # Get CSV rows as elements of a list
    data_list = read_csv_file(data_csv_path)

    embeddings = []

    # Loop over the data
    for row in data_list:
        header = row[1]
        desc = row[2]
        content = row[3]
        if desc=='':
            if content=='':
                # If both description and content is empty, use header
                embeddings.append(get_embedding(header))
            else:
                # If there is content, use content
                embeddings.append(get_embedding(get_summary(get_prompt(content))))
        else:
            # If there is description, use description
            embeddings.append((get_embedding(desc)))

    # Create a CSV file containing the embeddings
    embeds = [{"index": i+1, "embedding": embedding} for i, embedding in enumerate(embeddings)]
    with open(embeddings_file_name, mode='w', newline='', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=["index", "embedding"], delimiter=";")
        writer.writeheader()
        writer.writerows(embeds)

def get_embedding(string_to_embed: str) -> list[float]:
    # Replace new lines with a space
    string_to_embed = string_to_embed.replace("\n", " ")

    # Get embedding array
    embedding = openai.Embedding.create(input=string_to_embed, model="text-embedding-ada-002")['data'][0]['embedding']

    # Return embeddings
    return embedding

def get_summary(content_to_summarize: str) -> str:
    # Get prompt to summarize text
    prompt = get_prompt(content_to_summarize)

    # Get number of tokens of the prompt
    enc = tiktoken.encoding_for_model(model_name="gpt-3.5-turbo")
    tokenized_prompt = enc.encode(prompt)
    num_of_tokens = len(tokenized_prompt)

    # Check if it exceeds max num of tokens for the model
    if(num_of_tokens > MAX_NUM_TOKENS):
        tokenized_prompt = tokenized_prompt[:MAX_NUM_TOKENS]
    
    # Get summary of the content
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=[{"role": "user", "content": prompt}])

    # Return summary
    return chat_completion["choices"][0]["message"]["content"]

def get_prompt(text_to_prompt: str) -> str:
    prompt = f"""
    Aşağıda bir eğitim programının içeriğine dair bilgi verilmiş.
    Maksimum 3 cümlede bu içeriği özetleyebilir misin?
    İçerik bu:
    {text_to_prompt}
    """
    return prompt

def read_csv_file(file_path):
    data_list = []

    with open(file_path, 'r', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            data_list.append(row)

    return data_list[1:]
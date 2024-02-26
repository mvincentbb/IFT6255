import json
import requests

# Solr URL settings
solr_url = 'http://localhost:8983/solr'
core_name = 'dirichlet_core'
headers = {'Content-type': 'application/json'}

# Path to your JSON file containing the documents to index
json_file_path = '/Users/vincent/Downloads/solr-9.5.0/FICHIERS_TESTS/solr_documents.json'

def index_documents(solr_url, core_name, json_file_path):
    update_url = f'{solr_url}/{core_name}/update/json/docs?commit=true'
    
    # Load documents from the JSON file
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            documents = json.load(file)
    except UnicodeDecodeError as e:
        print(f"Error reading the JSON file: {e}")
        return
    
    # Post documents to Solr
    try:
        response = requests.post(update_url, json=documents, headers=headers)
        # response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Documents indexed successfully. Response: {response.text}")
    except requests.RequestException as e:
        print(f"Error posting documents to Solr: {e}")
        print(response.text)

if __name__ == "__main__":
    index_documents(solr_url, core_name, json_file_path)

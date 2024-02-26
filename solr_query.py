# import requests
# import re
# import json

# # Define the path to the topics file
# topics_file_path = '/Users/vincent/Downloads/solr-9.5.0/FICHIERS_TESTS/topics.1-50.txt'

# # Solr settings
# solr_url = 'http://localhost:8983/solr'
# core_name = 'testcore'

# # Function to read topics from file and extract titles
# def extract_titles(file_path):
#     titles = []
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         # Regular expression to find titles
#         matches = re.findall(r'<title>\s*Topic:\s*(.*?)\s*</title>', content, re.DOTALL)
#         titles.extend(matches)
#     return titles

# # Function to query Solr
# def query_solr(query):
#     url = f"{solr_url}/{core_name}/select"
#     params = {
#         'q': f"title:\"{query}\"",
#         'wt': 'json',
#         'indent': 'true',
#         'rows': 1000 # Limit to 5 results per query for demonstration
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# # Extract titles from the topics file
# titles = extract_titles(topics_file_path)

# # Query Solr using extracted titles and print results
# for title in titles:
#     results = query_solr(title)
#     if results and results['response']['numFound'] > 0:
#         print(f"Query: {title}")
#         print(f"Found {results['response']['numFound']} documents")
#         for doc in results['response']['docs']:
#             print(f" - Document ID: {doc['id']}, Score: {doc.get('score', 'No Score')}")
#         print("\n")
#     else:
#         print(f"Query: {title}")
#         print("No documents found.\n")
import requests
import json

# Load queries from your JSON file
json_file_path = 'test.json'  # Update with the actual path

# Solr settings
solr_url = 'http://localhost:8983/solr'
core_name = 'anothercore'  # Update with your actual core name

# Function to load queries from JSON
def load_queries(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to query Solr
def query_solr(query_text):
    url = f"{solr_url}/{core_name}/select"
    params = {'q': f'text:"{query_text}"', 'wt': 'json'}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None

# Main execution
if __name__ == "__main__":
    queries = load_queries(json_file_path)
    for query in queries:
        title = query.get('title')
        print(f"Querying Solr with text: {title}")
        results = query_solr(title)
        if results and results['response']['numFound'] > 0:
            # print(f"Found {results['response']['numFound']} documents for '{title}'\n")
            print(f"Found {results} documents for '{title}'\n")
        else:
            print(f"No results found for '{title}'\n")

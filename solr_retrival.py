# Since there was an issue loading and displaying the content directly, let's proceed with the script to handle multiple queries.
# # This script assumes the JSON file has a structure similar to what was previously discussed.

# import requests
# import json

# # Function to load queries from the JSON file
# def load_queries(json_file_path):
#     with open(json_file_path, 'r') as file:
#         queries = json.load(file)
#     return queries

# # Function to query Solr and print results in TREC format
# def query_solr_and_print_trec(queries, solr_url, core_name):
#     for query in queries:
#         query_text = query.get('title')  # Assuming each query has a 'title' field
#         query_id = query.get('number')  # Assuming each query has a 'number' field as queryID
#         params = {
#             'q': f'text:"{query_text}"',  # Adjust field name if necessary
#             'wt': 'json',
#             # 'rows': 1000,
#             'fl': 'id,score'  # Adjust number of rows as needed
#         }
#         response = requests.get(f'{solr_url}/{core_name}/select', params=params)
#         if response.status_code == 200:
#             data = response.json()
#             for rank, doc in enumerate(data['response']['docs'], start=1):
#                 doc_id = doc['id']
#                 score = doc.get('score', 0)
#                 print(f'{query_id} Q0 {doc_id} {rank} {score} BM25')  # RunID is set as 'BM25' for example
#         else:
#             print(f"Failed to query Solr with: {query_text}")

# # Path to the JSON file with queries
# json_file_path = '/Users/vincent/Downloads/solr-9.5.0/FICHIERS_TESTS/topics_converted.1-50.json'  # Update with the correct file path

# # Load queries from the JSON file
# queries = load_queries(json_file_path)

# # Solr settings - update these to match your Solr instance
# solr_url = 'http://localhost:8983/solr'
# core_name = 'anothercore'  # Update with your actual core name

# # Execute queries and print results in TREC format
# query_solr_and_print_trec(queries, solr_url, core_name)



# # import requests
# import json
# import time  # Import time module

# # Function to load queries from the JSON file
# def load_queries(json_file_path):
#     with open(json_file_path, 'r') as file:
#         queries = json.load(file)
#     return queries

# # Function to query Solr and print results in TREC format, including query time
# def query_solr_and_print_trec(queries, solr_url, core_name):
#     for query in queries:
#         query_text = query.get('title')  # Assuming each query has a 'title' field
#         query_id = query.get('number')  # Assuming each query has a 'number' field as queryID
#         params = {
#             'q': f'text:"{query_text}"',  # Adjust field name if necessary
#             'wt': 'json',
#             'rows': 1000,  # Adjust number of rows as needed
#             'fl': 'id,score'
#         }

#         # Start measuring time
#         start_time = time.time()

#         # Perform the query
#         response = requests.get(f'{solr_url}/{core_name}/select', params=params)
        
#         # Calculate elapsed time
#         elapsed_time = time.time() - start_time

#         if response.status_code == 200:
#             data = response.json()
#             for rank, doc in enumerate(data['response']['docs'], start=1):
#                 doc_id = doc['id']
#                 score = doc.get('score', 0)
#                 # Print results including query time
#                 print(f'{query_id} Q0 {doc_id} {rank} {score} BM25 QueryTime={elapsed_time:.2f}s')
#         else:
#             print(f"Failed to query Solr with: {query_text}")

# # Specify the path to your JSON file with queries and update Solr settings
# json_file_path = '/Users/vincent/Downloads/solr-9.5.0/FICHIERS_TESTS/topics_converted.1-50.json'  # Update with the correct file path
# solr_url = 'http://localhost:8983/solr'
# core_name = 'tfcore'  # Update with your actual core name

# Load queries and execute them
# queries = load_queries(json_file_path)
# query_solr_and_print_trec(queries, solr_url, core_name)



import requests
import json

# Function to load queries from the JSON file
def load_queries(json_file_path):
    with open(json_file_path, 'r') as file:
        queries = json.load(file)
    return queries

# Function to query Solr, print results in TREC format, and sum query times
def query_solr_sum_query_times(queries, solr_url, core_name):
    total_query_time = 0  # Initialize the total query time accumulator

    for query in queries:
        query_text = query.get('title')  # Assuming each query has a 'title' field
        query_id = query.get('number')  # Assuming each query has a 'number' field as queryID
        params = {
            'q': f'text:"{query_text}"',  # Adjust field name if necessary
            'wt': 'json',
            'rows': 1000,  # Adjust number of rows as needed
            'fl': 'id'
        }
        response = requests.get(f'{solr_url}/{core_name}/select', params=params)
        if response.status_code == 200:
            
            data = response.json()
            query_time = data['responseHeader']['QTime']  # Get the query time for this query
            total_query_time += query_time  # Accumulate the total query time
            for rank, doc in enumerate(data['response']['docs'], start=1):
                doc_id = doc['id']
                score = doc.get('score', 0)
                print(f'{query_id} Q0 {doc_id} {rank} {score} DIRICHLET')  # RunID is set as 'BM25' for example
        else:
            print(f"Failed to query Solr with: {query_text}")

    # print(f"Total query time for all queries: {total_query_time} milliseconds")

# Example usage
json_file_path = '/Users/vincent/Downloads/solr-9.5.0/FICHIERS_TESTS/topics_converted.51-100.json'  # Update with the correct file path
solr_url = 'http://localhost:8983/solr'
# core_name = 'anothercore'  # Update with your actual core name
core_name = 'tfcore'  # Update with your actual core name

queries = load_queries(json_file_path)  # Load queries from the JSON file

# Execute queries and sum the query times
query_solr_sum_query_times(queries, solr_url, core_name)
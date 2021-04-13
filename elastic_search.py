import requests
from pprint import pprint
import json

class ElasticSearchAPI():
    def __init__(self, url):
        self.base_url = url
        self.cluster = self.cluster_health()
        print(self)
        print('-'*30)

    def __repr__(self):
        return f"Elasticsearch instance running at {self.base_url} on {self.cluster['cluster_name']}"

    # Generic requests methods
    def _get_request(self, url, params=None):
        response = requests.get(url, params = params)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print('Bad request! Error hitting URL: ', url)
            print('Error message: ', response.json()) #['error']['message'])
            return response.json()
    
    def _post_request(self, url, json=None):
        response = requests.post(url, json=json)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print('Bad request! Error hitting URL: ', url)
            print('Error message: ', response.json())
            return response.json()

    # ES methods
    def cluster_health(self):
        cluster_url = self.base_url + '/_cluster/health?pretty'
        response = self._get_request(cluster_url)
        assert response['timed_out'] == False, 'Cluster has timed out'
        return response

    def index_stats(self):
        index_url = self.base_url + '/_stats'
        response = self._get_request(index_url)
        self.indices = list(response['indices'].keys())
        print('Indices: ', self.indices)
        print('-'*30)
        return response

    def count_documents(self, index=None, search_q=None):
        search_str = '?q=' + search_q if search_q != None else ''
        index = index+ '/' if index != None else ''
        count_url = f"{self.base_url}/{index}/_count" + search_str
        response = self._get_request(count_url)
        print('Document count: ', response['count'])
        print('-'*30)
        self.document_count = response['count']
        return response

    def search(self, key, query, index=None):
        # TODO: improve defualts for key etc
        # all_keys = ['acno', 'acquisitionYear', 'all_artists', 'creditLine', 'medium', 'title', 'thumbnailUrl', 'thumbnailCopyright', 'url']
        print(f'Searching {key} for {query}...')
        index = index+ '/' if index != None else ''
        search_url = f"{self.base_url}/{index}_search"
        q_str = {
                  "query": {
                    "match": {
                      key: {
                        "query": query,
                        "fuzziness": "AUTO"
                      }
                    }
                  }
                }
        # Docs say this should be a get request but for some reason only post works 
        response = self._post_request(search_url, q_str)
        titles = [hit['_source']['title'] for hit in response['hits']['hits']]
        print(f'Found artworks:')
        print(*['   ' + t for t in titles], sep='\n')
        print('-'*30)
        return response

# Testing 
ESClient = ElasticSearchAPI('http://localhost:9200')
ESClient.index_stats()
ESClient.count_documents('artwork')
ESClient.search("all_artists", "Turner")
# Running with fuzzy AUTO picks up from mispelt version!
ESClient.search("all_artists", "Turnr")
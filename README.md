# WIP - elasticsearch with art info
Playing around with elasticsearch using Docker to set up and artwork info to load and run searches on

## Approach
### 1. Container
Using a Docker container to run elasticsearch as linked: <br>
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

### 2. Data Prep
Used Tate data from linked repo: <br>
https://github.com/tategallery/collection
<br>
Filtered for only clean, easy to use keys for testing by running create_json.py which creates artwork.json 

### 3. Data Load 
Ran Bulk load API form upload_artwork.sh

### 4. Elasticsearch API calls
Test out in elastic_search.py

### TODO
- Load artists as well & index better
- Properly check what the format needs to be for the bulk load API 
- Make searching on artwork strings more flexible
- Mock the API to unit test?
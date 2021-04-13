# Bulk import API docs:
# https://www.elastic.co/guide/en/elasticsearch/reference/7.12/docs-bulk.html

# General useful commands
# https://markheath.net/post/exploring-elasticsearch-with-docker

# Run to check cluster health
# curl http://localhost:9200/_cluster/health?pretty
# Returns:
# {
#   "cluster_name" : "docker-cluster",
#   "status" : "yellow",
#   "timed_out" : false,
#   "number_of_nodes" : 1,
#   "number_of_data_nodes" : 1,       
#   "active_primary_shards" : 1,      
#   "active_shards" : 1,
#   "relocating_shards" : 0,
#   "initializing_shards" : 0,
#   "unassigned_shards" : 1,
#   "delayed_unassigned_shards" : 0,
#   "number_of_pending_tasks" : 0,
#   "number_of_in_flight_fetch" : 0,
#   "task_max_waiting_in_queue_millis" : 0,
#   "active_shards_percent_as_number" : 50.0
# }

# Create an index for artworks
# curl -X PUT "localhost:9200/artwork?pretty"
# Returns:
# {
#   "acknowledged" : true,       
#   "shards_acknowledged" : true,
#   "index" : "artwork"
# }

# List indexes to check it worked
# curl -X GET http://localhost:9200/_cat/indices?v

# Bulk load command - worked for some but lots had "error" : {
#           "type" : "mapper_parsing_exception",
#           "reason" : "failed to parse",
#           "caused_by" : {
#             "type" : "json_parse_exception",
# curl -H "Content-Type: application/json" -XPOST "localhost:9200/artwork/_bulk?pretty&refresh" --data-binary "@artwork.json"
# curl "localhost:9200/_cat/indices?v=true"

# Count number of records in the index
# Bulk uploaded 34k in 5 mins
# curl -X GET "localhost:9200/_cat/count/artwork?v"

# Search
# curl -XGET "localhost:9200/artwork/_search?q=blake" 
#-q {"all_artists": "William Blake"}
# curl -XGET --header 'Content-Type: application/json' http://localhost:9200/artwork/_search -d '{"query" : { "match" : {"all_artists": "William Blake"} }}'
# curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'

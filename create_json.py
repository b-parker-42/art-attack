import glob
import json

# Code to turn the artworks files into one file of the required format to load into elasticsearch using the Bulk API
all_artworks_paths = glob.glob('./artworks/*/*/*.json')
json_file = open('artwork.json', 'a')

req_keys = ['acno', 'acquisitionYear', 'all_artists', 'creditLine', 'medium', 'title', 'thumbnailUrl', 'thumbnailCopyright', 'url']
for artwork_path in all_artworks_paths:
    
    idx_line = '{\"index\":{\"_index\":\"artwork\"}}'
    
    json_file.write(idx_line)
    json_file.write("\n")

    with open(artwork_path) as f:
        art_dict = json.load(f)
        final_dict = {ky : art_dict[ky] for ky in req_keys}
        # artwork_line = str(json.load(f)).replace('\'','"')
        artwork_line = str(final_dict).replace('\'','"').replace('None', '"null"')
        json_file.write(artwork_line)
        json_file.write("\n")

json_file.close()
print('Created json file to upload')
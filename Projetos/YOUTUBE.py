from googleapiclient.discovery import build
import pandas as pd
from IPython.display import JSON
api_key = 'AIzaSyBZoFWFyRMnpR6eD0sen4--nQOJWi0O_Z4'

channel_ids = ['UCUFFHXvzAMRSD8Bq4bJppxQ', 'UCoOae5nYA7VqaXzerajD0lg']


api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client

youtube = build(
    api_service_name, api_version, developerKey=api_key)

request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id=",".join(channel_ids)
    
)
response = request.execute()

JSON(response)
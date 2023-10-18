import xml.etree.ElementTree as ET
import pandas as pd

# Load and parse the XML file
tree = ET.parse('datasets/vocapia/0a40d83a-1353-4f34-9889-c0f591e4d8f7/0ca0d6c6-cd60-43c3-88ad-202ffbac83ee/transcript.xml')
root = tree.getroot()

# Find the SegmentList element
segment_list = root.find('.//SegmentList')

# Create an empty list to hold the subtitle data
subtitles = []

# Iterate through the SpeechSegment elements
for speech_segment in segment_list.findall('SpeechSegment'):
    speaker_id = speech_segment.get('spkid')
    sentence_start_time = speech_segment.get('stime')
    
    # Initialize an empty sentence and its start time
    sentence = ''
    
    # Iterate through the Word elements
    for word in speech_segment.findall('Word'):
        word_text = word.text.strip()
        word_end_time = float(word.get('stime')) + float(word.get('dur'))
        
        # Append the word to the current sentence
        sentence += word_text + ' '
        
        # Check for sentence-ending punctuation
        if word_text.endswith(('.', '!', '?')):
            # Remove extra spaces around punctuation
            sentence = sentence.replace(" .", ".").replace(" ,", ",").replace(" ?", "?").replace(" !", "!").replace("' ", "'").strip()
            
            # Create a dictionary with the subtitle data
            subtitle_data = {
                'Speaker ID': speaker_id,
                'Start Time': sentence_start_time,
                'End Time': word_end_time,
                'Transcript': sentence
            }
            
            # Append the subtitle data to the subtitles list
            subtitles.append(subtitle_data)
            
            # Reset the sentence and update the sentence start time
            sentence = ''
            sentence_start_time = word_end_time

# Convert the subtitles list to a DataFrame
df = pd.DataFrame(subtitles)

# Print the DataFrame to view the data
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('subtitles.csv', index=False)

# ! other stuff we tried

# import config
# from gql import Client, gql
# from gql.transport.requests import RequestsHTTPTransport
# import pandas as pd

# # Set up the GraphQL client
# transport = RequestsHTTPTransport(
#     url='https://openapi.radiofrance.fr/v1/graphql',
#     headers={
#         "x-token": config.X_TOKEN,
#     },
#     use_json=True,
# )

# client = Client(
#     transport=transport,
#     fetch_schema_from_transport=True,
# )

# # Define the new GraphQL query
# query = gql("""
# {
#   showByUrl(
#     url: "https://www.radiofrance.fr/franceculture/podcasts/fictions-theatre-et-cie"
#   ) {
#     id
    
#     diffusionsConnection {
#       edges {
#         node {
#           transcript {
#             segments {
#               start
#               text
#               type
#             }
#           }
#         }
#       }
#     }
#   }
# }
# """)

# # Execute the query
# response = client.execute(query)

# # Print the response
# # print(response)

# # Assuming the variable `response` holds the data you received from the GraphQL query
# data = response['showByUrl']['diffusionsConnection']['edges'][0]['node']['transcript']['segments']

# # Convert the data to a DataFrame
# df = pd.DataFrame(data)

# # Print the DataFrame to view the data
# print(df)

# df.to_csv('test.csv', index=False)

# import pathlib as p
# import json
# import pandas as pd

# # Adjust the path to match the location of your whisper.csv file
# df = pd.read_csv(
#     p.Path("datasets") / "whisper.csv",
#     index_col="magnetothequeId",
#     nrows=300
# )

# def extract_transcript(json_string: str) -> str:
#     return "".join(s["text"] for s in json.loads(json_string))

# # Filter the DataFrame for the row with the specified ID
# selected_row = df.loc['2023F10488S0073']

# # Extract the transcript for the selected ID
# transcript = extract_transcript(selected_row['segments'])

# # Print the transcript
# print(transcript)

# import pathlib as p
# import json
# import pandas as pd

# # Adjust the path to match the location of your whisper.csv file
# df = pd.read_csv(
#     p.Path("datasets") / "whisper.csv",
#     index_col="magnetothequeId",
#     nrows=300
# )

# # Print the first three lines of the CSV file
# print(df.head(3))

# import pathlib as p
# import pandas as pd

# # Adjust the path to match the location of your whisper.csv file
# df = pd.read_csv(
#     p.Path("datasets") / "whisper.csv",
#     index_col="magnetothequeId",
#     # nrows=300  # You may need to remove this line if the desired ID is not within the first 300 rows
# )

# # Find the row with the specified magnetothequeId
# selected_row = df.loc['2022F45396S0023']

# # Print the selected row
# print(selected_row)

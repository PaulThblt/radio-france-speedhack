import config
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

# Set up the GraphQL client
transport = RequestsHTTPTransport(
    url='https://openapi.radiofrance.fr/v1/graphql',
    headers={
        "x-token": config.X_TOKEN,
    },
    use_json=True,
)

client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

# Define the GraphQL query
query = gql("""
    {
        brands {
            title
        }
    }
""")

# Execute the query
response = client.execute(query)

# Print the response
print(response)

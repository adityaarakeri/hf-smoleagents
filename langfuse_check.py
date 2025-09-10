import os
from langfuse import get_client

langfuse = get_client()  # Initialize the Langfuse client

# verify connection
if langfuse.auth_check():
    print("Langfuse connection is authenticated and ready!")
else:
    print(
        "Langfuse connection failed. Please check your API keys and network connection."
    )

import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# Ensure your API key is set as an environment variable named TAVILY_API_KEY
# If not set, you can pass it directly: tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

query = "Who is the CEO of LTIMindtree in 2025?"

# Execute a basic search query
response = tavily_client.search(query)

# Print the full response (which is a dictionary)
print(response)

# To get a direct answer, use the qna_search method
# answer = tavily_client.qna_search(query)
# print(answer)

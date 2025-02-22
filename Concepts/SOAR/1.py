import requests
import pandas as Pd 
url = "https://dummyjson.com/quotes"
response = requests.get(url)
data = response.json()
df = Pd.DataFrame(data["quotes"])
print(df)


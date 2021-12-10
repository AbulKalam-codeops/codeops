import requests
import pandas as pd

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Api-Key': '4nm408j6l98hpnfi71kzqxcnc'
}
# Requesting server to get the details and storing response in result variable
response = requests.get(
    "https://api-test.sandbox-resellers.jetbrains.com/resellers/api/v1/productPrices", headers=headers)
print(response.text)

df = pd.json_normalize(response.json())

df.to_csv("test.csv")

df.to_excel('test.xlsx')

df.to_html('test.html')

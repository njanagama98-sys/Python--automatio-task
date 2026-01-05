import requests
from bs4 import BeautifulSoup

# 1. వెబ్‌సైట్ అడ్రస్
url = 'https://news.ycombinator.com/'

# 2. వెబ్‌సైట్ నుండి సమాచారం తెచ్చుకోవడం
print("వార్తలు సేకరిస్తున్నాను, ఒక్క నిమిషం ఉండండి...\n")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 3. మొదటి 5 వార్తల పేర్లను వెతికి చూపిస్తుంది
for item in soup.find_all('span', class_='titleline')[:5]:
    print(f"వార్త: {item.text}")

print("\nపని పూర్తయింది!")

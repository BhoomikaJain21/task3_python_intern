import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all('h2')

        with open('headlines.txt', 'w', encoding='utf-8') as file:
            file.write("Top Headlines\n")
            file.write("-" * 20 + "\n\n")

            if headlines:
                for i, headline in enumerate(headlines, 1):
                    title = headline.get_text(strip=True)
                    file.write(f"{i}. {title}\n")
                print("✅ Successfully scraped and saved headlines to 'headlines.txt'.")
            else:
                print("⚠️ No headlines found. The script might need to be adjusted for the website's structure.")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the URL: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

scrape_headlines('https://www.thehindu.com/')
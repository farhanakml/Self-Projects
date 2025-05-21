import time
import requests
from bs4 import BeautifulSoup

 
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}
 
 
def fetching_content(url):
    """Mengambil konten HTML dari URL yang diberikan."""
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None
 
 
def extract_clothing_data(item):
    """Mengambil data buku berupa judul, harga, ketersediaan, dan rating dari article (element html)."""
    try:
        title = item.find('h3', class_='product-title').text.strip()
    except:
        title = "N/A"
    try:
        price = item.find('span', class_='price').text.strip()
    except:
        price = "N/A"
    
    # Extract details like rating, colors, size, and gender from <p> tags
    details = item.find_all("p")

    rating = next((p.text.strip() for p in details if "Rating" in p.text), "N/A")
    colors = next((p.text.strip() for p in details if "Color" in p.text), "N/A")
    size = next((p.text.strip() for p in details if "Size" in p.text), "N/A")
    gender = next((p.text.strip() for p in details if "Gender" in p.text), "N/A")

    product = {
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Colors": colors,
        "Size": size,
        "Gender": gender
    }

    return product
 
 
def scrape_clothes(base_url, start_page=1, delay=2):
    """Fungsi utama untuk mengambil keseluruhan data, mulai dari requests hingga menyimpannya dalam variabel data."""
    data = []
    page_number = 1

    while True:
        if page_number == 1:
            url = base_url
        else:
            url = f"{base_url}/page{page_number}"

        print(f"Scraping page: {url}")
        content = fetching_content(url)
        
        if content:
            soup = BeautifulSoup(content, "html.parser")
            clothing_element = soup.find_all('div', class_='collection-card')
            for clothes in clothing_element:
                item = extract_clothing_data(clothes)
                data.append(item)
 
            next_button = soup.find('li', class_='page-item next')
            if next_button:
                page_number += 1
                time.sleep(delay) # Delay sebelum halaman berikutnya
            else:
                break # Berhenti jika sudah tidak ada next button
        else:
            break # Berhenti jika ada kesalahan
 
    return data
 
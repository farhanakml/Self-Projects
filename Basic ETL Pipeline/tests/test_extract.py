import pytest
from bs4 import BeautifulSoup
from utils.extract import extract_clothing_data, fetching_content

# Dummy HTML for a single clothing item
SAMPLE_HTML = """
<div class="collection-card">
    <h3 class="product-title">T-shirt X</h3>
    <span class="price">$99.99</span>
    <p>Rating: ⭐ 4.5 / 5</p>
    <p>Color: 3 Colors</p>
    <p>Size: L</p>
    <p>Gender: Unisex</p>
</div>
"""

def test_extract_clothing_data():
    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    item = soup.find("div", class_="collection-card")
    result = extract_clothing_data(item)

    assert result["Title"] == "T-shirt X"
    assert result["Price"] == "$99.99"
    assert result["Rating"] == "Rating: ⭐ 4.5 / 5"
    assert result["Colors"] == "Color: 3 Colors"
    assert result["Size"] == "Size: L"
    assert result["Gender"] == "Gender: Unisex"

def test_fetching_content_success():
    url = "https://fashion-studio.dicoding.dev"
    content = fetching_content(url)
    assert content is not None
    assert isinstance(content, bytes)

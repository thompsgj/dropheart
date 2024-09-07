import django
import random
import requests

django.setup()

ITEM_CHOICES = [
    ("ELECTRONICS", "Electronics"),
    ("BOOKS", "Books"),
    ("GAMES", "Games"),
    ("ARTS", "Arts"),
    ("MEN_FASHION", "Men_fashion"),
    ("WOMEN_FASHION", "Women_fashion")
]

descriptions = {
    "ELECTRONICS": "Top-of-the-line electronic device with advanced features.",
    "BOOKS": "A best-selling novel that will keep you hooked till the last page.",
    "GAMES": "An exciting game that offers hours of entertainment.",
    "ARTS": "A beautiful artwork that would enhance any living space.",
    "MEN_FASHION": "A stylish and trendy piece for men’s fashion.",
    "WOMEN_FASHION": "An elegant and fashionable piece for women’s fashion."
}

# URLS to image
image_links = {
    "ELECTRONICS": {
        "Smartphone": "https://dictionary.cambridge.org/ko/images/thumb/smartp_noun_002_34391.jpg?version=6.0.31",
        "Laptop": "https://i.pcmag.com/imagery/reviews/01DwPnq2ew5930qO5p4LXWH-1..v1677608790.jpg"
    },
    "BOOKS": {
        "Mystery Novel": "https://upload.wikimedia.org/wikipedia/commons/7/78/Mystery_January_1934.jpg",
        "Science Fiction": "https://target.scene7.com/is/image/Target/GUEST_fd3858b5-a92f-4314-8376-429f676d7056?wid=488&hei=488&fmt=pjpeg"
    },
    "GAMES": {
        "Strategy Game": "https://upload.wikimedia.org/wikipedia/commons/3/38/Chess_set.jpg",
        "Racing Game": "https://c02.purpledshub.com/uploads/sites/41/2023/08/Hot-Wheels-tracks.jpg"
    },
    "ARTS": {
        "Oil Painting": "https://img.freepik.com/free-vector/watercolor-colorful-background-with-oil-painting_52683-105950.jpg",
        "Sculpture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQI5AONMwm13h_xRXk-NZlFs-_U6nomGsfDaw&s"
    },
    "MEN_FASHION": {
        "Leather Jacket": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrHLhsZJ5CvGRyLkQn60rQc_Wao4eiJyabyQ&s",
        "Formal Suit": "https://images-na.ssl-images-amazon.com/images/I/61AqenOjvHL.jpg"
    },
    "WOMEN_FASHION": {
        "Evening Dress": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaSpE0uCD4NXCDrIWdDDto4P1ydb4kNObYSw&s",
        "Heels": "https://all4me.com.au/app/uploads/2017/11/102430786_10222096725862656_6495889195814730989_n.jpg"
    }
}

# Generate item name and image
def generate_item_name_and_image(item_type):
    item_name = random.choice(list(image_links[item_type].keys()))
    image_url = image_links[item_type][item_name]
    return item_name, image_url

for i in range(20):
    item_type = random.choice(ITEM_CHOICES)[0]
    item_name, image_url = generate_item_name_and_image(item_type)
    item_description = descriptions[item_type]

    # Json Data for the items
    data = {
        "location_id": "Seoul, South Korea",
        "item_type": item_type,
        "image_path": image_url,
        "status": "AVAILABLE",
        "item_name": item_name,
        "item_description": item_description
    }

    # Send the POST request
    response = requests.post(url="https://dropheart-backend-z8c0.onrender.com/api/create/item", json=data)

    # Print the response status code and content
    print(f"Sent request {i+1}, Status Code: {response.status_code}, Response: {response.text}")

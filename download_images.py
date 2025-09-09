import os
import requests

# Folder to save images
folder = "media/products"
os.makedirs(folder, exist_ok=True)

# Product name: direct image URL
products = {
    "apple": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
    "banana": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg",
    "orange": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Orange-Fruit-Pieces.jpg",
    "mango": "https://upload.wikimedia.org/wikipedia/commons/9/90/Hapus_Mango.jpg",
    "grapes": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Table_grapes_on_white.jpg",
    "pineapple": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Pineapple_and_cross_section.jpg",
    "papaya": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Papaya_cross_section_bangladesh.jpg",
    "strawberry": "https://upload.wikimedia.org/wikipedia/commons/2/29/PerfectStrawberry.jpg",
    "watermelon": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Watermelon_cross_BNC.jpg",
    "kiwi": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Kiwi_aka.jpg",
    "carrot": "https://upload.wikimedia.org/wikipedia/commons/4/40/Carrot.jpg",
    "tomato": "https://upload.wikimedia.org/wikipedia/commons/8/88/Bright_red_tomato_and_cross_section02.jpg",
    "potato": "https://upload.wikimedia.org/wikipedia/commons/6/60/Potato_and_cross_section.jpg",
    "onion": "https://upload.wikimedia.org/wikipedia/commons/2/25/Onion.jpg",
    "cucumber": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Cucumber_and_cross_section.jpg",
    "spinach": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Spinach_leaves.jpg",
    "cauliflower": "https://upload.wikimedia.org/wikipedia/commons/1/10/Cauliflower_and_cross_section_edit.jpg",
    "broccoli": "https://upload.wikimedia.org/wikipedia/commons/0/03/Broccoli_and_cross_section_edit.jpg",
    "capsicum": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Capsicum.jpg",
    "beetroot": "https://upload.wikimedia.org/wikipedia/commons/8/81/Beetroot.jpg",
    "milk": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Milk_glass.jpg",
    "paneer": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Paneer_cubes.jpg",
    "curd": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Yogurt_in_a_bowl.jpg",
    "butter": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Butter_in_wrap.jpg",
    "cheese": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Emmental_cheese.jpg",
    "ghee": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Ghee_in_a_bowl.jpg",
    "yogurt": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Yogurt_in_a_bowl.jpg",
    "cream": "https://upload.wikimedia.org/wikipedia/commons/0/05/Heavy_cream.jpg",
    "buttermilk": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Buttermilk.jpg",
    "ice cream": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Ice_Cream_cone_-_vanilla.jpg",
    "chili": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Red_Chili.jpg",
    "ginger": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Ginger_Rhizome.jpg",
    "garlic": "https://upload.wikimedia.org/wikipedia/commons/8/8b/GarlicHead.jpg",
    "lemon": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Lemon-edit1.jpg",
    "mushroom": "https://upload.wikimedia.org/wikipedia/commons/5/55/Agaricus_bisporus2.jpg",
    "corn": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Corncobs.jpg",
    "peas": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Green_peas.jpg",
    "banana leaf": "https://upload.wikimedia.org/wikipedia/commons/4/41/Banana_leaf.jpg",
    "pumpkin": "https://upload.wikimedia.org/wikipedia/commons/0/03/Cucurbita_pepo.jpg",
    "lettuce": "https://upload.wikimedia.org/wikipedia/commons/2/29/Iceberg_lettuce.jpg"
}

# Download all images
for name, url in products.items():
    response = requests.get(url)
    path = os.path.join(folder, f"{name.replace(' ', '_')}.jpg")
    with open(path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {name}")

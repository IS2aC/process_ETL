import requests
from transform import transformation
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
db = myclient['GOT']

compteur = 0

# Extraction -- acteurs
for i in range(10, 1000):
    url = f"https://anapioficeandfire.com/api/characters/{i}"
    a = requests.get(url).json()

    # Transformation -- sélection unique des personnages principaux qui sont plus apparus dans la série
    if (transformation(a).get('culture') is not None) and (transformation(a).get('born') is not None) and (transformation(a).get('tvSeries') is not None):
        a = transformation(a)

        # Chargement dans la BD mongo
        db['actors'].insert_one(a)
    else:
        pass

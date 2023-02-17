def list_to_none_or_not(liste):
    """Fonction pour supprimer les listes sans contenus"""

    if len(liste) == 1 and liste[0] == '':
        return None
    return liste


def str_to_none_or_not(char):
    """Fonction pour supprimer les chaines de caractère sans contenus"""

    if char == '':
        return None
    return char


def transformation(json):
    """Extraction des features importantes"""

    return {
        "api_id": json.get("url").split("/")[-1],
        "name": json.get('name'),
        "gender": json.get("gender"),
        "culture": str_to_none_or_not(json.get("culture")),
        "born": str_to_none_or_not(json.get("born")),
        "tvSeries": list_to_none_or_not(json.get('tvSeries'))
    }

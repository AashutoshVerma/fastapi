def noteEntity(item) -> dict:
    return{
        "id" : str(item["id"]),
        "title" : item["title"],
        "desc" : item["desc"],
        "important" : item["important"],

    }
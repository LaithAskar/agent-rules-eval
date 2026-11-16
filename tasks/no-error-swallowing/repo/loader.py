import json


def load_user(text):
    data = json.loads(text)
    return {"name": data["name"], "age": int(data["age"])}

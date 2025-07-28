# # Data validation logic
# def validate(data):
#     return data and data.get('title') is not None


def validate(data):
    return "title" in data and isinstance(data["paragraphs"], list)

# Data validation logic
def validate(data):
    return data and data.get('title') is not None

import hug

api = hug.get(on_invalid=hug.redirect.not_found)

@api.urls('/do-math', examples='number_1=1&number_2=2')
def math(number_1: hug.types.number, number_2: hug.types.number):
    return number_1 + number_2


@api
def happy_birthday(name, age: hug.types.number):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())

import hug


@hug.get(examples='name=Timothy&age=26')
def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):

    return  {'message': f'Happyr {name} Birthday {age}!',
             'took': float(hug_timer)}

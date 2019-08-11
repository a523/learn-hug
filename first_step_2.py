import hug
from falcon import HTTPError, HTTP_401, HTTPStatus


class MyErr(HTTPError):
    def __init__(self, desc):
        super().__init__(status=HTTP_401, title='err', description=str(desc))


@hug.exception(exclude=MyErr)
def handle_exception(exception, response):
    response.status = HTTP_401
    return {'err': '{}'.format(exception)}


@hug.cli()
@hug.get(examples='name=Timothy&age=26')
def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):
    if age < 0:
        raise MyErr
    if age == 0:
        raise Exception('is zero')

    try:
        with open(name, 'r') as f:
            f.readlines()

    except FileNotFoundError as e:
        raise MyErr(e)
    return {'message': f'Happy {name} Birthday {age}!',
            'took': float(hug_timer)}


if __name__ == '__main__':
    happy_birthday.interface.cli()

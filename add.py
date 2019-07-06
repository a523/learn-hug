import hug


@hug.cli()
def add(number_1: hug.types.number, number_2: hug.types.number):
    """Returns the result of adding number_1 to number_2"""
    return number_1 + number_2


if __name__ == '__main__':
    add.interface.cli()

def two_fer(name=''):
    if name == '' or name is None:
        return "One for you, one for me."
    return 'One for ' + name + ', ' + 'one for me.'

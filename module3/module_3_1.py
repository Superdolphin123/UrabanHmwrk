def count_calls():
    print(calls)


def string_info(string=''):
    global calls
    calls += 1
    return len(string), string.upper(), string.lower()


def is_contains(string='', list_to_search=None):
    if list_to_search is None:
        list_to_search = []
    global calls
    calls += 1
    if string.lower() in str(list_to_search).lower():
        return True
    else:
        return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

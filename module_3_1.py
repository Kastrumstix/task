calls = 0
def count_calls():
    global calls
    calls += 1
    return
def string_info(s):
    count_calls()
    return (len(s), s.upper(), s.lower())
def is_contains(s, list):
    count_calls()
    return s.lower() in [x.lower() for x in list]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Кракозябра'))
print(string_info('123МиХаИл123'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('КуК', ['кУк', 'Аву', 'Енпр']))
print(calls)
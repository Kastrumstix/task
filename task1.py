animals = ['python','gopher']
more_animals = animals
print(animals == more_animals) #=> True
print(animals is more_animals) #=> True
even_more_animals = ['python','gopher']
print(animals == even_more_animals) #=> True
print(animals is even_more_animals) #=> False
print(id(animals))
print(id(more_animals))
print(id(even_more_animals))
print('Топинамбур'.istitle())
print('нам' in 'топинамбур')
print('The worlds fastest plane'.rfind('plane'))
print('The worlds fastest plane'.find('plane'))
print('The worlds fastest plane'.index('plane'))
print('The first president of the organization..'.count('o'))
print('florida dolphins'.capitalize())
name = 'Chris'
food = 'creme brulee'
print(f'Hello. My name is {name} and I like {food}.')
print('the happiest person in the whole wide world.'.index('the',4,44))
difficulty = 'easy'
thing = 'exam'
print('That {} was {}!'.format(thing, difficulty))
print('8000.0'.isnumeric())
print('This is great'.split(' '))
print('not--so--great'.split('--'))
print('all lower case'.islower()) #=> True
print('not aLL lowercase'.islower()) # False)
print(''.join(reversed("hello world")))
print('-'.join(['a','b','c']))
print( 'Â'.isascii() ) #=> False
print( 'A'.isascii() ) #=> True
sentence = 'The Cat in the Hat'
print(sentence.upper()) #=> 'THE CAT IN THE HAT'
print(sentence.lower()) #=> 'the cat in the hat'
animal = 'fish'
print(animal[0].upper() + animal[1:-1] + animal[-1].upper())
print('Toronto'.isupper()) #=> False
print('TORONTO'.isupper())
sentence = "It was a stormy night\nThe house creeked\nThe wind blew."
print(sentence.splitlines())
string = 'I like to eat apples'
print(string[:6] )#=> 'I like'
print(string[7:13]) #=> 'to eat'
print(string[0:-1:2]) #=> 'Ilk oetape' (каждый 2-й символ)
print('One1'.isalpha())
print('One'.isalpha())
sentence = 'Sally sells sea shells by the sea shore'
print(sentence.replace('sea', 'mountain')) #=> 'Sally sells mountain shells by the mountain shore'
print(min('strings')) #=> 'g')
print('Ten10'.isalnum()) #=> True
print('Ten10.'.isalnum()) #=> False
string = '  string of whitespace    '
print(string.lstrip()) #=> 'string of whitespace    '
print(string.rstrip()) #=> '  string of whitespace'
print(string.strip()) #=> 'string of whitespace'

# Print welcome Message

#dir() -> nos muestra todos los atributos que podemos usar en una variable
# help(str.lower)
# lower()
# upper()
# count()
# find()
# replace()

message = 'Hello World'

new_message = message.replace('World', 'Universe')

print(new_message)

greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {name}. Welcome!'

print(message)

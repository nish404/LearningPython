# dictionary = a changeable, unordered collection or unique key:value pairs 
# fast because they use hashing, allow us to access a value quickly 

capitals = {'USA':'Washington DC',
            'Brazil':'Brasilia',
            'Canada':'Ottawa',
            'England':'London'}

capitals.update({'Monaco':'Monaco'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('England')
capitals.clear()

#print(capitals['Canada'])
#print(capitals.get('Monaco'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key, value)

# logical operators
# check if magician AND expert: "you are a master magician"
# check if magician but not expert: "atleast you're getting there"
# if both false: "you need to practice more"

is_magician = True
is_expert= False

if is_expert and is_magician: 
    print('You are a master magician')
elif is_magician and not is_expert:
    print("Atleast you're getting there")
else: 
    print('You need to practice more')

import requests
#maine coon, ragdoll, sphynx cat, bombay cat, devon rex, persian , birman
#exotic, abyssinian, siamese, turkish angora

#name = 'siamese'
#prompt user for input on cat breed
name = input("Please type in the name of a domestic cat breed:\n")

#retreive cat information via their breed names
api_url = 'https://api.api-ninjas.com/v1/cats?name={}'.format(name)

#api key used
response = requests.get(api_url, headers={'X-Api-Key': 'yourspecialapikeymustbeputhere'})

#test if api works with response object
#if response.status_code == requests.codes.ok:
 #  print(response.text)
#else:
 # print("Error:", response.status_code, response.text)

#this will output it nicely
#cat's breed
cat_breed = response.json()[0]['name']
print(f'name : {cat_breed}')

#cat's origin
origin = response.json()[0]['origin']
print(f'origins : {origin}')

#cat's minimum life expectancy
minexp = response.json()[0]['min_life_expectancy']
print(f'min life expectancy : {int(minexp)} years')

#cat's maximum life expectancy
maxexp = response.json()[0]['max_life_expectancy']
print(f'max life expectancy : {int(maxexp)} years')

#cat's min and max weight
minweight = response.json()[0]['min_weight']
weightmin = minweight / 2.205
print(f'min weight: {int(weightmin)} kg')

maxweight = response.json()[0]['max_weight']
weightmax = maxweight / 2.205
print(f'max weight: {int(weightmax)} kg')

#length of cat in inches
catlength = response.json()[0]['length']
print(f'length : {catlength}')

#cat url
image = response.json()[0]['image_link']
print(f'link to cat\'s picture : {image}')

#print('On a scale from 0 to 5 how would you rate the breed\'s:')

health = response.json()[0]['general_health']
print(f'general health: {health}/5')

intelligence = response.json()[0]['intelligence']
print(f'intelligence: {intelligence}/5')

friendly = response.json()[0]['family_friendly']
print(f'family friendliness : {friendly}/5')

playful = response.json()[0]['playfulness']
print(f'playfulness:{playful}/5')

shedding =response.json()[0]['shedding']
print(f'shedding: {shedding}/5')

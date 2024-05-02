#!/usr/bin/python3

from server.models.amenity import Amenity
from server.models.city import City
from server.models.client import Client
from server.models.gym import Gym
from server.models.owner import Owner
from server.models.review import Review
from random import choice


clients = []
owners = []
cities = []
amenities = []


amenity_names = ["Security cameras", "Energy-efficient lighting and equipment", "First-aid stations", "Emergency exits and alarms", "Parking lots", "Bicycle racks", "Accessible facilities for disabled members", "Wi-Fi", "Music", "TV screens for entertainment", "Lounges", "Cafeterias or snack bars", "Retail shops", "Kids' playrooms", "Supervised childcare", "Showers", "Lockers", "Changing rooms", "Toilets", "Nutrition consulting", "Personal training", "Basketball courts", "Racquetball/squash courts", "Tennis courts", "Indoor soccer fields", "Swimming pools", "Steam rooms", "Fitness class rooms", "Yoga studios", "Boxing area"]

city_names = ["Casablanca", "Rabat", "Fes", "Marrakech", "Tangier", "Agadir", "Meknes", "Oujda", "Kenitra", "Tetouan", "Safi", "Mohammedia", "Khouribga", "Beni Mellal", "El Jadida", "Taza", "Nador", "Laayoune", "Larache", "Ksar El Kebir", "Essaouira", "Taounate", "Dakhla", "Sale", "Chefchaouen", "Azrou", "Al Hoceima", "Safar", "Zagora", "Inezgane"]

client_names = [("Badr", "Annabi"), ("Oumaima", "Naanaa"), ("Ahmed", "Raqui"), ("Ilyas", "Abounouas"), ("Ihsan", "Benbela")]

owner_names = [("Abdelhalim", "Elbouaami"), ("Radouane", "Abounouas"), ("Wakil"), ("khalil")]

gym_names = ["PowerPulse Fitness", "IronFist Gym", "Elevate Fitness Club", "Apex Strength Studio", "CoreQuest Gym", "ThunderFlex Fitness", "Titan Training Center", "FitSphere Wellness", "Prime Energy Gym", "Zenith Fitness Lab", "MaxForce Gym", "HyperFit Training Studio", "Iron Fortress Gym", "FlexPoint Fitness", "Summit Strength Co.", "VitalCore Gym", "Peak Performance Gym", "PulsePoint Fitness", "Radiant Strength Studio", "Urban FitWorks", "EdgePower Gym", "Iron Haven Fitness", "BodyWave Gym", "Torque Fitness Club", "Stronghold Training Center", "UltraFit Performance", "SteelGrip Gym", "NextLevel Fitness", "ImpactZone Gym", "SpartanFit Training Center"]

gym_cities = ["Casablanca", "Casablanca", "Casablanca", "Rabat", "Rabat", "Rabat", "Marrakech", "Marrakech", "Marrakech", "Tangier", "Tangier", "Fes", "Fes", "Agadir", "Agadir", "Meknes", "Oujda", "Kenitra", "Tetouan", "El Jadida", "Mohammedia", "Mohammedia", "Sale", "Sale", "Beni Mellal", "Khouribga", "Safar", "Inezgane", "Laayoune", "Dakhla"]

gym_descriptions = ["A high-energy gym that offers a range of high-intensity workouts designed to boost strength, endurance, and overall fitness.", "Focused on strength training and bodybuilding, with a vast array of free weights and machines to help you build muscle.", "A modern gym that emphasizes personal growth, offering customized fitness plans, group classes, and personal training.", "An elite gym designed for athletes and fitness enthusiasts seeking advanced training programs and equipment.", "Specializes in core strength and functional training, with workouts designed to improve stability and flexibility.", "A dynamic gym that combines strength training with high-intensity interval workouts to help you reach your fitness goals.", "A large gym equipped with state-of-the-art equipment and facilities for bodybuilding, weightlifting, and cross-training.", "A holistic fitness center offering yoga, pilates, and mindfulness classes alongside traditional strength and cardio workouts.", "A vibrant gym focused on high-energy workouts, perfect for those who love group classes, dance fitness, and aerobics.", "A cutting-edge gym that utilizes the latest fitness technology to track progress and optimize workouts.", "Designed for those who want to push their limits, with a variety of intense training programs and heavy equipment.", "A boutique gym offering personalized workouts and small group training sessions for maximum results.", "Designed like a fortress, providing a tough environment for those who are serious about strength and muscle building.", "A flexible gym that offers a variety of workout options, from yoga and pilates to weightlifting and cardio classes.", "Inspires you to reach new heights with its challenging workouts and mountain-themed décor.", "Focusing on building core strength and overall vitality, with specialized equipment and expert trainers.", "A performance-oriented gym that offers elite training programs for athletes and fitness enthusiasts alike.", "A high-energy gym with a focus on cardiovascular health, featuring a variety of cardio machines and group fitness classes.", "Designed to bring out your inner radiance, with a focus on holistic wellness and strength training.", "A modern gym located in the heart of the city, catering to urban professionals with busy lifestyles, offering quick and effective workouts.", "A sleek and modern gym designed for those who live on the edge, offering high-intensity training sessions and unique workout challenges.", "A sanctuary for weightlifting and strength training, with a focus on building muscle and physical endurance.", "Focuses on functional movement and bodyweight exercises, promoting flexibility and overall fitness through natural motion.", "A high-octane gym specializing in functional fitness and cross-training, with intense bootcamps and circuit training.", "A gym that feels like a fortress, offering robust strength-training equipment and challenging workouts for hardcore fitness enthusiasts.", "Dedicated to performance improvement, with a range of advanced fitness programs, nutrition guidance, and recovery services.", "A no-nonsense gym focused on building raw strength and power, with an extensive collection of heavyweights and lifting platforms.", "Takes your fitness journey to the next level, with a focus on progressive training and continuous improvement.", "Provides high-impact workouts and intense group classes designed to burn calories and build strength quickly.", "Embraces the Spartan ethos, offering challenging workouts inspired by ancient warrior training and obstacle courses."]

gym_locations = ["Casablanca's Maarif District", "Casablanca's Racine District", "Casablanca's Anfa District", "Rabat's Hay Riad", "Rabat's Agdal District", "Rabat's Hassan District", "Marrakech's Gueliz District", "Marrakech's Hivernage District", "Marrakech's Palmeraie", "Tangier's Malabata District", "Tangier's Iberia District", "Fez's Ville Nouvelle", "Fez's Saiss District", "Agadir's Founty District", "Agadir's Talborjt District", "Meknes's Hamria", "Oujda's Al Qods District", "Kenitra's Val Fleuri", "Tetouan's M'diq", "El Jadida's Sidi Bouzid", "Mohammedia's Quartier Floride", "Mohammedia's Quartier Essalam", "Salé's Tabriquet", "Salé's Hay Karima", "Beni Mellal's Tazart District", "Khouribga's Quartier Mimosa", "Safar's N'gadi District", "Inezgane's Hay Assaada", "Laayoune's El Marja District", "Dakhla's Al Walaa"]

gym_profile_pics = ["https://i.ibb.co/88fh6MC/1.jpg", "https://i.ibb.co/k9xLNYZ/2.jpg", "https://i.ibb.co/jJ23zkB/3.jpg", "https://i.ibb.co/12qt8N2/4.jpg", "https://i.ibb.co/K6jz2pc/5.jpg", "https://i.ibb.co/XWdRLws/6.jpg", "https://i.ibb.co/hW47mBM/7.jpg", "https://i.ibb.co/Jm2H9cm/8.jpg", "https://i.ibb.co/Jm2H9cm/8.jpg", "https://i.ibb.co/Fz36gnm/10.jpg", "https://i.ibb.co/PNWXXxT/11.jpg", "https://i.ibb.co/b6D5Q03/12.jpg", "https://i.ibb.co/YXwBJhK/13.jpg", "https://i.ibb.co/S0Nc8hM/14.jpg", "https://i.ibb.co/F0svcY1/15.jpg", "https://i.ibb.co/M1vwQrf/16.jpg", "https://i.ibb.co/jbYyC28/17.jpg", "https://i.ibb.co/QKvyZmB/18.jpg", "https://i.ibb.co/WkQYGrZ/19.jpg", "https://i.ibb.co/fSVKMpR/20.jpg", "https://i.ibb.co/K7rQS9p/21.jpg", "https://i.ibb.co/6bGtXbX/22.jpg", "https://i.ibb.co/71q1dFK/23.jpg", "https://i.ibb.co/YfB5xhs/24.jpg", "https://i.ibb.co/gdZdvxY/25.jpg", "https://i.ibb.co/f1mvGpF/26.jpg", "https://i.ibb.co/GRptWQm/27.jpg", "https://i.ibb.co/RCkNb6F/28.jpg", "https://i.ibb.co/sqGyLWy/29.jpg", "https://i.ibb.co/svxqWvW/30.jpg"]


reviews = ["I love this gym! The staff is super friendly, the equipment is top-notch, and they keep everything clean. The classes are fun, and the trainers are very knowledgeable.", "I really enjoy working out here. There's a good variety of machines and free weights. The only downside is that it can get pretty crowded during peak hours.", "This gym has a great atmosphere. It's spacious, and there's a good mix of people at all fitness levels. Plus, they offer a lot of unique classes you don't find elsewhere.", "The gym is okay. The equipment is decent, but I've noticed some machines that are out of order for a while. The locker rooms could also use a bit more attention in terms of cleanliness.", "This is the best gym I've ever been to. The personal trainers are fantastic, and they really help you reach your goals. The group classes are also amazing, and there's a great community feel.", "The gym has potential, but there's a lack of maintenance. A lot of equipment is old or broken, and they don't seem to repair it quickly. The staff is friendly, but that's about it.", "A good gym overall. I like the variety of equipment and the fact that they have a sauna and steam room. The only problem is the parking; it's always a challenge to find a spot.", "This gym is fantastic! The variety of classes keeps me motivated, and I love the sense of community. The trainers are approachable and willing to help, even outside of class times.", "The gym has a lot of different equipment, which is great, but sometimes it feels like there's not enough space to move around. It can get a bit cramped during busy times.", "The gym is okay for basic workouts, but it's not very inspiring. The interior design is a bit dull, and there's not much natural light. It's also a bit on the pricier side for what it offers.", "The gym has a lot of great amenities, like a swimming pool and a juice bar. I also appreciate the variety of classes offered, from yoga to kickboxing.", "It's a decent gym, but I find the music a bit too loud. It can be hard to concentrate during workouts, especially during peak hours.", "I love this gym's focus on wellness and recovery. They offer massage services and have a dedicated meditation room, which is a nice touch.", "The gym has a great selection of free weights and cardio machines, but they could use more squat racks. It gets busy, and there's often a wait.", "I like the location of this gym; it's close to my office. However, the changing rooms are quite small, and it can be a tight squeeze when it's crowded.", "This gym has a friendly atmosphere, and the staff is always willing to help. The equipment is a bit older, but it still gets the job done.", "The personal trainers here are amazing. They really take the time to understand your goals and customize workouts to meet your needs.", "It's a great gym for beginners. The staff is helpful and not intimidating, which makes it easier to get started with a fitness routine.", "The gym is open 24/7, which is super convenient for my schedule. I just wish they had a few more classes in the late evening.", "I joined this gym for the swimming pool, but I've also been enjoying the group fitness classes. They have something for everyone.", "The gym's layout is a bit confusing. It took me a while to figure out where everything is, and there's not much signage to help.", "The staff at this gym is fantastic. They're always friendly and make you feel welcome, even if you're new to working out.", "This gym is a bit on the expensive side, but you get what you pay for. The facilities are top-notch, and they keep everything clean and well-maintained.", "It's a smaller gym, but that means it's less crowded, which I like. There's always plenty of space to work out without feeling cramped.", "The gym has a nice community feel, with regular events and challenges. It makes working out more fun and engaging.", "The equipment is modern and in good condition, but the gym could use more mirrors. It can be hard to check your form without them.", "I appreciate that this gym has a women's-only section. It makes me feel more comfortable during my workouts.", "This gym is well-equipped, but it doesn't have a sauna or steam room, which is a drawback for me. Otherwise, it's a great place to work out.", "The location is perfect for me, and the gym has a nice view of the city. It makes working out a bit more enjoyable.", "The gym offers child care, which is a big plus for me as a parent. It allows me to work out without worrying about my kids."]
    

# print(len(gym_names))
# print(len(gym_descriptions))
# print(len(gym_locations))
# print(len(gym_profile_pics))
# print(len(gym_cities))

#create the cities

for city_name in city_names:
    city = City(name=city_name)
    city.save()
    cities.append(city)

print()
print("############################")
print()
print("all cities have been created")
print()
print("############################")

for amenity_name in amenity_names:
    amenity = Amenity(name=amenity_name)
    amenity.save()
    amenities.append(amenity)

print()
print("###############################")
print()
print("all amenities have been created")
print()
print("###############################")

for client_name in client_names:
    client = Client(first_name=client_name[0], last_name=client_name[1], email="{}.{}@gmail.com".format(client_name[1], client_name[0]), password="client1234")
    client.save()
    clients.append(client)

print()
print("#############################")
print()
print("all clients have been created")
print()
print("#############################")

for owner_name in owner_names:
    owner = Client(first_name=owner_name[0], last_name=owner_name[1], email="{}.{}@gmail.com".format(owner_name[1], owner_name[0]), password="owner1234")
    owner.save()
    owners.append(owner)

print()
print("############################")
print()
print("all owners have been created")
print()
print("############################")


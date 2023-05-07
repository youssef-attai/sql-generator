import random
import time

M = 'M'
F = 'F'

cities = { "United States": [ "New York City", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
          "Canada": ["Toronto", "Montreal", "Vancouver", "Ottawa", "Calgary", "Edmonton", "Quebec City", "Winnipeg", "Hamilton", "Kitchener"],
          "United Kingdom":[ "London", "Birmingham", "Manchester", "Leeds", "Glasgow", "Newcastle upon Tyne", "Liverpool", "Sheffield", "Bristol", "Nottingham"],
          "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille"],
          "Germany": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Dusseldorf", "Dortmund", "Essen", "Leipzig"],
          "Italy": ["Rome", "Milan", "Naples", "Turin", "Palermo", "Genoa", "Bologna", "Florence", "Venice", "Verona"],
          "Spain": ["Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza", "Malaga", "Murcia", "Palma", "Las" "Palmas de Gran Canaria", "Bilbao"],
          "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold" "Coast", "Canberra", "Newcastle", "Wollongong", "Geelong"],
          "Japan": ["Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Kobe", "Kyoto", "Fukuoka", "Kawasaki", "Hiroshima"],
          "China": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Tianjin", "Wuhan", "Dongguan", "Chengdu", "Chongqing", "Nanjing"],
          "Brazil": ["São" "Paulo", "Rio" "de" "Janeiro", "Brasília", "Salvador", "Fortaleza", "Belo" "Horizonte", "Manaus", "Curitiba", "Recife", "Porto Alegre"],
          "Mexico": ["Mexico" "City", "Ecatepec", "Guadalajara", "Puebla", "Juárez", "Tijuana", "León", "Monterrey", "Zapopan", "Nezahualcóyotl"],
          "Argentina": ["Buenos Aires", "Córdoba", "Rosario", "La Plata", "Mar del Plata", "San Miguel de Tucumán", "Salta", "Santa Fe", "Corrientes", "Bahía Blanca"],
          "South Africa": ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth", "Bloemfontein", "East London", "Nelspruit", "Kimberley", "Polokwane"],
          "Nigeria": ["Lagos", "Kano", "Ibadan", "Abuja", "Port Harcourt", "Benin City", "Maiduguri", "Zaria", "Aba", "Jos"],
          "Russia": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Samara", "Omsk", "Kazan", "Rostov-on-Don", "Chelyabinsk"],
          "India": ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai", "Hyderabad", "Pune", "Ahmedabad", "Surat", "Jaipur"],
          "Pakistan": ["Karachi", "Lahore", "Faisalabad", "Rawalpindi", "Multan", "Hyderabad", "Gujranwala", "Peshawar", "Abbottabad", "Quetta"],
          "Turkey": ["Istanbul","Ankara", "Izmir", "Bursa", "Adana", "Gaziantep", "Konya", "Antalya", "Kayseri", "Mersin"],
          "Egypt": ["Cairo", "Alexandria", "Giza", "Shubra El-Kheima", "Port Said", "Suez", "Luxor", "Aswan", "Mansoura", "Tanta"]
          }


female_names = [
        "Emily",
        "Emma",
        "Olivia",
        "Ava",
        "Sophia",
        "Isabella",
        "Mia",
        "Charlotte",
        "Amelia",
        "Harper",
        "Evelyn",
        "Abigail",
        "Elizabeth",
        "Sofia",
        "Victoria",
        "Grace",
        "Chloe",
        "Natalie",
        "Madison",
        "Eleanor",
        "Lily",
        "Hannah",
        "Avery",
        "Addison",
        "Aubrey",
        "Scarlett",
        "Zoe",
        "Leah",
        "Audrey",
        "Aria",
        "Savannah",
        "Brooklyn",
        "Alexa",
        "Lila",
        "Bella",
        "Stella",
        "Gabriella",
        "Maya",
        "Aaliyah",
        "Claire",
        "Nora",
        "Caroline",
        "Piper",
        "Peyton",
        "Madelyn",
        "Penelope",
        "Kennedy",
        "Skylar",
        "Riley",
        "Ariana"
]

male_names = [
        "Liam",
        "Noah",
        "Ethan",
        "Oliver",
        "Aiden",
        "Jackson",
        "Caden",
        "Grayson",
        "Lucas",
        "Mason",
        "Logan",
        "Elijah",
        "Carter",
        "Sebastian",
        "Alexander",
        "Benjamin",
        "James",
        "William",
        "Michael",
        "Matthew",
        "Daniel",
        "Henry",
        "Joseph",
        "David",
        "Gabriel",
        "Samuel",
        "Adam",
        "Andrew",
        "Nicholas",
        "Christopher",
        "Anthony",
        "Ryan",
        "John",
        "Tyler",
        "Owen",
        "Connor",
        "Wyatt",
        "Isaac",
        "Julian",
        "Levi",
        "Cole",
        "Evan",
        "Parker",
        "Caleb",
        "Dylan",
        "Brandon",
        "Cameron",
        "Hunter",
        "Tristan",
        "Austin",
]

products = [
        {"Category": "Smart Home Devices",
         "Product Name": "HomeMind - Smart Home Hub and Voice Assistant"},
        {"Category": "Personalized/Customized Gifts",
         "Product Name": "PrintMate - Custom Photo Phone Cases"},
        {"Category": "Skincare and Beauty Products",
         "Product Name": "GlowGenius - Brightening Facial Mask"},
        {"Category": "Wireless Earbuds and Headphones",
         "Product Name": "SoundHive - True Wireless Earbuds"},
        {"Category": "Portable Power Banks and Chargers",
         "Product Name": "JuiceBox - Ultra-Compact Power Bank"},
        {"Category": "Sustainable and Eco-Friendly Products",
         "Product Name": "EarthEra - Reusable Grocery Bags"},
        {"Category": "Gaming Accessories",
         "Product Name": "GameMaster - Wireless Gaming Controller"},
        {"Category": "Smartphone Cases and Accessories",
         "Product Name": "PhoneArmor - Shockproof Phone Case"},
        {"Category": "Yoga Mats, Fitness Equipment, and Workout Clothes",
         "Product Name": "FlexCore - Non-Slip Yoga Mat"},
        {"Category": "Home Security Cameras and Doorbells",
         "Product Name": "WatchDog - HD Smart Security Camera"},
        {"Category": "Children's Toys and Games",
         "Product Name": "FunZone - Indoor/Outdoor Play Tent"},
        {"Category": "Bluetooth Speakers and Soundbars",
         "Product Name": "SoundBox - Portable Bluetooth Speaker"},
        {"Category": "Pet Products",
         "Product Name": "PetHaven - Orthopedic Pet Bed"},
        {"Category": "Home Decor and Accessories",
         "Product Name": "ArtisanLane - Decorative Throw Pillows"},
        {"Category": "Sustainable and Eco-Friendly Products",
         "Product Name": "LeafLife - Reusable Bamboo Water Bottle}"},
        {"Category": "Smartphone Cases and Accessories",
         "Product Name": "PhoneArmor - Shockproof Phone Case"},
        {"Category": "Smartwatches and Fitness Trackers",
         "Product Name": "FitTracker - Advanced Fitness Tracker"},
        {"Category": "Personalized/Customized Gifts",
         "Product Name": "CustomCraze - Personalized Coffee Mugs"},
        {"Category": "Skincare and Beauty Products",
         "Product Name": "SkinZen - Hydrating Facial Moisturizer"},
        {"Category": "Wireless Earbuds and Headphones",
         "Product Name": "AirBuds - True Wireless Earbuds"},
        {"Category": "Portable Power Banks and Chargers",
         "Product Name": "ChargeMate - Ultra-Fast Charging Power Bank"},
        {"Category": "Sustainable and Eco-Friendly Products",
         "Product Name": "EcoBloom - Biodegradable Flower Pots"},
        {"Category": "Gaming Accessories",
         "Product Name": "PlayPulse - Gaming Headset with LED Lights"},
        {"Category": "Smartphone Cases and Accessories",
         "Product Name": "ToughShield - Rugged Phone Case"},
        {"Category": "Yoga Mats, Fitness Equipment, and Workout Clothes",
         "Product Name": "YogaFlex - Stretchable Yoga Pants"},
        {"Category": "Home Security Cameras and Doorbells",
         "Product Name": "HomeWatch - HD Smart Doorbell"},
        {"Category": "Children's Toys and Games",
         "Product Name": "FunFiesta - Party Pinata Game"},
        {"Category": "Bluetooth Speakers and Soundbars",
         "Product Name": "BoomBar - Wireless Soundbar with Subwoofer"},
        {"Category": "Pet Products",
         "Product Name": "FurBall - Self-Cleaning Cat Litter Box"},
        {"Category": "Home Decor and Accessories",
         "Product Name": "DecoHaus - Minimalist Wall Clock"},
        {"Category": "Sustainable and Eco-Friendly Products",
         "Product Name": "EcoStraw - Reusable Stainless Steel Straw Set"},
        {"Category": "Smart Home Devices",
         "Product Name": "SmartLife - Voice-Activated Smart Home System"},
        {"Category": "Personalized/Customized Gifts",
         "Product Name": "NameFrame - Personalized Picture Frame"},
        {"Category": "Skincare and Beauty Products",
         "Product Name": "ClearSkin - Acne Treatment Cream"},
        {"Category": "Wireless Earbuds and Headphones",
         "Product Name": "SonicFlow - Noise-Canceling Headphones"},
        {"Category": "Portable Power Banks and Chargers",
         "Product Name": "PowerPal - High-Capacity Power Bank"},
        {"Category": "Sustainable and Eco-Friendly Products",
         "Product Name": "EarthyEats - Reusable Beeswax Food Wraps"},
        {"Category": "Gaming Accessories",
         "Product Name": "GamingGrip - Ergonomic Gaming Mousepad"},
        {"Category": "Smartphone Cases and Accessories",
         "Product Name": "SlimShield - Ultra-Thin Phone Case"},
        {"Category": "Yoga Mats, Fitness Equipment, and Workout Clothes",
         "Product Name": "FitFlow - Anti-Slip Yoga Mat"},
        {"Category": "Home Security Cameras and Doorbells",
         "Product Name": "DoorDefender - Wireless Door Sensor Alarm"},
        {"Category": "Children's Toys and Games",
         "Product Name": "PlayLand - Indoor/Outdoor Play Tent"},
        {"Category": "Bluetooth Speakers and Soundbars",
         "Product Name": "SoundWave - Waterproof Bluetooth Speaker"},
        {"Category": "Pet Products",
         "Product Name": "Pawsome - Portable Pet Water Bottle"},
        {"Category": "Home Decor and Accessories",
         "Product Name": "LuxeLounge - Velvet Decorative Pillows"},
        {"Category": "Sustainable and Eco-Friendly Products",
         "Product Name": "EcoFuel - Reusable Bamboo Utensil Set"},
        {"Category": "Smartwatches and Fitness Trackers",
         "Product Name": "FitTracker - Advanced Fitness Tracker"},
        {"Category": "Personalized/Customized Gifts",
         "Product Name": "CustomCraze - Personalized Coffee Mugs"},
        {"Category": "Skincare and Beauty Products",
         "Product Name": "SkinZen - Hydrating Facial Moisturizer"},
        {"Category": "Wireless Earbuds and Headphones",
         "Product Name": "AirBuds - True Wireless Earbuds"},
]

companies = [
    (1, 'Amazon', 'Seattle, WA', 'contact@amazon.com'),
    (2, 'eBay', 'San Jose, CA', 'contact@ebay.com'),
    (3, 'Walmart', 'Bentonville, AR', 'contact@walmart.com'),
    (4, 'Alibaba', 'Hangzhou, China', 'contact@alibaba.com'),
    (5, 'Etsy', 'Brooklyn, NY', 'contact@etsy.com'),
    (6, 'Target', 'Minneapolis, MN', 'contact@target.com'),
    (7, 'Best Buy', 'Richfield, MN', 'contact@bestbuy.com'),
    (8, 'Costco', 'Issaquah, WA', 'contact@costco.com'),
    (9, 'Home Depot', 'Atlanta, GA', 'contact@homedepot.com'),
    (10, 'Lowes', 'Mooresville, NC', 'contact@lowes.com'),
    (11, 'Macys', 'New York, NY', 'contact@macys.com'),
    (12, 'Nordstrom', 'Seattle, WA', 'contact@nordstrom.com'),
    (13, 'Gap', 'San Francisco, CA', 'contact@gap.com'),
    (14, 'Nike', 'Beaverton, OR', 'contact@nike.com'),
    (15, 'Adidas', 'Herzogenaurach, Germany', 'contact@adidas.com'),
    (16, 'Zara', 'Arteixo, Spain', 'contact@zara.com'),
    (17, 'H&M', 'Stockholm, Sweden', 'contact@hm.com'),
    (18, 'Forever 21', 'Los Angeles, CA', 'contact@forever21.com'),
    (19, 'American Eagle Outfitters', 'Pittsburgh, PA', 'contact@ae.com'),
    (20, 'Sephora', 'San Francisco, CA', 'contact@sephora.com'),
    (21, 'Ulta Beauty', 'Bolingbrook, IL', 'contact@ultabeauty.com'),
    (22, 'CVS', 'Woonsocket, RI', 'contact@cvs.com'),
    (23, 'Walgreens', 'Deerfield, IL', 'contact@walgreens.com'),
    (24, 'Starbucks', 'Seattle, WA', 'contact@starbucks.com'),
    (25, 'Dunkin', 'Canton, MA', 'contact@dunkin.com'),
    (26, 'McDonalds', 'Chicago, IL', 'contact@mcdonalds.com'),
    (27, 'Burger King', 'Miami, FL', 'contact@burgerking.com'),
    (28, 'Subway', 'Milford, CT', 'contact@subway.com'),
    (29, 'Dominos Pizza', 'Ann Arbor, MI', 'contact@dominos.com'),
    (30, 'Pizza Hut', 'Plano, TX', 'contact@pizzahut.com'),
]

products = [{**product, "Price": random.choice(list(range(3, 200000)))} for product in products ]

payment_methods = [
        "Credit Card",
        "Debit Card",
        "PayPal",
        "Apple Pay",
        "Google Pay",
        "Venmo",
        "Cash",
]

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def insert_countries():
    return f"""
INSERT INTO [dbo].[Country]
	(Country) VALUES 
{f", {NL}".join([f"{TB}('{country}')" for country in cities])};
"""

def insert_cities():
    return f"""INSERT INTO [dbo].[City]
    (CountryID, City) VALUES
    {f", {NL}".join([f"{TB}({i}, '{city}')" for i, country in enumerate(cities, 1) for city in cities[country]])};
"""

def insert_into_sales_channel():
    result = "INSERT INTO [SalesChannel] ([ChannelName], [CityID], [ContactDetails]) VALUES"

    for company in companies:
        result += f"\n\t('{company[1]}', {random.choice(list(range(1,201)))}, '{company[3]}'),"

    return result[:-1] + ";"

def insert_into_customer(n):
    result = "INSERT INTO [Customer] ([CustomerID], [FullName], [Country], [City], [Age], [Gender]) VALUES\n"
    for i in range(1, n+1):
        country = random.choice(list(cities))
        gender = random.choice([M, F])
        result += f"\t({i}, '{random.choice(male_names if gender == M else female_names)} {random.choice(male_names)}', '{country}', '{random.choice(cities[country])}', {random.choice(list(range(18, 60)))}, '{gender}'),\n"

    return result + ";"

def insert_into_product():
    result = "INSERT INTO [Product] ([StockCode], [Description], [Category], [UnitPrice]) VALUES\n"

    # enumrate on products
    for i, p in enumerate(products):
        product = p
        product_name = product["Product Name"].replace("'", "")
        category = product["Category"].replace("'", "")
        unit_price = product["Price"]
        result += f"({i}, '{product_name}', '{category}', {unit_price}),\n"
    return result + ";"

def insert_into_order(n):
    result = "INSERT INTO [Order] ([InvoiceNo], [CustomerID], [ChannelID], [InvoiceDate], [PaymentMethod]) VALUES\n"
    for i in range(1, n+1):
        result += f"\t({i}, {random.choice(list(range(1, 250 + 1)))}, {random.choice(list(range(1, 30 + 1)))}, '{random_date('1/1/2016 1:30 PM', '1/1/2023 4:50 AM', random.random())}', '{random.choice(payment_methods)}'),\n"
    return result + ";"

def insert_into_order_item(n):
    result = "INSERT INTO [OrderItem] ([OrderID], [ProductStockCode], [Quantity]) VALUES\n"
    pairs = set()
    while len(pairs) < n:
        pair = f"{random.choice(list(range(1, 250 + 1)))}, {random.choice(list(range(0, 45 + 1)))}"
        pairs.add(pair)
    for pair in pairs:
        result += f"\t({pair}, {random.choice(list(range(1, 10 + 1)))}),\n"
    return result + ";"

if __name__ ==  "__main__":
    print(insert_into_order_item(400))

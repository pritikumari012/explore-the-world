from django.http import HttpResponse
from .models import GFG


def home(request):
    return HttpResponse("Welcome to Explore the World!")


def hotels(request):

    hotels = GFG.objects.all()

    # ---------------- FILTERS ----------------

    # Maximum price
    max_price = request.GET.get("max_price")

    if max_price:
        hotels = hotels.filter(hotel_price__lte=max_price)

    # Minimum rating
    min_rating = request.GET.get("rating")

    if min_rating:
        hotels = hotels.filter(rating__gte=min_rating)

    # Property type
    property_type = request.GET.get("property_type")

    if property_type:
        hotels = hotels.filter(property_type=property_type)

    # Bed type
    bed_type = request.GET.get("bed_type")

    if bed_type:
        hotels = hotels.filter(bed_type=bed_type)

    # Bedrooms
    bedrooms = request.GET.get("bedrooms")

    if bedrooms:
        hotels = hotels.filter(bedrooms__gte=bedrooms)

    # Facilities
    if request.GET.get("pool"):
        hotels = hotels.filter(swimming_pool=True)

    if request.GET.get("wifi"):
        hotels = hotels.filter(internet=True)

    if request.GET.get("parking"):
        hotels = hotels.filter(car_parking=True)

    if request.GET.get("airport"):
        hotels = hotels.filter(airport_transfer=True)

    if request.GET.get("gym"):
        hotels = hotels.filter(gym=True)

    # Dining
    if request.GET.get("breakfast"):
        hotels = hotels.filter(breakfast=True)

    if request.GET.get("lunch"):
        hotels = hotels.filter(lunch=True)

    if request.GET.get("dinner"):
        hotels = hotels.filter(dinner=True)

    # ---------------- SORTING ----------------

    sort = request.GET.get("sort")

    if sort == "price":
        hotels = hotels.order_by("hotel_price")

    elif sort == "offer":
        hotels = hotels.filter(
            limited_time_offer=True
        ).order_by("-discount_percentage")

    elif sort == "rating":
        hotels = hotels.order_by("-rating")

    # ---------------- HOTEL CARDS ----------------

    hotel_cards = ""

    for hotel in hotels:

        facilities = []

        if hotel.swimming_pool:
            facilities.append("🏊 Swimming Pool")

        if hotel.internet:
            facilities.append("📶 Wi-Fi")

        if hotel.car_parking:
            facilities.append("🚗 Parking")

        if hotel.airport_transfer:
            facilities.append("✈️ Airport Transfer")

        if hotel.gym:
            facilities.append("🏋️ Gym")

        dining = []

        if hotel.breakfast:
            dining.append("Breakfast")

        if hotel.lunch:
            dining.append("Lunch")

        if hotel.dinner:
            dining.append("Dinner")

        offer = ""

        if hotel.limited_time_offer:
            offer = f"""
            <p style="color:green;">
                <b>🔥 Limited Time Offer -
                {hotel.discount_percentage}% OFF</b>
            </p>
            """

        hotel_cards += f"""
        <div style="
            width: 700px;
            margin: 25px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 12px;
            background: white;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        ">

            <img src="{hotel.hotel_image}"
                 style="
                    width: 100%;
                    height: 300px;
                    object-fit: cover;
                    border-radius: 10px;
                 ">

            <h2>{hotel.hotel_name}</h2>

            <p>📍 {hotel.location}</p>

            <p>
                ⭐ <b>{hotel.rating}</b> / 5
            </p>

            <p>
                🛏️ {hotel.bedrooms} Bedroom |
                {hotel.bed_type}
            </p>

            <p>
                🏨 {hotel.property_type}
            </p>

            <h2>₹{hotel.hotel_price} / night</h2>

            <p>{hotel.hotel_description}</p>

            <p>
                {" | ".join(facilities)}
            </p>

            <p>
                🍽️ {" | ".join(dining)}
            </p>

            {offer}

        </div>
        """

    # ---------------- FILTER UI ----------------

    return HttpResponse(f"""
    <html>

    <head>

        <title>Explore the World - Hotels</title>

    </head>

    <body style="
        font-family: Arial;
        background: #f5f7fa;
        margin: 0;
        padding: 30px;
    ">

        <h1 style="text-align:center;">
            🌍 Explore the World
        </h1>

        <h2 style="text-align:center;">
            Hotels
        </h2>


        <!-- SORTING -->

        <div style="
            text-align:center;
            margin:25px;
            padding:20px;
            background:white;
            border-radius:12px;
        ">

            <h3>🔽 Sorting</h3>

            <a href="?sort=price">
                S1 - Lowest Price → Highest Price
            </a>

            &nbsp;&nbsp;

            <a href="?sort=offer">
                S2 - Limited Time Offer
            </a>

            &nbsp;&nbsp;

            <a href="?sort=rating">
                S3 - Highest Rating
            </a>

        </div>


        <!-- FILTERS -->

        <div style="
            width:700px;
            margin:20px auto;
            padding:25px;
            background:white;
            border-radius:12px;
            box-shadow:0 3px 10px rgba(0,0,0,0.1);
        ">

            <h2>🔎 Filter Hotels</h2>

            <form method="get">

                <label>
                    Maximum Price:
                </label>

                <input
                    type="number"
                    name="max_price"
                    placeholder="Example: 1500"
                >

                <br><br>


                <label>
                    Minimum Rating:
                </label>

                <select name="rating">

                    <option value="">
                        Any Rating
                    </option>

                    <option value="4">
                        ⭐ 4+
                    </option>

                    <option value="4.5">
                        ⭐ 4.5+
                    </option>

                </select>

                <br><br>


                <label>
                    Property Type:
                </label>

                <select name="property_type">

                    <option value="">
                        Any
                    </option>

                    <option value="Hotel">
                        Hotel
                    </option>

                    <option value="Resort">
                        Resort
                    </option>

                    <option value="Guesthouse">
                        Guesthouse
                    </option>

                    <option value="Serviced Apartment">
                        Serviced Apartment
                    </option>

                </select>

                <br><br>


                <label>
                    Bed Type:
                </label>

                <select name="bed_type">

                    <option value="">
                        Any
                    </option>

                    <option value="Single Bed">
                        Single Bed
                    </option>

                    <option value="Double Bed">
                        Double Bed
                    </option>

                    <option value="Queen Bed">
                        Queen Bed
                    </option>

                    <option value="King Bed">
                        King Bed
                    </option>

                </select>

                <br><br>


                <label>
                    Minimum Bedrooms:
                </label>

                <input
                    type="number"
                    name="bedrooms"
                    min="1"
                    placeholder="Example: 2"
                >

                <br><br>

                <b>Facilities:</b>

                <br>

                <input type="checkbox" name="wifi">
                📶 Wi-Fi

                <br>

                <input type="checkbox" name="pool">
                🏊 Swimming Pool

                <br>

                <input type="checkbox" name="parking">
                🚗 Parking

                <br>

                <input type="checkbox" name="airport">
                ✈️ Airport Transfer

                <br>

                <input type="checkbox" name="gym">
                🏋️ Gym

                <br><br>


                <b>Dining:</b>

                <br>

                <input type="checkbox" name="breakfast">
                🍳 Breakfast

                <br>

                <input type="checkbox" name="lunch">
                🍽️ Lunch

                <br>

                <input type="checkbox" name="dinner">
                🌙 Dinner

                <br><br>


                <button type="submit">
                    🔍 Apply Filters
                </button>

                &nbsp;

                <a href="/hotels/">
                    Reset Filters
                </a>

            </form>

        </div>


        <!-- HOTEL RESULTS -->

        <h2 style="text-align:center;">
            Available Hotels
        </h2>

        {hotel_cards}

    </body>

    </html>
    """)
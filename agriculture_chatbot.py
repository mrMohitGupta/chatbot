from flask import Flask, request, jsonify

app = Flask(__name__)

# Placeholder data
crop_info = {
    "wheat": "Wheat is generally planted in late October to November and requires well-drained loamy soil.",
    "rice": "Rice grows best in flooded fields with temperatures between 20°C and 35°C."
}

market_prices = {
    "wheat": "₹2,500 per quintal",
    "rice": "₹3,000 per quintal"
}

# Placeholder weather data
weather_data = {
    "Delhi": "Sunny, 30°C",
    "Mumbai": "Rainy, 28°C"
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()

    # Weather query
    if "weather" in user_message:
        city = user_message.split("in")[-1].strip().capitalize()
        weather = weather_data.get(city, "Weather data not available for this location.")
        return jsonify({"reply": f"The weather in {city} is: {weather}"})
    
    # Crop information query
    elif "about" in user_message:
        crop = user_message.split("about")[-1].strip().lower()
        info = crop_info.get(crop, "Information about this crop is not available.")
        return jsonify({"reply": info})
    
    # Market price query
    elif "price" in user_message:
        crop = user_message.split("price of")[-1].strip().lower()
        price = market_prices.get(crop, "Price information is not available.")
        return jsonify({"reply": f"The current price of {crop} is: {price}"})
    
    # Default response
    else:
        return jsonify({"reply": "I'm sorry, I didn't understand that. Please ask about weather, crop info, or market prices."})

if __name__ == '__main__':
    app.run(debug=True)

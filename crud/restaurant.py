from flask import jsonify, redirect
from models import db, Restaurant

# GET all restaurants
def get_all_restaurants():
    all_restaurants = Restaurant.query.all()
    results = [restaurants.as_dict() for restaurants in all_restaurants] 
    return jsonify(results)

# GET a one restaurant
def get_restaurant(id):
  restaurant = Restaurant.query.get(id)
  if restaurant:
    return jsonify(restaurant.as_dict())
  else:
    raise Exception(f"Error getting restaurant at {id}")

#POST a new restaurant
def create_restaurant(name, menu, location, phone):
    new_restuarant = Restaurant(name=name, menu=menu, location=location, phone=phone)
    db.session.add(new_restuarant)
    db.session.commit()
    return jsonify(new_restuarant.as_dict())

# PUT a specific restaurant
def update_restuarant(id, name, menu, location, phone):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        restaurant.name = name or restaurant.name
        restaurant.menu = menu or restaurant.menu
        restaurant.location = location or restaurant.location
        restaurant.phone = phone or restaurant.phone
        db.session.commit()
        return jsonify(restaurant.as_dict())
    else:
        raise Exception(f"No restaurant at {id}")

# DELETE a restaurant
def destroy_restaurant(id):
  restaurant = Restaurant.query.get(id)
  if restaurant:
    db.session.delete(restaurant)
    db.session.commit()
    return redirect("/restaurants")
  else:
    raise Exception(f"No restaurant at {id}")
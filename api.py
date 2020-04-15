from flask import jsonify, request
from models import app, user_reviews
from crud.user import get_all_users, get_user, create_user, update_user, destroy_user
from crud.restaurant import get_all_restaurants, get_restaurant, create_restaurant, update_restuarant, destroy_restaurant
from crud.review import get_all_reviews, get_review, create_review, update_review, destroy_review

# Error handling route
@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error(f"Unhandled Exception: {e}")
    message = e.__str__()
    return jsonify(message=message.split(":")[0])

# Routes for users
@app.route("/users", methods=["GET", "POST"])
def user_all():
    if request.method == "GET":
        return get_all_users()
    if request.method == "POST":
        return create_user(request.form["name"], request.form["email"])

# Route for specific user
@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def user_specific(id):
    if request.method == "GET":
        return get_user(id)
    elif request.method == "PUT":
        name = request.form["name"]
        email = request.form["email"]
        return update_user(id, name, email)
    else:
        return destroy_user(id)

# Route for all restaurants
@app.route('/restaurants', methods=['GET', 'POST'])
def restsurant_index_create():
    if request.method == 'GET':
        return get_all_restaurants()
    if request.method == 'POST':
        return create_restaurant(request.form['name'], request.form['menu'], request.form['location'], request.form['phone'])

# Route for specific restaurant
@app.route('/restaurants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def specific_restaurant(id):
    if request.method == "GET":
        return get_restaurant(id)
    elif request.method == "PUT":
        name = request.form['name']
        menu = request.form['menu']
        location = request.form['location']
        phone = request.form['phone']
        return update_restuarant(id, name, menu, location, phone)

@app.route('/reviews', methods=['GET', 'POST'])
def review_index_create():
    if request.method == 'GET':
        return get_all_reviews()
    if request.method == 'POST':
        return create_review(request.form['header'], request.form['body'], request.form['owner'])

# Route for specific review
@app.route('/reviws/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def specific_review(id):
    if request.method == "GET":
        return get_review(id)
    elif request.method == "PUT":
        header = request.form['header']
        body = request.form['body']
        owner = request.form['owner']
        return update_review(id, header, body, owner)
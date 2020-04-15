from flask import jsonify, redirect
from models import db, Review

# GET all reviews
def get_all_reviews():
    all_reviews = Review.query.all()
    results = [reviews.as_dict() for reviews in all_reviews] 
    return jsonify(results)

# GET a one review
def get_review(id):
  review = Review.query.get(id)
  if review:
    return jsonify(review.as_dict())
  else:
    raise Exception(f"Error getting review at {id}")

#POST a new review
def create_review(header, body, owner):
    new_review = Review(header=header, body=body, owner=owner)
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.as_dict())

# PUT a specific review
def update_review(id, header, body, owner):
    review = Review.query.get(id)
    if review:
        review.header = header or review.header
        review.body = body or review.body
        review.owner = owner or review.owner
        db.session.commit()
        return jsonify(review.as_dict())
    else:
        raise Exception(f"No review at {id}")

# DELETE a review
def destroy_review(id):
  review = Review.query.get(id)
  if review:
    db.session.delete(review)
    db.session.commit()
    return redirect("/reviews")
  else:
    raise Exception(f"No review at {id}")
from flask import Blueprint, jsonify, request

from models import db, Quote

quotes_bp = Blueprint('quotes', __name__)

@quotes_bp.route('/add_quote', methods=['POST'])
def add_quote():
    data = request.get_json()
    new_quote = Quote(title=data['title'], description=data['description'])
    db.session.add(new_quote)
    db.session.commit()
    return jsonify({'message': 'Quote added successfully'}), 201

@quotes_bp.route('/get_quotes', methods=['GET'])
def get_quotes():
    quotes = Quote.query.all()
    quotes_list = [{'title': quote.title, 'description': quote.description} for quote in quotes]
    return jsonify({'quotes': quotes_list}), 200

@quotes_bp.route('/delete_all', methods=['DELETE'])
def delete_all_quotes():
    Quote.query.delete()
    db.session.commit()
    return jsonify({'message': 'All quotes deleted successfully'}), 200

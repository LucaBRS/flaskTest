from flask import Flask, jsonify
import os
import json

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

DB_URI = os.getenv('DB_URI')
engine = create_engine(DB_URI)
Base = declarative_base()

# Define the model for the gas_prices table
class GasPrice(Base):
    __tablename__ = 'gas_prices'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    gas = Column(Float, nullable=False)
    diesel = Column(Float, nullable=False)

    def __repr__(self):
        return f"<GasPrice(id={self.id}, name={self.name}, lat={self.lat}, lng={self.lng}, gas={self.gas}, diesel={self.diesel})>"

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

@app.route('/get_all_gas_prices')
def get_all_gas_prices():
    # Create a session
    session = Session()

    # Query all gas prices
    prices = session.query(GasPrice).all()

    # Serialize the results
    serialized_prices = [{
        'id': price.id,
        'name': price.name,
        'lat': price.lat,
        'lng': price.lng,
        'gas': price.gas,
        'diesel': price.diesel
    } for price in prices]

    # Close the session
    session.close()

    return jsonify(serialized_prices)

@app.route('/get_json')
def get_json():
    json_file_path = os.path.join(os.path.dirname(__file__), 'gas.json')
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    return jsonify(json_data)

if __name__ == '__main__':
    # the same port of the docker for python!
    app.run(host='0.0.0.0', port=8000, debug=True)

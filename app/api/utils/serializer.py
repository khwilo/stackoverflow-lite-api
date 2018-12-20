'''JSON serializer for objects'''
from datetime import date, time

def serialize(obj):
    '''Helper function to serialize an object'''
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, time):
        serial = obj.isoformat()
        return serial

    return obj.__dict__

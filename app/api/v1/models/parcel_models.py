""" This module holds classes to handle the parcel models methods """

parcels = []


class ParcelModels:
    """ This class contains methods that handle parcels """

    def __init__(self):
        self.db = parcels

    def create_parcel(self, user_id, title, weight, s_name, s_email, r_id_no,
                      r_email, pick_up, destination):
        id = len(self.db) + 1
        status = 'in transit'
        parcel = {
            'parcel_id': id,
            'title': title,
            'user_id': 1,
            'weight': weight,
            'bill': weight * 123,
            's_name': s_name,
            's_email': s_email,
            'r_id_no': r_id_no,
            'r_email': r_email,
            'pick_up': pick_up,
            'current_loc': pick_up,
            'destination': destination,
            'status': status
        }
        self.db.append(parcel)
        return {'message': 'Successfully created parcel'}

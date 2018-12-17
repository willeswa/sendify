""" This module holds classes to handle the parcel models methods """

parcels = [ {
            "bill": 12915,
            "current_loc": "Kibera",
            "destination": "gas",
            "parcel_id": 1,
            "pick_up": "Kibera",
            "r_email": "pwanjala@gmail.com",
            "r_id_no": "30197811",
            "s_email": "gwiliez@gmail.com",
            "s_name": " ",
            "status": "in transit",
            "title": "Dornish Wine",
            "user_id": 2,
            "weight": 105
        },
         {
            "bill": 12915,
            "current_loc": "Kibera",
            "destination": "gas",
            "parcel_id": 1,
            "pick_up": "Kibera",
            "r_email": "pwanjala@gmail.com",
            "r_id_no": "30197811",
            "s_email": "gwiliez@gmail.com",
            "s_name": " ",
            "status": "in transit",
            "title": "Dornish Wine",
            "user_id": 2,
            "weight": 105
        },
         {
            "bill": 12915,
            "current_loc": "Kibera",
            "destination": "gas",
            "parcel_id": 2,
            "pick_up": "Kibera",
            "r_email": "pwanjala@gmail.com",
            "r_id_no": "30197811",
            "s_email": "gwiliez@gmail.com",
            "s_name": " ",
            "status": "in transit",
            "title": "Dornish Wine",
            "user_id": 3,
            "weight": 105
        }]


class ParcelModels:
    """ This class contains methods that handle parcels """

    def __init__(self):
        self.db = parcels

    def create_parcel(self, user_id, title, weight, s_name, s_email, r_id_no,
                      r_email, pick_up, destination):
        """ creates a parcels """

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

    def get_all_parcels(self):
        """ allows users to get all data  """
        if len(self.db) == 0:
            return 'You have no existing parcels'
        else:
            return self.db

    def view_order_details(self, parcel_id):
        """ retrieves a specific parcel """
        if self.db:
            result = self.check_if_parcel_id_exists(parcel_id)
            return result
        else:
            return 'You have no existing parcels'

    def check_if_parcel_id_exists(self, parcel_id):
        """ Checks if a parcel with the given parcel id exists """
        for parcel in self.db:
            if parcel['parcel_id'] == parcel_id:
                return parcel

        return 'No parcel with ID {}'.format(parcel_id)

    def user_specific_parcels(self, user_id):
        """ Retrieves parcels that are for a specific user """
        user_parcels = []
        for parcel in self.db:
            if parcel['user_id'] == user_id:
                user_parcels.append(parcel)
        if user_parcels:
            return user_parcels
        else:
            return 'No Parcels by user {}'.format(user_id)
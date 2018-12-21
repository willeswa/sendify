""" This module holds classes to handle the parcel models methods """
from flask_restful import abort
from app.db_config import init_db


class ParcelModels:
    """ This class contains methods that handle parcels """

    def __init__(self):
        self.db = init_db()

    def create_parcel(self, title, rec_name, rec_email, address, postal_code, pick_up, weight):
        """ creates a parcels """

        id = len(self.db) + 1
        status = 'Pending Approval'.capitalize()
        s_name = 'Willies Wanjala'
        s_email = 'gwiliez@gmail.com'
        created_on = 'now'
        user_id = 1
        parcel = {
            'parcel_id': id,
            'title': title,
            'user_id': user_id,
            'weight': weight,
            'bill': 150 + (weight*100),
            'sender_name': s_name,
            'sender_email': s_email,
            'rec_name': rec_name,
            'rec_email': rec_email,
            'address': address,
            'postal_code': postal_code,
            'pick_up': pick_up,
            'current_loc': pick_up,
            'status': status,
            'created_on':created_on
        }
        self.db.append(parcel)
        return {'message': 'Successfully created parcel'}

    # def get_all_parcels(self):
    #     """ allows users to get all data  """
    #     if len(self.db) == 0:
    #         return 'You have no existing parcels'
    #     else:
    #         return self.db

    # def view_order_details(self, parcel_id):
    #     """ retrieves a specific parcel """
    #     if self.db:
    #         result = self.check_if_parcel_id_exists(parcel_id)
    #         return result
    #     else:
    #         return 'You have no existing parcels'

    # def check_if_parcel_id_exists(self, parcel_id):
    #     """ Checks if a parcel with the given parcel id exists """
    #     for parcel in self.db:
    #         if parcel['parcel_id'] == parcel_id:
    #             return parcel

    #     abort(404, message='Parcel with ID {} does not exist'.format(parcel_id))

    # def user_specific_parcels(self, user_id):
    #     """ Retrieves parcels that are for a specific user """
    #     user_parcels = []
    #     for parcel in self.db:
    #         if parcel['user_id'] == user_id:
    #             user_parcels.append(parcel)
    #     if user_parcels:
    #         return user_parcels
    #     else:
    #         return 'No Parcels by user {}'.format(user_id)

    # def cancel_parcel(self, parcel_id):
    #     result = self.view_order_details(parcel_id)
    #     if result['status'] == 'In transit':
    #         result['status'] = 'Canceled'
    #         print(result)
    #         return 'Successfully canceled parcel {}'.format(parcel_id)
    #     elif result['status'] == 'Delivered':
    #         return 'This parcel is already delivered, it cannot be canceled'
    #     else:
    #         return 'The parcel is already canceled'
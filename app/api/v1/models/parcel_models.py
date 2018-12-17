""" This module holds classes to handle the parcel models methods """

parcels = []


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
        result = self.check_if_parcel_id_exists(parcel_id)
        return result

    def check_if_parcel_id_exists(self, parcel_id):
        """ Checks if a parcel with the given parcel id exists """
        if parcels:
            for parcel in self.db:
                if parcel['parcel_id'] == parcel_id:
                    return parcel
                else:
                    return 'No parcel with ID {}'.format(parcel_id)
        else:
            return 'No parcel with ID {}'.format(parcel_id)

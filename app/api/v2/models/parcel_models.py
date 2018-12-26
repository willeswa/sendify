""" This module holds classes to handle the parcel models methods """
from flask_restful import abort
from app.db_config import Database
from flask_jwt_extended import get_jwt_identity

db = Database()


class ParcelModels:
    """ This class contains methods that handle parcels """

    def create_parcel(self, title, rec_name, rec_email, address, postal_code, pick_up, weight):
        """ creates a new parcel and inserts it into the db """
        current_user = get_jwt_identity()
        s_email = current_user['email']
        s_name = current_user['name']
        user_id = current_user['user_id']
        self.title = title
        self.rec_name = rec_name
        self.rec_email = rec_email
        self.address = address
        self.postal_code = postal_code
        self.pick_up = pick_up
        self.weight = weight
        self.sender_name = s_name
        self.sender_email = s_email
        self.user_id = user_id
        self.bill = 150 + (self.weight*100)

        with db as conn:
            query = """INSERT INTO parcels(title, sender_name, sender_email, rec_name, rec_email,
                        address, postal_code, pick_up, weight, bill, user_id)
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            curr = conn.cursor()
            curr.execute(query, (self.title, self.sender_name, self.sender_email, self.rec_name, self.rec_email,
                                 self.address, self.postal_code, self.pick_up, self.weight, self.bill, self.user_id))
            conn.commit()

        return 'Successfuly created parcel'

    def get_all_parcels(self):
        """ allows users to get all data  """

        current_user = get_jwt_identity()
        with db as conn:
            curr = conn.cursor()
            if current_user['admin']:
                query = """ SELECT title, sender_name, sender_email, rec_name, rec_email, address, postal_code, 
                        pick_up, current_location, weight, bill, status, created_on FROM parcels """
                columns = ('title', 'sender_name', 'sender_email', 'rec_name', 'rec_email', 'address', 'postal_code',
                           'pick_up', 'current_location', 'weight', 'bill', 'status', 'created_on')
                curr.execute(query)
                records = curr.fetchall()
                if records:
                    parcels = []
                    for record in records:
                        values = []
                        for value in record:
                            values.append(str(value))
                        parcels.append(dict(zip(columns, values)))
                    return parcels
                else:
                    return 'There are 0 parcels at the moment'
            else:
                return 'Not authorize to view this page'

    def get_user_specific_parcels(self, user_id):
        """ allows retrieval of user specific parcels """
        current_user = get_jwt_identity()
        if user_id == current_user['user_id']:
            with db as conn:
                curr = conn.cursor()
                query = """ SELECT title, rec_name, rec_email, address, postal_code, pick_up, current_location, 
                        weight, bill, status, created_on FROM parcels WHERE user_id = %s """
                columns = ('title', 'rec_name', 'rec_email', 'address', 'postal_code', 'pick_up', 'current_location',
                           'weight', 'bill', 'status', 'created_on')
                curr.execute(query, (user_id,),)
                records = curr.fetchall()
                if records:
                    parcels = []
                    values = []
                    for record in records:
                        for value in record:
                            values.append(str(value))
                        parcels.append(dict(zip(columns, values)))
                    return parcels
                else:
                    return 'You have 0 parcels at the moment'
        else:
            return 'Not authorized to view this page'


#     # def view_order_details(self, parcel_id):
#     #     """ retrieves a specific parcel """
#     #     if self.db:
#     #         result = self.check_if_parcel_id_exists(parcel_id)
#     #         return result
#     #     else:
#     #         return 'You have no existing parcels'

#     # def check_if_parcel_id_exists(self, parcel_id):
#     #     """ Checks if a parcel with the given parcel id exists """
#     #     for parcel in self.db:
#     #         if parcel['parcel_id'] == parcel_id:
#     #             return parcel

#     #     abort(404, message='Parcel with ID {} does not exist'.format(parcel_id))

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

#     # def cancel_parcel(self, parcel_id):
#     #     result = self.view_order_details(parcel_id)
#     #     if result['status'] == 'In transit':
#     #         result['status'] = 'Canceled'
#     #         print(result)
#     #         return 'Successfully canceled parcel {}'.format(parcel_id)
#     #     elif result['status'] == 'Delivered':
#     #         return 'This parcel is already delivered, it cannot be canceled'
#     #     else:
#     #         return 'The parcel is already canceled'

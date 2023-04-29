import mysql.connector

class TrainData:
    def __init__(self, username, password, host_name):
        self.dataBase = mysql.connector.connect(
            host = host_name,
            user = username,
            passwd = password,
            allow_local_infile = True,
            auth_plugin = 'mysql_native_password'
        )
        self.cursorObject = self.dataBase.cursor()

    def get_user_password(self, username):
        pass
    def set_user_data(self, username, password, first_name, second_name, email_id, phone_number, gender):
        pass
    def get_user_data(self, username):
        pass
    def get_employee_password(self, username):
        pass
    def set_employee_data(self, username, password, first_name, second_name, email_id, phone_number, gender):
        pass
    def get_user_data(self, username):
        pass
    def book_scheduled_train(self, train_id, departure_date_time, arrival_date_time, ac_seats, ac_seats_occupied, non_ac_seats, non_ac_seats_occupied):
        pass
    def check_seat_availibility (self, scheduled_id):
        pass
    def update_seat_availibility (self, ac_seats, non_ac_seats):
        pass
    def get_scheduled_train_details (self, date):
        pass
    def get_train_details (self, location):
        pass
 
# Get Available Scheduled Trains on Specifed Date Function
# Common Functions
# Get Train Details Function 
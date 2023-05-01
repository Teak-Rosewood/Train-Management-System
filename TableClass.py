import mysql.connector

class TrainData:
    def __init__(self, username, password, host_name):
        self.dataBase = mysql.connector.connect(
            host = host_name,
            user = username,
            passwd = password,
            allow_local_infile = True,
            auth_plugin = 'mysql_native_password',
            database = 'train_management'
        )
        self.cursorObject = self.dataBase.cursor()

    def get_user_password(self, username):
        query = """select * from tblUsers where username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])[2]
        else:
            return False
        
    def set_user_data(self, username, password, first_name, second_name, email_id, phone_number, gender):
        pass

    def get_user_data(self, username):
        query = """select * from tblUsers natural join tblUserDetails where username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])
        else:
            return False

    def get_employee_password(self, username):
        query = """select * from tblEmployees where username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])[2]
        else:
            return False
    
    def set_employee_data(self, username, password, first_name, second_name, email_id, phone_number, gender):
        pass
    
    def get_employee_data(self, username):
        query = """select * from tblEmployees natural join tblEmployeeDetails where username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])
        else:
            return False
    
    def book_scheduled_train(self, train_id, departure_date_time, arrival_date_time, ac_seats, ac_seats_occupied, non_ac_seats, non_ac_seats_occupied):
        pass

    def check_seat_availibility (self, scheduled_id):
        pass

    def update_seat_availibility (self, ac_seats, non_ac_seats):
        pass

    def get_scheduled_train_details (self, date):
        pass

    def get_train_details (self, startlocation = '', endlocation = ''):
        data = []
        if startlocation == '':
            query = """select * from tblTrains where end_location = %s"""
            parameters = (endlocation, )
            self.cursorObject.execute(query, parameters)
            data = self.cursorObject.fetchall()
        elif endlocation == '':
            query = """select * from tblTrains where start_location = %s"""
            parameters = (startlocation, )
            self.cursorObject.execute(query, parameters)
            data = self.cursorObject.fetchall()
        else:
            query = """select * from tblTrains where start_location = %s and end_location = %s"""
            parameters = (startlocation, endlocation)
            self.cursorObject.execute(query, parameters)
            data = self.cursorObject.fetchall()
        return data
 
traindata = TrainData('user', 'password', 'localhost')
#traindata.cursorObject.execute("insert into tblUsers values (null, 'saatwik', 'password')")
#traindata.dataBase.commit()
print(traindata.get_user_password('saatwik'))
#print(traindata.get_train_details(startlocation='Lokmanyatilak T', endlocation='Madgaon'))
# Get Available Scheduled Trains on Specifed Date Function
# Common Functions
# Get Train Details Function 
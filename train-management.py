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

    # Setting User data on registration
        
    def set_user_data(self, username, password, first_name, second_name, email_id, phone_number, gender):
        query = """insert into tblUsers values (%s, %s)"""
        parameters = (username, password)
        try:
            self.cursorObject.execute(query, parameters)
        except mysql.connector.Error as err:
            return err
        query = """insert into tblUserDetails values (%s, %s, %s, %s, %s, %s)"""
        parameters = (username, first_name, second_name, email_id, phone_number, gender)
        try:
            self.cursorObject.execute(query, parameters)
        except mysql.connector.Error as err:
            return err
        self.dataBase.commit()
        return True
    
    # Setting Employee data on Registration

    def set_employee_data(self, username, password, first_name, second_name, email_id, phone_number, gender):
        query = """insert into tblEmployees values (%s, %s)"""
        parameters = (username, password)
        try:
            self.cursorObject.execute(query, parameters)
        except mysql.connector.Error as err:
            return err
        query = """insert into tblEmployeeDetails values (%s, %s, %s, %s, %s, %s)"""
        parameters = (username, first_name, second_name, email_id, phone_number, gender)
        try:
            self.cursorObject.execute(query, parameters)
        except mysql.connector.Error as err:
            return err
        self.dataBase.commit()
        return True

    # Getting User Password to authenticate login

    def get_user_password(self, username):
        query = """select * from tblUsers where username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])[1]
        else:
            return False
        
    # Resetting User password on registration
        
    def set_user_password(self, username, password, new_password):
        temp_pass = self.get_user_password(username)
        if temp_pass == False:
            return False
        elif temp_pass == password:
            query = """update tblUsers
            set password = %s,
            where username = %s"""
            parameters = (new_password, username)
            try:
                self.cursorObject.execute(query, parameters)
            except mysql.connector.Error as err:
                return err
            self.dataBase.commit()
            return True
        else:
            return False
        
    # Getting Employee password to authenticate login

    def get_employee_password(self, username):
        query = """select * from tblEmployees where emp_username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])[1]
        else:
            return False
    
    # Resetting User password on registration
        
    def set_employee_password(self, emp_username, password, new_password):
        temp_pass = self.get_employee_password(emp_username)
        if temp_pass == False:
            return False
        elif temp_pass == password:
            query = """update tblEmployees
            set password = %s,
            where emp_username = %s"""
            parameters = (new_password, emp_username)
            try:
                self.cursorObject.execute(query, parameters)
            except mysql.connector.Error as err:
                return err
            self.dataBase.commit()
            return True
        else:
            return False

    # Getting User data to display on profile page

    def get_user_data(self, username):
        query = """select * from tblUsers natural join tblUserDetails where username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])
        else:
            return False

    # Getting Employee Data to display on profile page 

    def get_employee_data(self, username):
        query = """select * from tblEmployees natural join tblEmployeeDetails where emp_username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])
        else:
            return False
    
    # Scheduling a train with a special Schedule id
        
    def schedule_train(self, train_id, departure_data_time, arrival_date_time):
        query = """insert into tblTrainSchedules values (null, %s, %s, %s, 100, 0, 100, 0)"""
        parameters = (train_id, departure_data_time, arrival_date_time)
        try:
            self.cursorObject.execute(query, parameters)
        except mysql.connector.Error as err:
            print(err)
        self.dataBase.commit()
        query = """select schedule_id from tblTrainSchedules where train_id = %s"""
        parameters = (train_id,)
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return (data[0])[0]
        else:
            return False
    
    # Users to see how many seats on the train are left

    def check_seat_availibility (self, scheduled_id):
        query = """select non_ac_seats_occupied, ac_seats_occupied from tblTrainSchedules where schedule_id = %s"""
        parameters = (scheduled_id, )
        self.cursorObject.execute(query, parameters)
        data = self.cursorObject.fetchall()
        if len(data) > 0:
            return data[0]
        else:
            return False
    
    # Aids the booking procedure by updating the occupied seats on the train

    def update_seat_availibility (self, scheduled_id, ac_seats, non_ac_seats):
        query = """update tblTrainSchedules
        set ac_seats_occupied = ac_seats_occupied + %s,
        non_ac_seats_occupied = non_ac_seats_occupied + %s
        where schedule_id = %s"""
        parameters = (ac_seats, non_ac_seats, scheduled_id)
        try:
            self.cursorObject.execute(query, parameters)
        except mysql.connector.Error as err:
            return err
        self.dataBase.commit()
        return True
    
    # Booking a Scheduled Train
    
    def book_scheduled_train(self, scheduled_id, username, ac_seats, non_ac_seats):
        if self.update_seat_availibility(scheduled_id, ac_seats, non_ac_seats) == True:
            query = """insert into tblBookings values (null, %s, %s, %s, %s)"""
            parameters = (username, scheduled_id, ac_seats, non_ac_seats)
            try:
                self.cursorObject.execute(query, parameters)
            except mysql.connector.Error as err:
                return err
            self.dataBase.commit()
            query = """select booking_id from tblBookings where username = %s and schedule_id = %s"""
            parameters = (username, scheduled_id)
            self.cursorObject.execute(query, parameters)
            data = self.cursorObject.fetchall()
            if len(data) > 0:
                return (data[0])[0]
            else:
                return False
        else:
            return self.update_seat_availibility(scheduled_id, ac_seats, non_ac_seats)
    
    # Getting user Booking details to display on profile page
        
    def get_user_booking_details (self, username):
        query = """select * from tblBookings natural join tblTrainSchedules where username = %s"""
        parameters = (username, )
        self.cursorObject.execute(query, parameters)
        return self.cursorObject.fetchall()
        
    # Gets train details for a specific day, place

    def get_scheduled_train_details (self, date, startlocation = '', endlocation = ''):
        data = []
        if startlocation == '':
            query = """select * from tblTrainSchedules natural join tblTrains where end_location = %s"""
            parameters = (endlocation, )
            self.cursorObject.execute(query, parameters)
            data = self.cursorObject.fetchall()
        elif endlocation == '':
            query = """select * from tblScheduledTrains natural join tblTrains where start_location = %s"""
            parameters = (startlocation, )
            self.cursorObject.execute(query, parameters)
            data = self.cursorObject.fetchall()
        else:
            query = """select * from tblScheduledTrains natural join tblTrains where start_location = %s and end_location = %s"""
            parameters = (startlocation, endlocation)
            self.cursorObject.execute(query, parameters)
            data = self.cursorObject.fetchall()
        return data

    # Gets train details for a specific place

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
 

# Testing 

# traindata = TrainData('user', 'password', 'localhost')
# print(traindata.set_user_data('tempUser', 'password', 'tempUser', 'secon', 'tempUser@gmail.com', 9740225444, 'M'))
# print(traindata.set_employee_data('emp', 'password', 'em', 'p', 'emp@gmail.com', 9740225445, 'M'))
# print(traindata.get_user_password('tempUser'))
# print(traindata.get_employee_password('emp'))
# print(traindata.get_user_data('tempUser'))
# print(traindata.get_employee_data('emp'))
# schedule_id = traindata.schedule_train('111', '1998-01-23 12:45:56', '1998-01-23 14:45:56')
# print(schedule_id)
# print(traindata.check_seat_availibility(schedule_id))
# print(traindata.book_scheduled_train(schedule_id, 'tempUser', 5, 5))
# print(traindata.get_user_booking_details('tempUser'))

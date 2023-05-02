import mysql.connector

# Initialising Database

dataBase = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    allow_local_infile = True,
    auth_plugin='mysql_native_password'
)

# Defining Curser Object 

cursorObject = dataBase.cursor()

# User Tables

tblUser = """create table tblUsers (
    username varchar(20) unique primary key,
    password varchar(20)
)"""

tblUserDetails = """create table tblUserDetails (
    username varchar(20),
    first_name varchar(20),
    second_name varchar(20),
    email_id varchar(50),
    phone_number numeric(10),
    gender varchar(1),

    constraint FK_UserDetails_Users foreign key (username) references tblUsers(username),
    constraint CHK_valid_email_user check(email_id like '%@%.com'),
    constraint CHK_valid_phone_number_user check(phone_number >= 1000000000 and phone_number <= 9999999999),
    constraint CHK_valid_gender_user check(gender in ('F', 'M', 'O'))
)"""

# Employee Tables

tblEmployees = """create table tblEmployees (
    emp_username varchar(20) unique primary key,
    password varchar(20)
)"""

tblEmployeeDetails = """create table tblEmployeeDetails (
    emp_username varchar(20),
    first_name varchar(20),
    second_name varchar(20),
    email_id varchar(50),
    phone_number numeric(10),
    gender varchar(1),

    constraint FK_UserDetails_Employees foreign key (emp_username) references tblEmployees(emp_username),
    constraint CHK_valid_email_employee check(email_id like '%@%.com'),
    constraint CHK_valid_phone_number_employee check(phone_number >= 1000000000 and phone_number <= 9999999999),
    constraint CHK_valid_gender_employee check(gender in ('F', 'M', 'O'))
)"""

# Train table 

tblTains_create = """create table tblTrains (
    train_id numeric(10) primary key,
    num numeric(5),
    train_name varchar(50),
    start_location varchar(50),
    end_location varchar(50)
)"""

tblTrains_adddata = """load data local infile '~/Documents/train_management/dataset/All_Indian_Trains.csv'
into table tblTrains
fields terminated by ','
ignore 1 rows"""

tblTains_deletecol = """alter table tblTrains
drop column num"""

# Train Schedule Table

tblTrainSchedules = """create table tblTrainSchedules (
    schedule_id int unsigned not null auto_increment primary key,
    train_id numeric(10),
    departure_date_time datetime,
    arrival_date_time datetime,
    ac_seats int, 
    ac_seats_occupied int,
    non_ac_seats int, 
    non_ac_seats_occupied int,

    constraint FK_Trains_TrainSchedule foreign key (train_id) references tblTrains(train_id),
    constraint CHK_valid_train_time check (departure_date_time < arrival_date_time),
    constraint CHK_valid_seating check((ac_seats > ac_seats_occupied) and (non_ac_seats > non_ac_seats_occupied))
)"""

# Train Bookings Table

tblBookings = """create table tblBookings (
    booking_id int unsigned not null auto_increment primary key,
    username varchar(20),
    schedule_id int unsigned not null,
    ac_seats_alloted int,
    non_ac_seats_alloted int,

    constraint FK_Users_Bookings foreign key (username) references tblUsers(username),
    constraint FK_TrainSchedules_Bookings foreign key (schedule_id) references tblTrainSchedules(schedule_id)
)"""

# User reset password

tblResetPassword = """create table tblResetPassword (
    username varchar(20),
    security_code varchar(20),

    constraint FK_Users_ResetPassword foreign key (username) references tblUsers(username),
)"""

# Table creation

cursorObject.execute("create database train_management")
cursorObject.execute("use train_management")
cursorObject.execute(tblUser)
cursorObject.execute(tblUserDetails)
cursorObject.execute(tblEmployees)
cursorObject.execute(tblEmployeeDetails)
cursorObject.execute(tblTains_create)
cursorObject.execute(tblTrains_adddata)
cursorObject.execute(tblTains_deletecol)
cursorObject.execute(tblTrainSchedules)
cursorObject.execute(tblBookings)
cursorObject.execute(tblResetPassword)




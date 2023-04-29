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
    user_id int unsigned not null auto_increment primary key,
    username varchar(20) unique,
    password varchar(20),

    constraint UC_username_user unique(user_id, username)
)"""

tblUserDetails = """create table tblUserDetails (
    user_id int unsigned not null,
    first_name varchar(20),
    second_name varchar(20),
    email_id varchar(50),
    phone_number varchar(50),
    gender varchar(1),

    constraint FK_UserDetails_Users foreign key (user_id) references tblUsers(user_id),
    constraint CHK_valid_email_user check(email_id like '%@%.com'),
    constraint CHK_valid_phone_number_user check(phone_number like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    constraint CHK_valid_gender_user check(gender in ('F', 'M', 'O'))
)"""

# Employee Tables

tblEmployees = """create table tblEmployees (
    employee_id int unsigned not null auto_increment primary key,
    username varchar(20) unique,
    password varchar(20),

    constraint UC_username_employee unique(employee_id, username)
)"""

tblEmployeeDetails = """create table tblEmployeeDetails (
    employee_id int unsigned not null,
    first_name varchar(20),
    second_name varchar(20),
    email_id varchar(50),
    phone_number varchar(50),
    gender varchar(1),

    constraint FK_UserDetails_Employees foreign key (employee_id) references tblEmployees(employee_id),
    constraint CHK_valid_email_employee check(email_id like '%@%.com'),
    constraint CHK_valid_phone_number_employee check(phone_number like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    constraint CHK_valid_gender_employee check(gender in ('F', 'M', 'O'))
)"""

# Train table 

tblTains_create = """create table tblTrains (
    num numeric(5),
    train_id numeric(10) primary key,
    train_name varchar(50),
    start_location varchar(50),
    end_location varchar(50)
)"""

tblTrains_adddata = """load data local infile '/home/saatwik/Documents/trains_project/All_Indian_Trains.csv'
into table tblTrains
fields terminated by ','
ignore 1 rows"""

tblTains_deletecol = """alter table tblTrains
drop column num"""

# Train Schedule Table

tblTrainSchedules = """create table tblTrainSchedules (
    schedule_id int unsigned not null auto_increment primary key,
    train_id numeric(10) unique,
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
    user_id int unsigned not null,
    schedule_id int unsigned not null,
    ac_seats_alloted int,
    non_ac_seats_alloted int,

    constraint FK_Users_Bookings foreign key (user_id) references tblUsers(user_id),
    constraint FK_TrainSchedules_Bookings foreign key (schedule_id) references tblTrainSchedules(schedule_id)
)"""

# Table creation

cursorObject.execute("create database training")
cursorObject.execute("use training")
cursorObject.execute(tblUser)
cursorObject.execute(tblUserDetails)
cursorObject.execute(tblEmployees)
cursorObject.execute(tblEmployeeDetails)
cursorObject.execute(tblTains_create)
cursorObject.execute(tblTrains_adddata)
cursorObject.execute(tblTains_deletecol)
cursorObject.execute(tblTrainSchedules)
cursorObject.execute(tblBookings)




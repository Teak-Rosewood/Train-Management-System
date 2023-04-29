-- User Tables

create table tblUsers (
    user_id int unsigned not null auto_increment primary key,
    username varchar(20) unique,
    password varchar(20),

    constraint UC_username_user unique(user_id, username)
);

create table tblUserDetails (
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
);

-- Employee Tables 

create table tblEmployees (
    employee_id int unsigned not null auto_increment primary key,
    username varchar(20) unique,
    password varchar(20),

    constraint UC_username_employee unique(employee_id, username)
);

create table tblEmployeeDetails (
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
);

-- Train table 

create table tblTrains (
    num numeric(5),
    train_id numeric(10) primary key,
    train_name varchar(50),
    start_location varchar(50),
    end_location varchar(50)
);

load data local infile '/home/saatwik/Documents/trains_project/All_Indian_Trains.csv'
into table tblTrains
fields terminated by ','
ignore 1 rows;

alter table tblTrains
drop column num;

-- Schedule Table

create table tblTrainSchedules (
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
);

-- Bookings Table 

create table tblBookings (
    booking_id int unsigned not null auto_increment primary key,
    user_id int unsigned not null,
    schedule_id int unsigned not null,
    ac_seats_alloted int,
    non_ac_seats_alloted int,

    constraint FK_Users_Bookings foreign key (user_id) references tblUsers(user_id),
    constraint FK_TrainSchedules_Bookings foreign key (schedule_id) references tblTrainSchedules(schedule_id)
);

-- Employee Functions

-- Employee_id password Function 

select * from tblEmployees where ()

-- Get Employee Details Function 
select * from tbl
-- Set Employee Details Function 

-- Schedule Train Function


-- User Functions

-- Username Password Function

-- Get User Details Function 

-- Set User Details Function 

-- Book Scheduled Train Function 

-- Check Seat Availability Function

-- Update Seat Availability Function

-- Get Available Scheduled Trains on Specifed Date Function


-- Common Functions

-- Get Train Details Function 

insert into tblUsers values(null, 'saatwik', 'password');
insert into tblEmployees values (null, 'aansh', 'hello123');
insert into tblEmployeeDetails values (1, 'aansh', 'basu', 'hello@gmail.com', '9740225444', 'M');
# Railway Management System

A comprehensive Python-Tkinter application for managing railway operations, including user registration, authentication, train scheduling, and ticket booking. This project demonstrates the implementation of a multi-user system with role-based access control using a GUI-based interface and Oracle database integration.


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Application Modules](#application-modules)
- [Project Architecture](#project-architecture)
- [Database Schema](#database-schema)
- [Implementation Details](#implementation-details)
  - [Authentication System](#authentication-system)
  - [Manager Module](#manager-module)
  - [Booking System](#booking-system)
  - [Data Persistence](#data-persistence)
- [User Interface Walkthrough](#user-interface-walkthrough)
- [Setup Instructions](#setup-instructions)
- [Dependencies](#dependencies)
- [Usage Guide](#usage-guide)
- [Code Structure](#code-structure)
- [System Design Patterns](#system-design-patterns)
- [Learning Outcomes](#learning-outcomes)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Railway Management System is a desktop application built with Python and Tkinter that provides a complete solution for railway operations management. It features a multi-user system with different access levels (admin/manager and regular users), allowing administrators to manage train schedules and routes while enabling passengers to search for trains and book tickets.

The application uses a modular architecture with separate components for authentication, administration, and booking functions, all of which interact with an Oracle database to store and retrieve data.

## Features

- **User Authentication & Registration**: Secure login system with registration for new users
- **Admin/Manager Interface**: Complete control panel for managing train routes, schedules, and station information
- **Ticket Booking System**: User-friendly interface for searching and booking train tickets
- **Real-time Data Validation**: Input validation for all forms to ensure data integrity
- **Database Integration**: Oracle database connection for persistent data storage
- **Attractive UI**: Modern, responsive interface with intuitive navigation
- **Role-based Access Control**: Different interfaces and permissions for users and administrators

## Application Modules

The application consists of the following main modules:

1. **Login Module**: Handles user authentication with username and password verification
2. **Registration Module**: Allows new users to create accounts with personal details
3. **Manager Module**: Administrative interface for managing train routes and schedules
4. **Booking Module**: User interface for searching and booking train tickets

Each module is implemented as a separate Python file to maintain code organization and separation of concerns.

## Project Architecture

The project follows a layered architecture with the following components:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│                  Presentation Layer                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │  Login UI   │  │ Manager UI  │  │ Booking UI  │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│                   Business Logic                    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │   Auth      │  │Train Route  │  │ Ticket      │  │
│  │ Controller  │  │ Controller  │  │ Controller  │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│                    Data Access                      │
│              ┌─────────────────────┐               │
│              │   Oracle Database   │               │
│              │     Connection      │               │
│              └─────────────────────┘               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Flow Diagram

```
┌──────────┐     ┌──────────┐
│  Start   │────▶│  Login   │
└──────────┘     └────┬─────┘
                      │
                      ▼
              ┌───────────────┐     ┌──────────────┐
              │ User Login?   │ No  │ Registration │
              └───────┬───────┘────▶│    Form      │
                      │ Yes         └──────┬───────┘
                      │                    │
                      ▼                    │
         ┌────────────────────┐            │
         │ Check User Type    │◀───────────┘
         └────────┬───────────┘
                  │
          ┌───────┴───────┐
          ▼               ▼
  ┌───────────────┐  ┌────────────┐
  │ Manager Panel │  │ User Panel │
  └───────┬───────┘  └─────┬──────┘
          │                │
          ▼                ▼
  ┌───────────────┐  ┌────────────┐
  │ Manage Routes │  │ Book Ticket│
  └───────────────┘  └────────────┘
```

## Database Schema

The system uses an Oracle database with the following main tables:

### Tables

1. **REGISTRATION** - Stores user account information
   ```
   CREATE TABLE registration (
     first_name VARCHAR2(50),
     last_name VARCHAR2(50),
     contact_number VARCHAR2(15),
     email VARCHAR2(100) PRIMARY KEY,
     gender VARCHAR2(10),
     age NUMBER,
     password VARCHAR2(50)
   );
   ```

2. **MANAGER** - Stores train route information
   ```
   CREATE TABLE manager (
     from_ VARCHAR2(50),
     to_ VARCHAR2(50),
     train_no VARCHAR2(20) PRIMARY KEY,
     station_code VARCHAR2(10),
     arrival_time VARCHAR2(10),
     departure_time VARCHAR2(10)
   );
   ```

3. **TICKET** - Stores ticket booking information
   ```
   CREATE TABLE ticket (
     ticket_no VARCHAR2(20) PRIMARY KEY,
     from_ VARCHAR2(50),
     to_ VARCHAR2(50),
     train_no VARCHAR2(20),
     station_code VARCHAR2(10),
     arrival_time VARCHAR2(10),
     departure_time VARCHAR2(10),
     FOREIGN KEY (train_no) REFERENCES manager(train_no)
   );
   ```

### Entity Relationship Diagram

```
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│  REGISTRATION │          │    MANAGER    │          │    TICKET     │
├───────────────┤          ├───────────────┤          ├───────────────┤
│ first_name    │          │ from_         │          │ ticket_no     │
│ last_name     │          │ to_           │          │ from_         │
│ contact_number│          │ train_no (PK) │◀─────────│ to_           │
│ email (PK)    │          │ station_code  │    │     │ train_no (FK) │
│ gender        │          │ arrival_time  │    │     │ station_code  │
│ age           │          │ departure_time│    │     │ arrival_time  │
│ password      │          └───────────────┘    │     │ departure_time│
└───────────────┘                               │     └───────────────┘
                                                │
                                                │
                                           Foreign Key
                                           Relationship
```

## Implementation Details

### Authentication System

The authentication system (implemented in `login.py` and `register.py`) manages user access to the application:

- **Login**: Validates user credentials against the database and directs users to appropriate interfaces based on their role
- **Registration**: Collects and validates user information, ensures username uniqueness, and stores data securely
- **Password Reset**: Allows users to reset forgotten passwords using a verification process

Key features:
- Input validation to ensure data integrity
- Username uniqueness checking
- Special handling for manager/admin accounts
- Password confirmation to prevent typographical errors

#### Login Process

```python
def login(self):
    if self.txt_username.get() == "" or self.txt_pass_.get() == "":
        messagebox.showerror("Error","All fields are required",parent=self.root)
    else:
        try:
            con = cx_Oracle.connect("railway/railway007")
            cur = con.cursor()

            em = self.txt_username.get()
            ps = self.txt_pass_.get()
            cur.execute("select * from registration where email = :email and password = :password",
                       {'email':em, 'password':ps})
            row = cur.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "Invalid EMAIL or PASSWORD", parent=self.root)
            elif self.txt_username.get() == "Manager007@gmail.com" and self.txt_pass_.get() == "manager007":
                messagebox.showinfo("Success", "Welcome", parent=self.root)
                self.root.destroy()
                import manager
            else:
                messagebox.showinfo("Success","Welcome",parent=self.root)
                self.root.destroy()
                import Booking
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)
```

### Manager Module

The Manager Module (`manager.py`) provides an administrative interface for managing train routes, schedules, and related information:

- **Train Route Management**: Add, update, and delete train routes
- **Search Functionality**: Find specific train information using various search criteria
- **Data Visualization**: Tabular view of all train routes and schedules

Key functionalities:
- CRUD operations for train routes
- Validation for route data
- Integration with the Oracle database for persistent storage
- Filtering and searching capabilities

#### Train Route Management

```python
def add_train_info(self):
    if self.From_var.get() == "" or self.To_var.get() == "" or self.TrainNo_var.get() == "" or self.St_Code_var.get() == "" or self.A_Time_var.get == "" or self.D_Time_var.get() == "":
        messagebox.showerror("Error","All fields are required")
    else:
        con = cx_Oracle.connect("railway/railway007")
        cur = con.cursor()
        cur.execute("insert into manager values (:1,:2,:3,:4,:5,:6)",
                   (
                       self.From_var.get(),
                       self.To_var.get(),
                       self.TrainNo_var.get(),
                       self.St_Code_var.get(),
                       self.A_Time_var.get(),
                       self.D_Time_var.get()
                   ))
        con.commit()
        self.fetch_data_to_searchby()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")
```

### Booking System

The Booking System (`Booking.py`) allows users to search for and book train tickets:

- **Train Search**: Find trains between specified stations
- **Ticket Booking**: Book tickets for selected trains
- **Ticket Confirmation**: Generate and display ticket information

Key features:
- User-friendly interface for finding train routes
- Train selection from available options
- Ticket generation with unique ticket numbers
- Booking confirmation with ticket details

#### Ticket Booking Process

```python
def add_train_info(self):
    if self.From_var.get() == "" or self.To_var.get() == "" or self.TrainNo_var.get() == "" or self.St_Code_var.get() == "" or self.A_Time_var.get == "" or self.D_Time_var.get() == "":
        messagebox.showerror("Error","All fields are required")
    else:
        self.ticket_no = str(random.randint(100,10000)) + str(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        con = cx_Oracle.connect("railway/railway007")
        cur = con.cursor()
        cur.execute("insert into ticket (ticket_no,from_,to_,train_no,station_code,arrival_time,departure_time) values (:1,:2,:3,:4,:5,:6,:7)",
                   (
                       self.ticket_no,
                       self.From_var.get(),
                       self.To_var.get(),
                       self.TrainNo_var.get(),
                       self.St_Code_var.get(),
                       self.A_Time_var.get(),
                       self.D_Time_var.get()
                   ))
        con.commit()
        con.close()
        messagebox.showinfo("TICKET NUMBER", "Your Ticket Number is "+self.ticket_no)
        messagebox.showinfo("Success","Train has been booked")
        self.root.destroy()
```

### Data Persistence

The application uses Oracle Database for data persistence with the following key features:

- **Connection Management**: Efficient database connection handling
- **Prepared Statements**: Protection against SQL injection
- **Transaction Management**: Proper commit and rollback mechanics
- **Error Handling**: Comprehensive error capture and user-friendly messages

## User Interface Walkthrough

### Login Screen

The login screen provides access to the application with username and password fields and navigation to the registration p

Key components:
- Username and password fields
- Login button
- Registration link
- Forgot password option
- Animated clock display

### Registration Screen

The registration screen allows new users to create accounts:


Key components:
- Personal information fields
- Password and confirmation
- Terms and conditions acceptance
- Submit button
- Navigation back to login

### Manager Dashboard

The manager dashboard enables administrators to manage train routes and schedules:


Key components:
- Form for adding/editing train routes
- Data table showing all routes
- Search functionality
- CRUD operation buttons

### Booking Interface

The booking interface allows users to search for and book train tickets:


Key components:
- Origin and destination fields
- Train selection
- Booking form
- Search results table

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Oracle Database (11g or higher)
- Oracle client libraries (cx_Oracle dependencies)
- Tkinter (usually included with Python)
- PIL/Pillow (Python Imaging Library)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arshnoor-Singh-Sohi/railway-management-tkinter.git
   cd railway-management-tkinter
   ```

2. **Install required Python packages**
   ```bash
   pip install cx_Oracle pillow
   ```

3. **Set up Oracle Database**
   - Install Oracle Database (11g or higher)
   - Create a user 'railway' with password 'railway007'
   - Run the included database setup script:
   ```sql
   CREATE TABLE registration (
     first_name VARCHAR2(50),
     last_name VARCHAR2(50),
     contact_number VARCHAR2(15),
     email VARCHAR2(100) PRIMARY KEY,
     gender VARCHAR2(10),
     age NUMBER,
     password VARCHAR2(50)
   );

   CREATE TABLE manager (
     from_ VARCHAR2(50),
     to_ VARCHAR2(50),
     train_no VARCHAR2(20) PRIMARY KEY,
     station_code VARCHAR2(10),
     arrival_time VARCHAR2(10),
     departure_time VARCHAR2(10)
   );

   CREATE TABLE ticket (
     ticket_no VARCHAR2(20) PRIMARY KEY,
     from_ VARCHAR2(50),
     to_ VARCHAR2(50),
     train_no VARCHAR2(20),
     station_code VARCHAR2(10),
     arrival_time VARCHAR2(10),
     departure_time VARCHAR2(10),
     FOREIGN KEY (train_no) REFERENCES manager(train_no)
   );
   ```

4. **Configure database connection**
   - Ensure the connection string in the Python files matches your Oracle database setup
   - Default: `cx_Oracle.connect("railway/railway007")`

5. **Run the application**
   ```bash
   python login.py
   ```

## Dependencies

The application relies on the following external libraries:

- **cx_Oracle**: For Oracle database connectivity
- **Tkinter**: For the graphical user interface
- **PIL/Pillow**: For image handling and processing
- **Random**: For generating unique ticket numbers

## Usage Guide

### For Users

1. **Launch the application** by running `login.py`
2. **Log in** with your registered credentials
   - If you don't have an account, click on "Register New Account"
3. **Search for trains** by entering departure and destination stations
4. **Select a train** from the search results
5. **Book a ticket** by filling in the required information
6. **Receive a confirmation** with your ticket number

### For Administrators

1. **Launch the application** by running `login.py`
2. **Log in** with manager credentials (default: Manager007@gmail.com/manager007)
3. **Manage train routes** through the manager interface:
   - Add new train routes
   - Update existing routes
   - Delete routes
   - Search for specific train information

## Code Structure

The project is organized into the following main Python files:

- **login.py**: Handles user authentication and navigation to appropriate interfaces
- **register.py**: Manages user registration and account creation
- **manager.py**: Provides the administrative interface for train management
- **Booking.py**: Implements the ticket booking functionality for users
- **railway_mgr.py**: Alternative implementation of the manager interface

### Key Classes

1. **Login Class**: Manages authentication and user redirection
2. **Register Class**: Handles user registration and validation
3. **Manager Class**: Implements train route management functions
4. **Booking Class**: Provides ticket booking capabilities

### Common Patterns

Throughout the codebase, you'll find several recurring design patterns:

1. **Form Validation**: Consistent input validation across all forms
2. **Database Interaction**: Standardized approach to database operations
3. **Event Handling**: Consistent approach to Tkinter event management
4. **Message Display**: Standardized user notifications using messagebox

## System Design Patterns

The application implements several key design patterns:

1. **MVC Pattern**: Separation of data model, user interface, and control logic
2. **Singleton Pattern**: Single database connection instance
3. **Factory Pattern**: Creation of appropriate user interfaces based on user role
4. **Observer Pattern**: UI updates in response to data changes

## Learning Outcomes

This project demonstrates proficiency in:

1. **GUI Development**: Creating user-friendly interfaces with Tkinter
2. **Database Integration**: Connecting to and managing Oracle databases
3. **Authentication Systems**: Implementing secure user authentication
4. **CRUD Operations**: Creating, reading, updating, and deleting database records
5. **Input Validation**: Ensuring data integrity through validation
6. **Error Handling**: Providing user-friendly error messages
7. **OOP Principles**: Applying object-oriented programming concepts

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Ensure Oracle is running
   - Verify connection string parameters
   - Check that user 'railway' exists with password 'railway007'

2. **Missing Images**
   - Make sure the 'images' folder is in the correct location
   - Verify image file names and paths

3. **User Registration Issues**
   - Ensure all fields are filled correctly
   - Check that the email address is not already registered

### Error Handling

The application includes comprehensive error handling throughout:

```python
try:
    # Database operation or other code that might fail
    con = cx_Oracle.connect("railway/railway007")
    # ...
except Exception as es:
    messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)
finally:
    if con:
        con.close()
```

## Future Enhancements

Potential improvements for future versions:

1. **Enhanced Security**: Password hashing and stronger authentication
2. **Responsive Design**: Better adaptation to different screen sizes
3. **Payment Integration**: Add payment processing for ticket purchases
4. **User Profiles**: Allow users to manage their information and view booking history
5. **Seat Selection**: Enable users to select specific seats when booking
6. **Email Notifications**: Send booking confirmations via email
7. **Report Generation**: Generate detailed reports for administrators
8. **Data Analytics**: Add insights on popular routes and booking patterns

## Contributing

Contributions to improve the Railway Management System are welcome! To contribute:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Commit your changes**: `git commit -m 'Add some feature'`
5. **Push to the branch**: `git push origin feature/your-feature-name`
6. **Submit a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2023 Arshnoor Singh Sohi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# ---------------------------------------------------------- #
# Title: TestHarness.py
# Description: A main module for testing
# ChangeLog (Who,When,What):
# PCoonrad,6.15.2020,Created started script
# PCoonrad,6.15.2020,Added test Data module
# PCoonrad,6.15.2020,Added test processing module
# PCoonrad,6.15.2020,Added test IO module
# ---------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only!
    from ProcessingClasses import FileProcessor as Fp # Processing classes
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())

# -------------------------------------------------------------------------
# Database Connection
# if __name__ == "__main__":
#     import DataClasses, IOClasses, ProcessingClasses  # Will error if the modules are not found
# else:
#     raise Exception("This file was not created to be imported")
#
# import ProcessingClasses as dp
#
# db_con = None
#
# try:  # Connect
#     db_con = dp.create_connection('C:/DataFiles/test.db')
#     print("Connected!")
# except Exception as e:
#     print(e)
#
# try:  # Create
#     db.create_demo_table(db_con)
#     print("Table created!")
# except Exception as e:
#     print(e)
#
# try:  # Insert
#     db.insert_demo_data(db_con, 3, "CCC")
#     print("Data inserted!")
# except Exception as e:
#     print(e)
#
# try:  # Select
#     rows = db.select_demo_data(db_con)
#     for row in rows:
#         print(row)
#     print("Data selected!")
# except Exception as e:
#     print(e)
#
# try:  # Update
#     db.update_demo_data(db_con, 3, "CC")
#     rows = dp.select_demo_data(db_con)
#     for row in rows:
#         print(row)
#     print("Data updated!")
# except Exception as e:
#     print(e)
#
# try:  # Delete
#     db.delete_demo_data(db_con, 3)
#     rows = dp.select_demo_data(db_con)
#     for row in rows:
#         print(row)
#     print("Data deleted!")
# except Exception as e:
#     print(e)
#
# db_con.close

# Test for importing Person class
# if __name__ == "__main__":
#     import DataClasses as D  # Data classes
#     import ProcessingClasses as P # Processing classes
# else:
#     raise Exception("This file was not created to be imported")
#
# # Test data module
# objP1 = D.Person("Bob", "Smith")
# objP2 = D.Person("Sue", "Jones")
# lstTable = [objP1, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))
#
# # Test processing module
# P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
# lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
# lstTable.clear()
# for row in lstFileData:
#     p = D.Person(row[0], row[1])
#     print(p.to_string(), type(row), type(p))
#     lstTable.append(p)
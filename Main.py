# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# PCoonrad,6.15.2020,Added Main Body of Script
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
lstTable = []
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
Eio.print_current_list_items(lstTable)

while (True):
    # Show user a menu of options
    Eio.print_menu_items()

    # Get user's menu option choice
    choice = Eio.input_menu_options()

    # Show current employee data
    if choice.strip() == '1':
        Eio.print_current_list_items(lstTable)
        continue  # to show the menu

    # Add new employee data
    elif choice.strip() == '2':
        lstTable.append(Eio.input_employee_data())
        continue  # to show the menu

    # Save employee data to File
    elif choice.strip() == '3':  # Save data to file
        Fp.save_data_to_file("EmployeeData.txt", lstTable)
        continue

    # Exit Program
    elif choice.strip() == '4':
            print("Goodbye!")
    break  # and Exit
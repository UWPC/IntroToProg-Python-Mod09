# ---------------------------------------------------------- #
# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PCoonrad,6.15.2020,Added FileProcessor class
# PCoonrad,6.15.2020,Added DatabaseProcessor class
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """
    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
            print("Data successfully saved to file!")
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

# class DatabaseProcessor:
#     # TODO: Add code to process to and from a database
    """Processes data to (writes) and from (reads) a database file:

    methods:
        create_connection(db_file):
        create_demo_table(con):
        insert_demo_data(con, ID, Name):
        update_demo_data(con, ID, Name):
        delete_demo_data(con, ID):
        select_demo_data(con):

    changelog: (When,Who,What)
        PCoonrad,6.15.2020,Created Class
    """

    def create_connection(db_file):
        """ Open or create database

        :param db_file:
        :return: con
        """
        try:
            con = sqlite3.connect(db_file)  # This opens OR creates the database
        except Exception as e:
            raise e
        return con

    def create_demo_table(con):
        try:
            csr = con.cursor()  # A cursor object allows you to submit commands
            csr.execute("CREATE TABLE Demo (ID [integer], Name [text]);")
        except Exception as e:
            raise e

    def insert_demo_data(con, ID, Name):
        try:
            csr = con.cursor()  # A cursor object allows you to submit commands
            csr.execute("INSERT INTO Demo (ID, Name) values (?,?);", [ID, Name])  # ? is a parmeter
            csr.execute("commit;")  # Adding this to use SQLite3
            csr.close()  # To close the cursor when done
        except Exception as e:
            raise e

    def update_demo_data(con, ID, Name):
        try:
            csr = con.cursor()  # A cursor object allows you to submit commands
            csr.execute("Update Demo Set Name = ? Where ID = ?;", [ID, Name])  # ? is a parmeter
            csr.execute("commit;")  # Adding this to use SQLite3
            csr.close()  # To close the cursor when done
        except Exception as e:
            raise e

    def delete_demo_data(con, ID):
        try:
            csr = con.cursor()  # A cursor object allows you to submit commands
            csr.execute("Delete From Demo Where ID = ?;", [ID])  # ? is a parmeter
            csr.execute("commit;")  # Adding this to use SQLite3
            csr.close()  # To close the cursor when done
        except Exception as e:
            raise e

    def select_demo_data(con):
        try:
            csr = con.cursor()  # A cursor object allows you to submit commands
            csr.execute("SELECT ID, Name FROM Demo;")
            rows = csr.fetchall()  # fetchall puts all of the rows from the result into a list
            csr.close()  # To close the cursor when done
        except Exception as e:
            raise e

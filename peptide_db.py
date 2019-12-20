import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import aa_nt


def show_table(name):
    query = "SELECT * FROM {}".format(name)
    cursor.execute(query)
    for entry in cursor:
        print(entry)
    print("\n\n")


def search(table, entry):
    query = "SELECT * FROM {}".format(table)
    data = pd.read_sql(query, cnx)
    if entry in data.name.values:
        print(data.loc[data['name'] == entry])
    else:
        print(entry + " not in table\n")


def export(table, filename):
    query = "SELECT * FROM {}".format(table)
    data = pd.read_sql(query, cnx)
    data.to_csv(path_or_buf=filename)


def batch_update(filename, table):
    query = "SELECT * FROM {}".format(table)
    current_data = pd.read_sql(query, cnx)
    new_data = pd.read_csv(filename)
    frames = [current_data, new_data]
    combined_data = pd.concat(frames, sort=False)
    print(combined_data)

    # duplicates = combined_data[combined_data.duplicated(subset=['name', 'peptide_seq'])]
    # print(duplicates)
    # duplicates.to_csv(path_or_buf='duplicates.csv')

    combined_data.drop_duplicates(inplace=True, subset=['name'])
    combined_data.to_csv(path_or_buf='combined.csv')

    df = pd.read_csv('combined.csv')
    df.to_sql(table, con=engine, if_exists='replace')

 # add which column is duplicated (name or peptide sequencd
 # add amino acid position column
 # add effect type column
def compare(filename, table):
    query = "SELECT * FROM {}".format(table)
    current_data = pd.read_sql(query, cnx)
    new_data = pd.read_csv(filename)
    frames = [current_data, new_data]
    combined_data = pd.concat(frames, sort=False).reset_index()

    duplicates = combined_data[combined_data.duplicated(subset=['name', 'peptide_seq'])]
    duplicates.to_csv(path_or_buf='duplicates.csv')

    frames2 = [duplicates, new_data]
    new_entries = pd.concat(frames2, sort=False)
    new_entries = new_entries.drop_duplicates(subset=['name', 'peptide_seq'], keep=False)
    new_entries.to_csv(path_or_buf='new_entries.csv')


def create_table(table, filename):
    query = "CREATE TABLE {} (name VARCHAR(255) NOT NULL)".format(table)
    "   peptide_seq VARCHAR(255) NOT NULL,"
    "   oligo VARCHAR(255) NOT NULL,"
    "   oligo_seq VARCHAR(255) NULL,"
    "   IVTT_version VARCHAR(255) NULL,"
    "   oligo_location VARCHAR(255) NULL,"
    "   oligo_buffer VARCHAR(255) NULL,"
    "   oligo_concentration VARCHAR(255) NULL,"
    "   oligo_vendor VARCHAR(255) NULL,"
    "   oligo_date VARCHAR(255) NULL,"
    "   peptide VARCHAR(255) NOT NULL,"
    "   peptide_location VARCHAR(255) NULL,"
    "   peptide_buffer VARCHAR(255) NULL,"
    "   peptide_concentration VARCHAR(255) NULL,"
    "   origin VARCHAR(255) NOT NULL,"
    "   peptide_vendor VARCHAR(255) NULL,"
    "   peptide_date VARCHAR(255) NULL,"
    "   person VARCHAR(255) NULL"
    ")"

    cursor.execute(query)
    df = pd.read_csv(filename)
    print(df)
    df.to_sql(table, con=engine, if_exists='replace')

if __name__ == "__main__":
    cnx = mysql.connector.connect(user='root', password="#peptideDB19",
                                  host='localhost', port='3306', database='peptides')
    cursor = cnx.cursor()
    engine = create_engine('mysql+mysqlconnector://root:#peptideDB19@localhost:3306/peptides', echo=False)
    command = ""

    while command != "Q":
        command = input("What would like to do?\n(P)rint table\n(E)xport to csv\n(U)pdate\n(CR)eate Table\n(C)ompare\n(R)un conversions\n(S)earch\n(Q)uit\n").upper()
        if command == "P":
            table_name = input("Enter name of table\n")
            show_table(table_name)
        if command == "E":
            table = input("Enter name of table\n")
            filename = input("Enter name of file to export to\n")
            export(table, filename)
        if command == "U":
            update_file = input("Enter name of file to update from\n")
            table_name = input("Enter table name to update\n")
            batch_update(update_file, table_name)
        if command == "C":
            update_file = input("Enter name of file to compare\n")
            table_name = input("Enter table name to compare with\n")
            compare(update_file, table_name)
        if command == "CR":
            new_table_name = input("Enter name of new table\n")
            source_file = input("Enter name of file containing data\n")
            create_table(new_table_name, source_file)
        if command == "S":
            table = input("Enter table to search\n")
            search_entry = input("Enter name, peptide sequence, or oligo sequence to search for\n")
            search(table, search_entry)
        if command == "R":
            pepfile = input("Enter pepfile name\n")
            version = input("Enter version\n")
            aa_nt.aa_nt(pepfile, version)

    cursor.close()
    cnx.close()

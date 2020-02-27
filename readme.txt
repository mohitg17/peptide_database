Purpose
This script provides MySQL database management and cross checking functionality between csv files and a MySQL table.

General Usage
1. Run the script (no arguments)
    Ex: python peptide_db.py

2. User will be prompted in console to select function by typing corresponding letter
    Ex: What would like to do?
	(P)rint table
	(E)xport to csv
	(U)pdate
	(CR)eate Table
	(C)ompare
	(R)un conversions
	(S)earch
	(Q)uit

	>> P	(print table)

3. Enter table and file names as prompted
    Ex: Enter name of table
	>> peptide	(name of existing MySQL table)

4. Type Q to quit


Functions
  Print table
	Prints out all values stored in given MySQL table to console
	
	Example Run:

	What would you like to do? 
	...
	>> P
	Enter name of table
	>> test		(name of existing MySQL table)
	('B_BM2_1.1', 'VLSDNMEVL', 'TRUE', 'ATGGACGACGACGACAAGGTTCTGTCTGACAACATGGAAGTTCTGTAACGAAGCACCTCGCTAAAAAAAAAAAAAAAAAAAAAAAAA'...)
	('B_BM2_27.1', 'HFMAWTIGHL', 'TRUE', 'ATGGACGACGACGACAAGCACTTCATGGCTTGGACCATCGGTCACCTGTAACGAAGCACCTCGCTAAAAAAAAAAAAAAAAAAAAAAAAA'...)
	.........

  Export to csv
	Exports MySQL table to csv file

	Example Run:
	
	What would you like to do?
	...
	>> E
	Enter name of table
	>> test			(name of existing MySQL table)
	Enter name of file to export to
	>> table_values.csv	(new csv filename)

	*** file created in wokring directory called 'table_values.csv' containing all values from table ***

  Update
	Adds all non-duplicate entries in csv file to MySQL table

	Example Run:

	What would you like to do?
	...
	>> U
	Enter name of file to update from
	>> new_values.csv	(name of csv file containing data)
	Enter table name to update
	>> test			(name of existing MySQL table)

	*** Prints out updated table to console ***

  Create Table
	Creates new table from csv file containing the follow columns: name, peptide_seq, oligo, oligo_seq, IVTT_version, oligo_location, oligo_buffer, oligo_concentration, oligo_vendor, oligo_date, peptide, peptide_location, peptide_buffer, peptide_concentration, origin, amino acid position, effect type, peptide_vendor, peptide_date, person
	*** name, peptide_seq, oligo, origin columns must have values ***

	Example Run:

	What would you like to do?
	...
	>> CR
	Enter name of new table
	>> new_table		(new name of table)
	Enter name of file containing data
	>> test.csv		(name of csv file containing data)

	*** Prints out new table to console ***
  
  Compare
	Compare values in csv file to values in MySQL table. Creates 'duplicates.csv' and 'new_entries.csv' in working directory.

	Example Run:

	What would you like to do?
	...
	>> C
	Enter name of file to compare
	>> csv_values.csv	(name of csv file containing set of data)
	Enter table name to compare with
	>> test
    
	*** Ignore SettingWithCopyWarning. If script prompts user, function was successful. ***

  Run Conversions
	Convert peptide sequences into revcomp nucleotide sequence. Output is csv file containing the following columns: name, pep_seq, nt_seq, revcomp

	Example Run:
	
	What would you like to do?
	...
	>> R
	Enter source file name
	>> test.csv 	(name of file containing peptide sequences in second column)
	Enter name of file to create
	>> conversions.csv
	Enter version (V1, V2, V3, B)
	>> V1

	*** csv file containing revcomp is created in working directory ***

  Search
	Search MySQL table for specific peptide using name, peptide sequence, or oligo sequence

	Example Run:

	What would you like to do?
	...
	>> S
	Enter table to search
	>> test		(name of MySQL table to search)
	Enter name, peptide sequence, or oligo sequence to search for
	>> B_BM2_1.1
	
	*** Prints out row from MySQL table with corresponding name or sequence if found

  Quit
	Ends script


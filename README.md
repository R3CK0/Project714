#Project714

This command is useful to run a sql script from a bash shell to execute the script \n
mysql -u username -p database_name < mysqlscript.sql

use this command to drop a table into a sql file
mysqldump -u username -p my_database my_table > my_table_dump.sql


This command is usefull to run the evaluation script

python evaluation_script.py <path_to_prediction> <path_to_gold>
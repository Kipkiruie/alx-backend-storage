0x01-NoSQL
This project involves using MongoDB to perform various tasks. Below are the steps and scripts to complete the tasks mentioned.

Task 0: List All Databases
Write a script that lists all databases in MongoDB.

Create a file named 0-list_databases with the following content:

sh
Copy code
#!/bin/bash
echo "show dbs" | mongo
Make the script executable:

sh
Copy code
chmod +x 0-list_databases
Run the script to list all databases:

sh
Copy code
./0-list_databases
Task 1: Create or Use a Database
Write a script that creates or uses the database my_db.

Create a file named 1-use_or_create_database with the following content:

sh
Copy code
#!/bin/bash
echo "use my_db" | mongo
Make the script executable:

sh
Copy code
chmod +x 1-use_or_create_database
Run the script to create or use the my_db database:

sh
Copy code
./1-use_or_create_database
Setting Up MongoDB on Ubuntu 18.04
Import the MongoDB public GPG key:

sh
Copy code
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
Create a list file for MongoDB:

sh
Copy code
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
Reload the local package database:

sh
Copy code
sudo apt-get update
Install the MongoDB packages:

sh
Copy code
sudo apt-get install -y mongodb-org
Start MongoDB:

sh
Copy code
sudo systemctl start mongod
Verify that MongoDB has started:

sh
Copy code
sudo systemctl status mongod
Enable MongoDB to start on boot:

sh
Copy code
sudo systemctl enable mongod
Example Commands
To list all databases:

sh
Copy code
./0-list_databases
To create or use the my_db database:

sh
Copy code
./1-use_or_create_database
By following these steps, you can set up MongoDB on Ubuntu 18.04 and complete the tasks for the 0x01-NoSQL project. If you need further assistance or encounter any issues, feel free to ask!








OPI-LC-simply
Quickly and easily build OPI-LC
One-click setup for OPI light nodes
If you find it difficult to understand, just download it directly
image
Unzip
Skipping steps 2 and 3

# Step 1
Download Python and PostgreSQL
Python download link (for Windows 64-bit): https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe
(Be sure to check "Add Python to PATH" on the first page during installation to add Python to the system globally)
PostgreSQL download link: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

# Step 2
Download https://github.com/bestinslot-xyz/OPI-LC
and unzip it
As shown in the image
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/523a3d22-d15e-4238-a083-033e1c610ba4)   

# Step 3
Go to https://github.com/ganzhoumengnan/OPI-LC-simply/blob/main/main-en.py
Download main.py
Place the main.py file in the OPI-LC/brc20/sqlite directory after unzipping
As shown in the image
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/059d9de6-51bc-44bc-9f7d-c9fc0ac58dcd)   

# Step 4
In the OPI-LC/brc20/sqlite directory, click on the navigation bar
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/d0466a7c-1a9b-411c-8f2d-0aa57d93ef4e)  
Enter CMD and press Enter

![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/7b18c23c-95b6-486f-ba82-dcfa567b462e)  

# Step 5
Enter the following command in the cmd: python main.py  
If you are using main-en.py please usr this code:python main-en.py

![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/02ea7911-2463-4690-9a12-c5058facdc6d)  

# Step 6
Wait for the installation of various dependencies, and press Enter after the installation is complete
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/2c301387-1213-40d2-a530-31c220a1fdef)  

# Step 7
At this step, you can wait, or if you find it troublesome, just enter 1. The script will automatically download the database. If you find it slow, go to the address in the instructions to download, then paste the file into the same directory as this script
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/b3fb6609-4c7f-4fe2-8f1c-df3c83cbcc6f)  

# Step 8
If you are reopening the script, enter 0; otherwise, it will delete some already unzipped files and unzip them again. If it is your first time, enter 1
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/d81490fe-d1ff-409f-b641-c46ea7887043)  

# Step 9
If you have already configured the .env file, follow the prompts to skip; otherwise, press Enter to continue
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/acd90e5b-7806-41c1-9e36-cbcf7267f12e)  

# Step 10
Start syncing nodes. If you close it, to continue syncing next time, open cmd in the current directory and enter: python brc20_light_client_sqlite.py

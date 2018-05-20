# Item-Catalog

This folder contains the necessary program files to generate run catalog web
application.

## Contents

1. database_setup.py
    * Python file the defines and creates itemcatalog.db.
2. items_data.py
    * Python file used to populate itemcatalog.db.
3. application.py
    * Python file to run item catalog application.
4. templates
    * main.html
    * catalog.html
    * items.html
    * publicitems.html
    * description.html
    * publicdescription.html
    * additem.html
    * edititem.html
    * deleteitem.html
    * login.html
5. static
    * style.css
6. client_secrets.json
    * file containing authorization key for google sign-in

## Installation

This project can be run on a Linux-based virtual machine that comes pre-installed with the PostgreSQL database, python and other necessary software.

1. Download the following software to run the project.
    * Download VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).Install the platform package for your operating system. No need to download the extension package or SDK.There is also no need to launch VirtualBox.
    * Download "Vagrant" from the following git repository.
        * ```git clone https://github.com/udacity/fullstack-nanodegree-vm```
    * On your Terminal navigate to  "fullstack-nanodegree-vm" folder cloned from the above GIT repository. Navigate to vagrant subdirectory.
        * ```cd vagrant```
    * Use the following command to clone the project repository.
        * ```git clone https://github.com/shilpamadini/item-catalog.git```
3. Run the following commands to install the required software.
    * Navigate to the "vagrant" directory where above mentioned software is downloaded.
    * To install the Linux VM. Run the following command.
        * ```vagrant up```
    * Once Vagrant up is finished running,run the following command to login to VM
        * ```vagrant ssh```
    * All the files in "vagrant" directory on your terminal will appear in the "/vagrant" directory on the VM
    *  At the VM shell prompt
        * ```cd /vagrant/catalog```
        * ```python database_setup.py```
        * ```python items_data.py```
        * ```python application.py```
        * ```\q``` to go back to shell prompt
    * Open any internet browser window and connect to host.
        * ```http://localhost:8000```

## Functionality

    1. Connecting http://localhost:8000 will open the item catalog application.
    2. Website displays book categories and the latest items added to the database.
    3. When a user not logged in all catalogs and their corresponding items are displayed. Add item and edit/delete item options are not available.
    3. A login button enables users to login to the database. Authorization is verified using Google Plus sign-in.
    4. All the new users are automatically logged into the database.
    5. Once a user is logged-in add item privileges are provided.
    6. User is provided edit and delete privileges only to the items created by the user.

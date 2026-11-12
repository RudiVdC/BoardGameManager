# **BoardGameManager**



###### **Overview**



BoardGameManager is a command-line application developed in Python to manage a personal board game collection.



The application allows users to add, view, search, update and remove board games. It stores the information in an SQLite database and can export the collection to a CSV file.



The project was developed as part of a Python programming course at VIVES.



###### 

###### **Features**



**View board games:** Display all board games in alphabetical order.



**Add board games:** Add new games, including their publisher and game details.



**Search board games:** Search and filter the collection to find a specific game.



**Update board games:** Modify existing game information.



**Remove board games:** Delete games from the collection after confirmation.



**Export to CSV:** Export the board game collection to a CSV file.



**Data validation:** Validate user input, including player counts, playing time, year and game status.



**Database storage:** Store board games and publishers in an SQLite database.



Each board game has the following information:



* Name
* 
* Publisher
* 
* Minimum number of players
* 
* Maximum number of players
* 
* Playing time
* 
* Release year
* 
* Collection status



Available statuses are Owned, Wishlist, Played and For Sale.



###### 

###### **Project structure**



The project is organized into separate packages to keep the code structured and maintainable.



BoardGameManager/

│

├── main.py

├── database\_example.db

├── config.example.json

├── requirements.txt

├── README.md

├── .gitignore

│

├── ui/

│   └── \_\_init\_\_.py

│

├── data\_access/

│   └── \_\_init\_\_.py

│

├── domain/

│   └── \_\_init\_\_.py

│

└── service/

&#x20;   └── \_\_init\_\_.py



**main.py:** Entry point of the application. Starts the application and displays the main menu.



**ui:** Handles user interaction through the command line.



**data\_access:** Handles communication with the SQLite database.



**domain:** Contains the classes representing the application's data, such as BoardGame and Publisher.



**service:** Contains the application's business logic and validation.



**database\_example.db:** Sample SQLite database containing example board games and publishers.



**config.example.json:** Example configuration file used to configure the database location.



Each package contains additional Python modules.



###### 

###### **Requirements**



Python 3



No additional Python packages are required. The application uses Python's standard library, including SQLite support.



###### 

###### Installation and setup



1\. Clone the repository



&#x09;Clone the repository from GitHub:



&#x09;git clone <repository-url>



&#x09;Navigate to the project directory:



&#x09;cd BoardGameManager



2\. Create a virtual environment



&#x09;Create a virtual environment:



&#x09;python -m venv venv



&#x09;Activate the virtual environment on Windows:



&#x09;.\\venv\\Scripts\\Activate.ps1



3\. Install dependencies



&#x09;Install the required packages:



&#x09;pip install -r requirements.txt



&#x09;The project currently does not require additional packages.



4\. Configure the database



&#x09;The application uses a JSON configuration file to determine the location of the SQLite database.



&#x09;Copy config.example.json and rename the copy to config.json.



&#x09;The example configuration points to the sample database:



&#x09;{

&#x20;   	    "database\_path": "database\_example.db"

&#x09;}



&#x09;You can change the database location by editing the database\_path value.



&#x09;For example, to use a separate local database:



&#x09;{

&#x20;	    "database\_path": "data/boardgames.db"

&#x09;}



&#x09;The application creates the database directory if it does not exist and initializes the required database tables when necessary.



&#x09;Important: config.json is a local configuration file and is not included in the Git repository. Only config.example.json is provided.



5\. Run the application



&#x09;Start the application from the project root directory:



&#x09;python main.py



&#x09;The main menu will appear in the terminal.



###### 

###### **Database**



The application uses SQLite and contains two tables:



**Publishers**



Stores publisher information.



id: Unique publisher ID.



name: Publisher name.



**Board games**



Stores the board game information.



id: Unique board game ID.



name: Board game name.



publisher\_id: Reference to the publisher.



min\_players: Minimum number of players.



max\_players: Maximum number of players.



playing\_time: Playing time in minutes.



year: Release year.



status: Collection status.



The relationship between the two tables ensures that multiple board games can be associated with the same publisher.



A sample database (database\_example.db) is included in the repository so the application can be tested immediately.





###### **CSV export**



The application can export the board game collection to a CSV file.



The export includes the board game details and publisher information. The records are sorted alphabetically by game name.



The CSV file uses a semicolon (;) as the delimiter and UTF-8 with BOM encoding to improve compatibility with spreadsheet applications such as Microsoft Excel.



###### 

###### **Version control**



Git was used throughout development to track changes and document the development process.



The repository includes a .gitignore file to exclude files that should not be committed, such as:



The virtual environment.



Python cache files.



Local configuration files.



Local SQLite database files.



The sample database and example configuration file are included in the repository.



###### 

###### **Author**



Rudi Van de Casteele



Developed as a project for VIVES, Programming in Python.


1 .Features
Full CRUD operations (Create, Read, Update, Delete) External API integration (OpenFoodFacts) Import products from external API into local inventory CLI interface for easy interaction Mock database using Python list Error handling for invalid requests

2 .project structure 


├── app.py
├── cli.py
├── Pipfile
├── Pipfile.lock
└── README.md

3 .Installations and Setup
a.Clone the Repository
git clone https://github.com/angvela/inventory-management
cd inventory-project
b.Create virtual environment
pipenv shell
c.Install packages
pipenv install flask request pytest
d.Run The Application
🔹Start Flask server;

python app.py
e. Run CLI application
🔹Open a new terminal:

python cli.py
4.API Endpoints
🔹 Inventory Routes

GET /inventory/Get all items
GET /inventory/ / Get single item POST /inventory/ Add new item
PATCH /inventory// Update item
DELETE /inventory/ Delete item

🔹 External API Routes GET/search//Search product in OpenFoodFacts POST/import// Import product into inventory

5 .CLI Features
🔹CLI allows users to:

1. View All
2. View One
3. Add Item
4. Update Item
5. Delete Item
6. Search API
7. Import from API
8. Exit
🔹 External API Used . OpenFoodFacts API . Used to fetch real product data like: . Product name . Brand . Ingredients

6 .Technologies Used
Python
Flask
Requests
Pytest
OpenFoodFacts API
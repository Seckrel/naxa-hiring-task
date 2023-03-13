# Project README

This project is a Django-based web application that allows users to filter and view project data using API endpoints. This README file provides instructions for setting up and running the project.

# Prerequisites

To run this project, you will need the following:

- Python 3 installed on your system
- pipenv package installed (optional)
- Postman or any other API testing tool

# Installation

Follow the steps below to set up the project on your local machine:

1. Clone the repository or download the source code.
2. Navigate to the project root directory.
3. Create a new virtual environment using venv or pipenv.
4. Activate the virtual environment.
5. Install the required packages using the command pip install -r requirements.txt.
6. Running the server

To run the Django server, navigate to the project root directory and run the following command:


```
python manage.py runserver
```


The server should start running on http://127.0.0.1:8000/.


# Uploading a CSV file

To upload a CSV file, use a tool like Postman and send a `POST` request to the `/api/v1/upload/` endpoint. Attach the CSV file to the request body with the key `fileName`. The server will parse the CSV file and save the data to the database.

Filtering projects

To filter project data, use the `/api/v1/projects/` endpoint. You can apply filters by appending query parameters to the URL. For example, to filter projects by sector name, use the following URL:

```
/api/v1/projects/?project_sector__sector_name__icontains=Health
```

This will return all projects that have a sector name containing the word "Health".

# Summary of projects

To get a summary of projects, use the `/api/v1/summary/` endpoint. You can apply filters by appending query parameters to the URL. For example, to get a summary of projects with a sector name containing the word "agriculture", use the following URL:

```
/api/v1/summary/?project_sector__sector_name__icontains=agriculture
```

This will return a summary of projects that have a sector name containing the word "agriculture".

# Sector-based summary of projects

To get a sector-based summary of projects, use the /`api/v1/count-projects-budget/` endpoint. You can apply filters by appending query parameters to the URL. For example, to get a sector-based summary of projects in a district called "Surkhet", use the following URL:

```
/api/v1/count-projects-budget/?municipality__district__district_name__icontains=Surkhet
```

This will return a sector-based summary of projects in the district "Surkhet".
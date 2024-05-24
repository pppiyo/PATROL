
# PATROL App API
## Introduction
 This is a FastAPI application for the PATROL Application. It provides endpoints to perform various operations related to student check-ins, posts, and accessing historical data.

# Setup
## Requirements
* Python 3.7+
* MongoDB

## Installation

* Install dependencies:
Navigate to the project directory and install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
* Set up environment variables:
Ensure you have MongoDB installed and running.
Set MONGODB_URL environment variable to your MongoDB connection string.
* Run the FastAPI server:
Start the FastAPI server using the following command:
```bash 
uvicorn main:app --reload
```
# Usage
 * Add CheckIn student:
Endpoint to add a check-in record for a student.
* List all checkIns:
Endpoint to retrieve a list of all check-in records.
* Add Post:
Endpoint to add a new post.
* List posts:
Endpoint to retrieve a list of all posts.
* Update CheckIn:
Endpoint to update the check-in details of a student.
* List history:
Endpoint to retrieve historical data within a specified date range.
* Seed All Data:
Endpoint to seed historical data from an external API.

# Environment Variables
* MONGODB_URL: MongoDB connection string.
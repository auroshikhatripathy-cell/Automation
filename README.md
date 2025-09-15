## API Data Injection Scripts for Skillioz
### Description
This repository contains two Python scripts, JobsInjection.py and CandidateInjection.py, designed to populate the Skillioz test API (https://test-api.skillioz.com) with a large volume of sample data.

The scripts leverage multithreading to send concurrent API requests, making them efficient tools for stress testing, database seeding, or creating a realistic development environment.

### Features
Bulk Data Creation: Generate a specified range of job and candidate records.

Concurrent API Requests: Utilizes ThreadPoolExecutor to send multiple API requests in parallel, significantly speeding up the data injection process.

Dynamic Data Generation: Creates semi-realistic data for each record by randomly selecting from predefined lists of skills, cities, job titles, etc.

Interactive: Prompts the user for necessary inputs like the API authentication token and the desired range of records to create.

### Prerequisites
Before running the scripts, ensure you have the following installed:

Python 3.x

The requests and num2words Python libraries.

### Installation
Clone this repository or download the JobsInjection.py and CandidateInjection.py files.

Install the required Python packages using pip:

Bash

pip install requests num2words
### Usage
To run the scripts, navigate to the directory containing the files in your terminal and execute them using the python command.

1. To Inject Job Data
Run the JobsInjection.py script to create multiple job postings.

Bash

python JobsInjection.py
The script will then prompt you for the following information:

Enter token value: Your valid authentication token for the API.

Enter number of threads: Note: This input is currently ignored in the script, which is hardcoded to use 10 threads.

Enter low range: The starting number for the data generation loop (e.g., 1).

Enter high range: The exclusive ending number for the loop (e.g., entering 100 will create records from 1 to 99).

2. To Inject Candidate Data
Run the CandidateInjection.py script to create multiple candidate profiles.

Bash

python CandidateInjection.py
This script will ask for the same prompts as the job injection script.

Script Details
JobsInjection.py
Endpoint: POST https://test-api.skillioz.com/job/create

Purpose: Creates job postings with randomly generated details.

Payload Format: The script sends the payload as form data (data=...).

Key Generated Fields: category, city, companyName, country, jobLocation, jobTitle, jobType, skillset, yearOfExperience.

CandidateInjection.py
Endpoint: POST https://test-api.skillioz.com/candidate/create

Purpose: Creates candidate profiles with randomly generated names, contact information, skills, and professional details.

Payload Format: The script sends the payload in JSON format (json=...).

Key Generated Fields: name, email, mobileNo, skills, year_of_experience, designation.

Important Notes
API Token: A valid authentication token is required for the API requests to be successful. Invalid tokens will result in authorization errors.

Hardcoded Thread Count: Both scripts prompt for a number of threads but are currently hardcoded to use a maximum of 10 worker threads (ThreadPoolExecutor(max_workers=10)). To change the level of concurrency, you must modify this value directly in the script files.

Target Environment: These scripts are specifically configured to target the https://test-api.skillioz.com endpoints.

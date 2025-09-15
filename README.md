# API Data Injection Scripts for Skillioz

This repository contains two Python scripts, `JobsInjection.py` and `CandidateInjection.py`, designed to populate the Skillioz test API (`https://test-api.skillioz.com`) with a large volume of sample data.

The scripts leverage **multithreading** to send concurrent API requests, making them efficient tools for stress testing, database seeding, or creating a realistic development environment.

---

## Features 

* **Bulk Data Creation**: Generate a specified range of job and candidate records.
* **Concurrent API Requests**: Utilizes `ThreadPoolExecutor` to send multiple API requests in parallel, significantly speeding up the data injection process.
* **Dynamic Data Generation**: Creates semi-realistic data for each record by randomly selecting from predefined lists of skills, cities, job titles, etc.
* **Interactive**: Prompts the user for necessary inputs like the **API authentication token** and the desired range of records to create.

---

## Prerequisites

Before running the scripts, ensure you have the following installed:

* Python 3.x
* The `requests` and `num2words` Python libraries.

---

## Installation

1.  Clone this repository or download the `JobsInjection.py` and `CandidateInjection.py` files.

2.  Install the required Python packages using `pip`:
    ```bash
    pip install requests num2words
    ```

---

## Usage

To run the scripts, navigate to their directory in your terminal and execute them using the `python` command.

### To Inject Job Data

Run the `JobsInjection.py` script to create multiple job postings.

```bash
python JobsInjection.py 
```

To Inject Candidate Data
Run the CandidateInjection.py script to create multiple candidate profiles.

Bash

python CandidateInjection.py
After running either script, you will be prompted for:

API Token: Your valid authentication token.

Number of Threads: The number of concurrent threads.

Low Range: The starting number for the data generation loop (e.g., 1).

High Range: The exclusive ending number for the loop (e.g., 100 will create records from 1 to 99).

Script Details
JobsInjection.py
Endpoint: POST https://test-api.skillioz.com/job/create

Purpose: Creates job postings with randomly generated details like company name, job title, skills, and location.

Payload Format: The script sends the payload as form data.

CandidateInjection.py
Endpoint: POST https://test-api.skillioz.com/candidate/create

Purpose: Creates candidate profiles with random names, contact information, skills, and experience.

Payload Format: The script sends the payload in JSON format.

Important Notes ⚠
API Token: You must provide a valid authentication token for the API requests to be successful.

Hardcoded Thread Count: Both scripts ask for a number of threads but are hardcoded to use a maximum of 10 worker threads. To change the concurrency, you must modify the max_workers=10 value directly in the script files.

Target Environment: These scripts are configured specifically for the https://test-api.skillioz.com endpoint.

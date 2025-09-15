# Skillioz Data Injection Scripts

This repository contains two Python scripts for injecting **candidate** and **job** data into the [Skillioz Test API](https://test-api.skillioz.com).

- `CandidateInjection.py`: Creates fake candidate profiles with randomized details.
- `JobsInjection.py`: Creates fake job postings with randomized details.

Both scripts use **multithreading** to generate bulk data efficiently.

---

## Features

- Randomized candidate and job data generation.
- Uses `ThreadPoolExecutor` for concurrent API requests.
- Configurable number of threads and data range.
- Accepts token dynamically at runtime for authentication.

---

## Files

### 1. `CandidateInjection.py`
- Injects candidate profiles with:
  - Name (e.g., *candidate one, candidate two*).
  - Email (unique per candidate).
  - Mobile number.
  - Skills (random selection from predefined list).
  - Years of experience.
  - Designation.

Endpoint:  
```http
POST https://test-api.skillioz.com/candidate/create
````

---

### 2. `JobsInjection.py`

* Injects job postings with:

  * Company name.
  * Job title, type, and location.
  * City, country.
  * Skills required.
  * Years of experience.
  * Start and end date.
  * Priority and notes.

Endpoint:

```http
POST https://test-api.skillioz.com/job/create
```

---

## Requirements

Install dependencies before running:

```bash
pip install requests num2words
```

---

## Usage

Run either script:

```bash
python CandidateInjection.py
```

or

```bash
python JobsInjection.py
```

You will be prompted for:

* **Token value** → API token for authentication.
* **Number of threads** → Concurrency level.
* **Low range** → Starting index for data generation.
* **High range** → Ending index for data generation.

Example:

```
Enter token value: <your_api_token>
Enter number of threads: 10
Enter low range: 1
Enter high range: 100
```

---

## Sample Output

**CandidateInjection.py**

```json
{
  "name": "candidate one",
  "email": "email+1@gmail.com",
  "mobileNo": "9876543210",
  "skills": "Python, SQL",
  "year_of_experience": "5",
  "designation": "Backend Developer"
}
```

**JobsInjection.py**

```json
{
  "companyName": "company one",
  "jobTitle": "Data Scientist",
  "jobType": "fullTime",
  "jobLocation": "remote",
  "city": "Bangalore",
  "country": "India",
  "skillset": ["Python", "AWS"],
  "yearOfExperience": "3"
}
```

---

## Notes

* Ensure you have a valid API token before running.
* The scripts are designed for **testing purposes only**.
* Modify ranges and thread counts according to your system capacity and API rate limits.

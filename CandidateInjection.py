import requests
import random
from num2words import num2words
from concurrent.futures import ThreadPoolExecutor, as_completed
token_value=input("Enter token value:")
thread=int(input("Enter number of threads:"))
low=int(input("Enter low range:"))
high=int(input("Enter high range:"))
jobs_url = "https://test-api.skillioz.com/candidate/create"
headers = {
    "accept": "*/*",
    "token": f"{token_value}"
}
designations = ["Software Engineer","Backend Developer","Frontend Developer","Full Stack Developer","Data Scientist","Machine Learning Engineer","DevOps Engineer","Product Manager","Project Manager","Business Analyst","Quality Assurance Engineer","UI/UX Designer","Mobile App Developer","Cloud Engineer","Database Administrator","System Administrator","Technical Lead","Solution Architect","Network Engineer","Security Analyst"]
skills = ["Python","JavaScript","Java","C++","Node.js","React","Angular","Django","Flask","SQL","NoSQL","AWS","Azure","Docker","Kubernetes","Machine Learning","Data Analysis","HTML","CSS","Git"]
def job(i):# Form data
    data = {
        "name": f"candidate {num2words(i).replace("-", " ")}",
        "email": f"email+{i}@gmail.com",
        "mobileNo": f"{random.randint(1000000000, 9999999999)}",
        "skills": f"{random.choice(skills)}, {random.choice(skills)}",
        "year_of_experience": f"{random.randint(1, 20)}",
        "designation": f"{random.choice(designations)}",
    }
    print(data)

    # Send POST request
    response = requests.post(jobs_url, headers=headers, json=data)
    print("Status Code:", response.status_code)
    print("Response Body:")
    print("Response Body:", response.json())

executor = ThreadPoolExecutor(max_workers=10)

futures = [executor.submit(job, i) for i in range(low,high)] 


for future in as_completed(futures):
    future.result()

executor.shutdown(wait=True)
import requests
import random
from num2words import num2words
from concurrent.futures import ThreadPoolExecutor, as_completed
token_value=input("Enter token value:")
thread=int(input("Enter number of threads:"))
low=int(input("Enter low range:"))
high=int(input("Enter high range:"))
Url="https://test-api.skillioz.com/job/create"
headers = {
    "accept": "*/*",
    "token": f"{token_value}"
}
cities = ["Bhubaneswar","Delhi","Mumbai","Bangalore","Chennai","Hyderabad","Kolkata","Pune","Ahmedabad","Jaipur","Lucknow","Patna","Guwahati","Thiruvananthapuram","Chandigarh","Indore","Nagpur","Surat","Visakhapatnam","Coimbatore"]
categories = ["technology", "finance", "healthcare", "education", "marketing", "sales", "human resources", "operations", "legal", "real estate", "manufacturing", "entertainment", "consulting", "logistics", "government", "non-profit", "agriculture", "energy", "travel", "media"]
countries = ["India","United States","United Kingdom","Canada","Australia","Germany","France","Italy","Spain","China","Japan","South Korea","Brazil","Russia","Mexico","South Africa","Singapore","Netherlands","Switzerland","United Arab Emirates"]
job_titles = ["Software Engineer","Backend Developer","Frontend Developer","Full Stack Developer","Data Scientist","Machine Learning Engineer","DevOps Engineer","Product Manager","Project Manager","Business Analyst","Quality Assurance Engineer","UI/UX Designer","Mobile App Developer","Cloud Engineer","Database Administrator","System Administrator","Technical Lead","Solution Architect","Network Engineer","Security Analyst"]
skills = ["Python","JavaScript","Java","C++","Node.js","React","Angular","Django","Flask","SQL","NoSQL","AWS","Azure","Docker","Kubernetes","Machine Learning","Data Analysis","HTML","CSS","Git"]
job_loc=["onsite","remote","hybrid"]
job_type=["fullTime","partTime","contract"]

def job_th(i):
    data = {
        "category": "Technology",
        "city": f"{random.choice(cities)}",
        "companyName": f"company {num2words(i)}",
        "country": f"{random.choice(countries)}",
        "endDate": "2025-09-17T15:25:01.624Z",
        "jobDescription": "<p>this is my description</p>",
        "jobLocation": f"{random.choice(job_loc)}",
        "jobStatus": "",
        "jobTitle": f"{random.choice(job_titles)}",
        "jobType": f"{random.choice(job_type)}",
        "note": "a small note",
        "priority": "high",
        "skillset": [f"{random.choice(skills)}", f"{random.choice(skills)}"],
        "startDate": "2025-09-10T15:25:01.624Z",
        "yearOfExperience": f"{random.randint(1, 20)}"
    }
    response=requests.post(Url,headers=headers,data=data)
    print("Status Code:", response.status_code)
    print("Response Body:")
    print("Response Body:", response.json())

executor = ThreadPoolExecutor(max_workers=10)
futures = [executor.submit(job_th, i) for i in range(low,high)]  

for future in as_completed(futures):
    future.result()

executor.shutdown(wait=True)
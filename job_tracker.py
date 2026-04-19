import json
import os

FILE_NAME = "jobs.json"

def load_jobs():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_jobs(jobs):
    with open(FILE_NAME, "w") as file:
        json.dump(jobs, file, indent=4)

def add_job():
    company = input("Enter company name: ")
    role = input("Enter role: ")
    date = input("Enter applied date: ")

    job = {
        "company": company,
        "role": role,
        "date": date,
        "status": "Applied"
    }

    jobs = load_jobs()
    jobs.append(job)
    save_jobs(jobs)

    print("Job added successfully!\n")

def view_jobs():
    jobs = load_jobs()

    if not jobs:
        print("No jobs found.\n")
        return

    for i, job in enumerate(jobs):
        print(f"{i+1}. {job['company']} - {job['role']} - {job['status']} - {job['date']}")
    print()

def update_status():
    jobs = load_jobs()

    view_jobs()

    try:
        index = int(input("Enter job number to update: ")) - 1
        new_status = input("Enter new status (Applied/Interview/Rejected/Offer): ")

        jobs[index]["status"] = new_status
        save_jobs(jobs)

        print("Status updated!\n")
    except:
        print("Invalid input\n")

def search_job():
    keyword = input("Enter company or role to search: ").lower()
    jobs = load_jobs()

    found = False

    for job in jobs:
        if keyword in job["company"].lower() or keyword in job["role"].lower():
            print(f"{job['company']} - {job['role']} - {job['status']} - {job['date']}")
            found = True

    if not found:
        print("No matching jobs found.")

    print()

def main():
    while True:
        print("==== SMART JOB TRACKER ====")
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Update Status")
        print("4. Search Job")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            update_status()
        elif choice == "4":
            search_job()
        elif choice == "5":
            print("Good luck with your job search!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    # Sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    result = [-1] * n  # To store the job index in the result sequence
    slot = [False] * n  # To track if the time slot is occupied

    # Iterate through each job
    for i in range(n):
        # Check for available slots from min(jobs[i].deadline, n)-1 down to 0
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            if not slot[j]:
                result[j] = i  # Place job i in the jth slot
                slot[j] = True  # Mark slot as occupied
                break

    print("Following is the maximum profit sequence of jobs:")
    for i in range(n):
        if slot[i]:
            print(f"Job {jobs[result[i]].id}", end=" ")
    print()

if __name__ == "__main__":
    n = int(input("Enter the number of jobs: "))  # Number of jobs
    jobs = []

    # Taking input from the user
    for i in range(n):
        id = int(input(f"Enter Job ID for Job {i+1}: "))
        deadline = int(input(f"Enter deadline for Job {i+1}: "))
        profit = int(input(f"Enter profit for Job {i+1}: "))
        jobs.append(Job(id, deadline, profit))  # Add the job to the list

    job_sequencing(jobs, n)

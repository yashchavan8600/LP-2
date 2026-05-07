def job_scheduling(jobs, max_deadline):
    jobs.sort(key=lambda x: x[2], reverse=True)

    schedule = [None] * (max_deadline + 1)
    total_profit = 0
    jobs_done = []

    for job_id, deadline, profit in jobs:
        for slot in range(min(max_deadline, deadline), 0, -1):
            if schedule[slot] is None:
                schedule[slot] = job_id
                total_profit += profit
                jobs_done.append(job_id)
                break

    return jobs_done, total_profit, schedule


# --- User Input ---
job_list = []

n = int(input("Enter number of jobs: "))

for _ in range(n):
    job_id = input("Enter Job ID: ")
    deadline = int(input(f"Enter deadline for {job_id}: "))
    profit = int(input(f"Enter profit for {job_id}: "))
    job_list.append((job_id, deadline, profit))

max_time = int(input("Enter maximum deadline (time slots): "))

# --- Execution ---
scheduled_jobs, profit, schedule = job_scheduling(job_list, max_time)

print(f"Scheduled Jobs: {scheduled_jobs}")
print(f"Total Profit: {profit}")
print(f"Time Slot Allocation: {['Slot ' + str(i) + ': ' + str(job) for i, job in enumerate(schedule) if i > 0]}")
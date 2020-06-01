# python3
#todo git

##############################
# @author Daniel Avdar
# @input: first line - number or processes (workers) and number of jobs.
#         second line - each jobs' runtime.
#         assumes correct input.
# @output:  first col - worker id, second col - time of new job start
# @description: the script orders a given program's jobs into a queue
#               that enables a parallel run (scheduler)
#
##############################

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["finishTime", "worker", "started_at"])


def assign_jobs(n_workers, jobs):
    assigned_jobs = []
    job_zero = 0
    ans = []
    i = 0
    while i < n_workers:
        if i + job_zero >= len(jobs):
            return ans
        w = AssignedJob(finishTime=jobs[i + job_zero], worker=i, started_at=0)
        if w.finishTime == 0:
            ans.append(w)
            job_zero += 1
            continue

        heapq.heappush(assigned_jobs, w)
        ans.append(w)
        i += 1

    for i in jobs[n_workers + job_zero:]:
        worker = heapq.heappop(assigned_jobs)
        previous_finish_time = worker.finishTime
        w = AssignedJob(finishTime=previous_finish_time + i, worker=worker.worker, started_at=previous_finish_time)
        heapq.heappush(assigned_jobs, w)
        ans.append(w)

    return ans


def ansFormat(ans):
    res = ""
    for i in ans:
        res += str(i.worker) + " " + str(i.started_at) + "\n"
    return res


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    assigned_jobs = assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

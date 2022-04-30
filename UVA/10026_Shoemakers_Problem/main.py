import sys


def read_line():
    return sys.stdin.readline().strip()


def find_optimal_jobs_order(job_days, job_fines):
    def _cmp(job_pos):
        cost_ratio = job_fines[job_pos] / job_days[job_pos]
        return -round(cost_ratio, 12), job_pos

    jobs_order = list(range(len(job_days)))

    return sorted(jobs_order, key=_cmp)


def main():
    n_cases = int(read_line())
    case_sep = ""

    for _ in range(n_cases):
        read_line()

        job_days, job_fines = [], []

        n_jobs = int(read_line())
        for _ in range(n_jobs):
            curr_job_days, curr_job_fine = map(int, read_line().split())
            job_days.append(curr_job_days)
            job_fines.append(curr_job_fine)

        jobs_order = find_optimal_jobs_order(job_days, job_fines)
        print(
            f"{case_sep}{' '.join(str(job_pos + 1) for job_pos in jobs_order)}"
        )
        case_sep = "\n"

    return 0


if __name__ == '__main__':
    sys.exit(main())

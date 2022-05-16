import sys


def write_pre(domain_file, d, s_p, t_p):
    domain_file.write("pre: ")
    pre = []
    for smaller_disc in range(d[0]):
        pre.append(f"!{d[1]}-on-{s_p}")  # validate no smaller disc before d
        pre.append(f"!{d[1]}-on-{t_p}")  # validate no smaller disc on t_p which is blocking
    domain_file.write(" ".join(pre))
    domain_file.write("\n")


def write_add(domain_file, d, s_p, t_p):
    domain_file.write("add: ")
    add = [f"!{d[1]}-on-{s_p}", f"{d[1]}-on-{t_p}"]
    domain_file.write(" ".join(add))
    domain_file.write("\n")


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    # Propositions:
    domain_file.write("Propositions:\n")
    Propositions = []
    for d in disks:
        for p in pegs:
            Propositions.append(f"{d}-on-{p}")
            Propositions.append(f"!{d}-on-{p}")
    domain_file.write(" ".join(Propositions))
    domain_file.write("\n")

    # Actions:
    domain_file.write("Actions:\n")
    for d in enumerate(disks):
        for s_p in pegs:
            for t_p in pegs:
                if s_p == t_p:
                    continue
                domain_file.write(f"Name: M-{d[1]}-from-{s_p}-to-{t_p}\n")
                write_pre(domain_file, d, s_p, t_p)
                write_add(domain_file, d, s_p, t_p)
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    init_state = []
    goal_state = []
    for d in disks:
        init_state.append(f"{d}-on-{pegs[0]}")
        goal_state.append(f"{d}-on-{pegs[-1]}")

        for p in pegs[1:]:
            init_state.append(f"!{d}-on-{p}")
        for p in pegs[:-1]:
            goal_state.append(f"!{d}-on-{p}")




    problem_file.write("Initial state:")
    problem_file.write(" ".join(init_state))
    problem_file.write("\n")

    problem_file.write("Goal state:")
    problem_file.write(" ".join(goal_state))
    problem_file.write("\n")
    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)

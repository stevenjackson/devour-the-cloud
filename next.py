#!/usr/bin/env python3
from subprocess import check_output, call
import time

BRANCH_ORDER = [
      "master",
      "signup_script",
      "buy_script",
      "user_funnel",
      "find_baseline"
]

CURRENT_BRANCH_CMD = "git rev-parse --abbrev-ref HEAD".split()
QUERY_CHANGES_CMD = "git diff-index --quiet HEAD --".split()
COMMIT_WIP_CMD = "git commit -am 'wip'".split()
CHECKOUT_CMD = "git checkout".split()
RESET_CMD = "git reset --hard".split()
FETCH_CMD = "git fetch origin".split()

def next_branch(current_branch):
    next_index = 0
    for index, branch in enumerate(BRANCH_ORDER):
        if current_branch.startswith(branch):
            next_index = index + 1

    if next_index >= len(BRANCH_ORDER):
        next_index = 0

    return BRANCH_ORDER[next_index]

def build_command(base, *args):
    cmd = list(base)
    cmd.extend(args)
    return cmd

def current_branch():
    return check_output(CURRENT_BRANCH_CMD).decode("utf-8").strip()

def change_branch(current_branch, next_branch):
    changes = call(QUERY_CHANGES_CMD)
    if changes > 0:
        wip_branch = "%s_%d" % (current_branch, time.time())
        print("Storing work-in-progress at " + wip_branch)
        call(build_command(CHECKOUT_CMD, "-b", wip_branch))
        call(COMMIT_WIP_CMD)
    call(FETCH_CMD)
    call(build_command(CHECKOUT_CMD, next_branch))
    call(build_command(RESET_CMD, "origin/" + next_branch))

if __name__ == "__main__":
    current_branch = current_branch()
    next_branch = next_branch(current_branch)
    change_branch(current_branch, next_branch)
    print("Ready for " + next_branch + " exercise")

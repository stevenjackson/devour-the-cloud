#!/usr/bin/env python3
from next import current_branch, change_branch

if __name__ == "__main__":
    current_branch = current_branch()
    next_branch = current_branch + "_end"
    change_branch(current_branch, next_branch)
    print("Skip to the end of the " + current_branch + " exercise")

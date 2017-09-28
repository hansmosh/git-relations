"""gitrelations

Iterate over the git history and count how often files are in commits with
eachother.
"""
import subprocess
from collections import defaultdict


def main():
    """Main"""
    relations = _relations()
    relations = _remove_low_counts(relations, 3)
    print(relations)


def _relations():
    relations = defaultdict(lambda: defaultdict(int))
    for i in range(100):
        git_command = ("git diff-tree --no-commit-id --name-only -r "
                       "HEAD{}..HEAD{}".format("^"*(i+1), "^"*i))
        process = subprocess.Popen(git_command.split(), stdout=subprocess.PIPE)
        output = [filename for filename in
                  process.communicate()[0].decode().split('\n') if filename]
        if not output:
            # fix: break on last commit, not just any commit with nothing
            break
        for fromfile in output:
            for tofile in output:
                if fromfile != tofile:
                    relations[fromfile][tofile] += 1
    return dict({k: dict(v) for k, v in relations.items()})


def _remove_low_counts(relations, threshold=1):
    temp = {
        fromfile: {
            tofile: count
            for tofile, count in counts.items() if count > threshold
        }
        for fromfile, counts in relations.items()
    }
    return {tofile: counts for tofile, counts in temp.items() if counts}


if __name__ == "__main__":
    main()

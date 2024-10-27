import re
import sys

COMMIT_MSG_PATTERN = (
    r"^(chore|fix|feat|docs|style|refactor|perf|test|build|ci|revert|wip):"
)
ACCEPTABLE_TYPES = re.findall(r"\w+", COMMIT_MSG_PATTERN)

TYPE_DESCRIPTIONS = {
    "chore": "Routine task or maintenance",
    "fix": "Bug fix",
    "feat": "New feature",
    "docs": "Documentation changes",
    "style": "Code style changes (formatting, etc.)",
    "refactor": "Code refactoring",
    "perf": "Performance improvements",
    "test": "Adding or updating tests",
    "build": "Changes to the build system",
    "ci": "Changes to CI configuration",
    "revert": "Reverting a previous commit",
    "wip": "Work in progress",
}


def validate_commit_message(commit_msg_file):
    with open(commit_msg_file, "r") as file:
        commit_msg = file.read().strip()

    if not re.match(COMMIT_MSG_PATTERN, commit_msg):
        descriptions = [f"{type_}: {desc}" for type_, desc in TYPE_DESCRIPTIONS.items()]
        print(
            f"Invalid commit message. Must start with one of the following types:\n"
            + "\n".join(descriptions)
        )
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_commit_msg.py <commit_msg_file>")
        sys.exit(1)

    validate_commit_message(sys.argv[1])

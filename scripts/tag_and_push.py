import subprocess
import sys
from datetime import datetime


def run_command(command, check=True):
    """Runs a command and returns its output."""
    try:
        result = subprocess.run(
            command,
            check=check,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        sys.exit(1)


def main():
    """Cleans up old test tags and pushes a new timestamp-based tag."""
    print("Fetching latest tags from origin...")
    run_command(["git", "fetch", "--tags"])

    # Find all local and remote tags matching the pattern
    all_tags_raw = run_command(["git", "tag", "-l", "test-*"])
    all_tags = all_tags_raw.splitlines()

    if len(all_tags) >= 2:
        print(f"Found {len(all_tags)} test tags. Cleaning up old tags...")
        all_tags.sort()
        tags_to_delete = all_tags[:-1]  # Giữ lại tag mới nhất
        print("Keeping latest tag:", all_tags[-1])
        print("Deleting old tags:", ", ".join(tags_to_delete))

        # Xóa các tag cũ ở local
        run_command(["git", "tag", "-d"] + tags_to_delete)
        # Xóa các tag cũ trên remote
        run_command(["git", "push", "origin", "--delete"] + tags_to_delete)

    # Tạo tag mới dựa trên timestamp
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    new_tag = f"test-{timestamp}"

    print("Creating and pushing new tag:", new_tag)
    run_command(["git", "tag", new_tag])
    # Sử dụng --force để ghi đè nếu có tag trùng tên (khó xảy ra nhưng an toàn)
    run_command(["git", "push", "--force", "origin", new_tag])

    print("Successfully pushed tag", new_tag, "to origin.")


if __name__ == "__main__":
    main()

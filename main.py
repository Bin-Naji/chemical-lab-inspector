import os
from collections import Counter
from pathlib import Path


def analyze_lab(lab_directory):

    lab_directory = Path(lab_directory)

    file_count = 0
    directory_count = 0
    total_size = 0

    extensions = Counter()

    for path in lab_directory.rglob("*"):
        if path.is_dir():
            directory_count += 1
            continue

        if path.is_file():
            file_count += 1

            total_size += path.stat().st_size

            extension = path.suffix or "no extension"

            extensions[extension] += 1

    return {
        "files": file_count,
        "directories": directory_count,
        "total_size": total_size,
        "extensions": extensions,
    }


def main():
    print("=== Chemical Lab Inspector ===")

    print("\nSystem information")
    print("-------------------")

    print(f"Operating system: {os.name}")
    print(f"CPU count: {os.cpu_count()}")
    print(f"Process ID: {os.getpid()}")

    print("\nEnvironment")
    print("------------")

    print(f"User: {os.getenv('USER', 'unknown')}")

    lab = Path("chemical_project")

    print("\nLab directory")
    print("--------------")

    print(f"Path: {lab}")
    print(f"Absolute: {lab.resolve()}")

    if not lab.exists():
        print("Lab directory does not exist.")
        return

    report = analyze_lab(lab)

    print("\nAnalysis")
    print("--------")

    print(f"Files: {report['files']}")
    print(f"Directories: {report['directories']}")
    print(f"Total size: {report['total_size']} bytes")

    print("\nExtensions")

    for extension, count in report["extensions"].items():
        print(f"{extension}: {count}")


if __name__ == "__main__":
    main()

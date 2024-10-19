"""
CP1404 Practical
Wimbledon
Estimate: 1 hour
Actual:    minutes
"""

FILENAME = "wimbledon.csv"

def main():
    data = get_data(FILENAME)
    print(f"{data}")


def get_data(FILENAME):
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data




main()
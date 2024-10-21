"""
CP1404 Practical
Wimbledon
Estimate: 1 hour
Actual:  3 hours, 50 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print Wimbledon champions and countries"""
    records = get_data(FILENAME)
    champion_count, countries = process_records(records)
    display_results(champion_count, countries)


def process_records(records):
    champion_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_count[record[INDEX_CHAMPION]] = 1
    return champion_count, countries


def display_results(champion_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_count.items():
        print(name, count)
    print(f"\n These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_data(filename):
    """Extract data from CSV file and return it as a list"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()

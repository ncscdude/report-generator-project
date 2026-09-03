"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv


def read_csv_file(filepath):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    # TODO: Your code here
    # Hint: Use csv.DictReader to read CSV files into dictionaries
    # Hint: Remember to use 'with open()' for proper file handling
    with open(filepath, 'r',) as file:
        reader = csv.DictReader(file)
        return list(reader)


def count_records(data_list):
    """Counts the number of records in a dataset."""
    # TODO: Your code here
    # Hint: Use the len() function
    return len(data_list)


def get_unique_values(data_list, field_name):
    """Gets all unique values for a specific field in the dataset."""
    # TODO: Your code here
    # Hint: Use a set to collect unique values
    # Hint: Convert the set to a list and sort it before returning
    unique_values = set()
    for record in data_list:
        unique_values.add(record[field_name])
    return sorted(list(unique_values))



def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""
    # TODO: Your code here
    # Hint: Use a list comprehension to filter or a loop!
    # see here for more info: https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions
    filtered_records = []
    for record in data_list:
        if record[field_name] == field_value:
            filtered_records.append(record)
    return [record for record in data_list if record[field_name] == field_value]



def calculate_total(data_list, field_name):
    """Calculates the sum of a numeric field across all records."""
    # TODO: Your code here
    # Hint: Initialize a total variable to 0
    # Hint: Loop through each record and add float(record[field_name]) to total
    # Hint: Remember to convert string values to float!
    total = 0.0
    for record in data_list:
        total += float(record[field_name])
    return total



def calculate_average(data_list, field_name):
    """Calculates the average value of a numeric field."""
    # TODO: Your code here
    # Hint: Use calculate_total() and count_records() functions
    # Hint: Average = total / count
    count = count_records(data_list)
    if count == 0:
        return 0.0
    total = calculate_total(data_list, field_name)
    return total / count



def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    # TODO: Your code here
    # Hint: Loop through data_list
    # Hint: Return the record when record[id_field] == id_value
    for record in data_list:
        if record[id_field] == id_value:
            return record
    return None  # Return None if not found



def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    # TODO: Your code here
    # Hint: Create a dictionary mapping secondary_list IDs to records
    # Hint: For each record in primary_list, look up the matching secondary record
    # Hint: Use dict.update() to merge dictionaries
    # Step 1: Build lookup dictionary from secondary list
    secondary_lookup = {}
    for item in secondary_list:
        secondary_lookup[item[foreign_key]] = item

    # Step 2: Merge secondary data into each primary record
    joined_list = []
    for primary_item in primary_list:
        combined = primary_item.copy()
        match_id = primary_item.get(primary_key)

        if match_id in secondary_lookup:
            combined.update(secondary_lookup[match_id])

        joined_list.append(combined)

    return joined_list


def write_report_to_file(filepath, content):
    """Writes a text report to a file."""
    # TODO: Your code here
    # Hint: Use 'with open(filepath, 'w')' to open file for writing
    pass


def format_header(title):
    """Creates a formatted header for reports."""
    # TODO: Your code here
    # Hint: Use "=" * 60 to create a line of equals signs
    # Hint: Use .center(60) to center the title
    pass


# Testing functions
if __name__ == '__main__':
    print("Testing report functions...")

    # Test read_csv_file
    pilots = read_csv_file('data/pilots.csv')
    print(f"Loaded {len(pilots)} pilots")
    print(f"First pilot: {pilots[0]}")
    count = count_records(pilots)
    print(f"Count function returned: {count}")
    squadrons = get_unique_values(pilots, 'squadron')
    print(f"Unique squadrons: {squadrons}")
    vfa_41_pilots = filter_by_field(pilots, 'squadron', 'VFA-41')
    print(f"VFA-41 pilots found: {len(vfa_41_pilots)}")
    for p in vfa_41_pilots:
        print(f"  - {p['rank']} {p['last_name']} ({p['callsign']})")
    total_hours = calculate_total(vfa_41_pilots, 'total_flight_hours')
    print(f"Total flight hours for VFA-41: {total_hours}")
    avg_hours = calculate_average(vfa_41_pilots, 'total_flight_hours')
    print(f"Average flight hours for VFA-41: {avg_hours:.2f}")
    avg_hours = calculate_average(vfa_41_pilots, 'total_flight_hours')
    print(f"Average flight hours for VFA-41: {avg_hours:.2f}")
    pilot = find_record_by_id(pilots, 'pilot_id', 'P001')
    print(f"Found pilot P001: {pilot['rank']} {pilot['last_name']} ({pilot['callsign']})")
    # Load flight logs to test join
    flights = read_csv_file('data/flight_logs.csv')
    print(f"Loaded {len(flights)} flight records")

    # Join flights with pilots using 'pilot_id'
    enriched_flights = join_data(flights, pilots, 'pilot_id', 'pilot_id')
    print(f"Sample enriched flight record: {enriched_flights[0]}")
"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.

    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """
    # TODO: PART 1 - Load the data files
    pilots = rf.read_csv_file('data/pilots.csv')
    aircraft = rf.read_csv_file('data/aircraft.csv')
    flights = rf.read_csv_file('data/flight_logs.csv')

    # TODO: PART 2 - Filter data for the specified squadron
    squadron_pilots = rf.filter_by_field(pilots, 'squadron', squadron_code)
    squadron_aircraft = rf.filter_by_field(aircraft, 'squadron', squadron_code)

    # TODO: PART 3 - Get flights for squadron pilots
    squadron_pilot_ids = [p['pilot_id'] for p in squadron_pilots]
    squadron_flights = [f for f in flights if f['pilot_id'] in squadron_pilot_ids]


    # TODO: PART 4 - Calculate statistics
    # PART 4: Calculate statistics
    total_hours = rf.calculate_total(squadron_flights, 'duration_hours')
    total_missions = rf.count_records(squadron_flights)
    avg_duration = rf.calculate_average(squadron_flights, 'duration_hours')

    # Count missions by type
    mission_types = rf.get_unique_values(squadron_flights, 'mission_type')
    mission_counts = {}
    for m_type in mission_types:
        matches = rf.filter_by_field(squadron_flights, 'mission_type', m_type)
        mission_counts[m_type] = rf.count_records(matches)

    # TODO: PART 5 - Build the report content
    report = []
    report.append(rf.format_header(f"SQUADRON OPERATIONS REPORT: {squadron_code}"))
    report.append("Generated: Operational Flight Data System\n")

    # Section 1: Operational Summary
    report.append("--- OPERATIONAL SUMMARY ---")
    report.append(f"Total Missions Flown : {total_missions}")
    report.append(f"Total Flight Hours   : {total_hours:.1f} hrs")
    report.append(f"Average Mission Time : {avg_duration:.2f} hrs\n")

    # Section 2: Mission Breakdown
    report.append("--- MISSION BREAKDOWN ---")
    for m_type, count in mission_counts.items():
        report.append(f"  {m_type:<18}: {count:>4} missions")
    report.append("")

    # Section 3: Personnel Roster
    report.append(f"--- SQUADRON ROSTER ({len(squadron_pilots)} Pilots) ---")
    for p in squadron_pilots:
        full_name = f"{p['rank']} {p['first_name']} {p['last_name']}"
        report.append(f"  {p['pilot_id']} | {full_name:<24} | Callsign: {p['callsign']:<12} | Hours: {p['total_flight_hours']}")
    report.append("")

    # Section 4: Aircraft Inventory
    report.append(f"--- AIRCRAFT INVENTORY ({len(squadron_aircraft)} Aircraft) ---")
    for a in squadron_aircraft:
        report.append(f"  {a['aircraft_id']} | Tail: {a['tail_number']:<10} | Status: {a['status']:<12} | Hours: {a['total_flight_hours']}")
    report.append("\n" + "=" * 60 + "\n")

    full_report_text = "\n".join(report)

    # TODO: PART 6 - Write the report to file
    rf.write_report_to_file(output_file, full_report_text)
    print(f"Report for {squadron_code} successfully generated at {output_file}")


# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")
    pilots = rf.read_csv_file('data/pilots.csv')
    squadron = rf.get_unique_values(pilots, 'squadron')

    for sq in squadron:
        output_path = f"reports/{sq}-report.txt"
        generate_squadron_report(sq, output_path)

        print("\nAll reports succssfully generated.")


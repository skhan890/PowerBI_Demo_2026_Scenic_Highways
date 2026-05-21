import csv
from dbfread import DBF

def dbf_to_csv(dbf_path)
    # Create the output CSV filename by replacing .dbf with .csv
    csv_path = dbf_path.rsplit('.', 1)[0] + '.csv'
    # Open and read the DBF file
    table = DBF(dbf_path)
    
    # Open the CSV file for writing
    with open(csv_path, 'w', newline='', encoding='utf-8') as f
        writer = csv.writer(f)
        # Write the header row (field names from DBF)
        writer.writerow(table.field_names)
        # Write each record as a row
        for record in table
            writer.writerow(list(record.values()))
    
    print(fSuccess! CSV file saved to {csv_path})
    return csv_path

# --- Main execution block ---
if __name__ == __main__
    # Get the name of your DBF file from the user
    dbf_filename = input(Enter the name of your .dbf file (e.g., mydata.dbf) )
    dbf_to_csv(dbf_filename)
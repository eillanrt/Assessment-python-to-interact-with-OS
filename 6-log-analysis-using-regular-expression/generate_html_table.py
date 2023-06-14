import csv


def generate_html_table(csv_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Read the CSV data
        csv_data = csv.reader(file)

        # Create the HTML table
        html_table = '<table>\n'

        # Iterate over each row in the CSV data
        for row in csv_data:
            html_table += '\t<tr>\n'

            # Iterate over each cell in the row
            for cell in row:
                html_table += f'\t\t<td>{cell}</td>\n'

            html_table += '\t</tr>\n'

        html_table += '</table>'

    return html_table

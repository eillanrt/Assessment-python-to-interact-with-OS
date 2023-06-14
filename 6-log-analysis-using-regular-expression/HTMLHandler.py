import csv


def append_to_html_file(html_file, element_id, content):
    # Read the existing HTML file
    with open(html_file, 'r') as file:
        html_content = file.read()

    # Find the position of the specified element in the HTML content
    element_start = html_content.find(f'id="{element_id}"')
    element_end = html_content.find('>', element_start) + 1

    # Append the content after the specified element
    updated_html_content = (
        html_content[:element_end] +
        '\n' + content.strip() +
        html_content[element_end:]
    )

    # Write the updated HTML content back to the file
    with open(html_file, 'w') as file:
        file.write(updated_html_content)


def generate_html_table(csv_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Read the CSV data
        csv_data = csv.reader(file)

        # Create the HTML table
        html_table = '<table>\n'
        is_header = True
        header_class_name = ' class="header"'

        # Iterate over each row in the CSV data
        for row in csv_data:
            html_table += '\t<tr>\n'

            # Iterate over each cell in the row
            for cell in row:
                html_table += f'\t\t<td{header_class_name if is_header else ""}>{cell}</td>\n'

            html_table += '\t</tr>\n'
            is_header = False

        html_table += '</table>'

    return html_table

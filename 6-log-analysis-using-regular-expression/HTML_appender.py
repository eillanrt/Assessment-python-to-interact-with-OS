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

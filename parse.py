from cleaner import delete_format_waste_content
from webwriter import write_html
if __name__ == "__main__":
    messages = delete_format_waste_content()
    write_html(messages)
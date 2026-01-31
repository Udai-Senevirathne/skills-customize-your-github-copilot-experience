"""
File Input and Output Assignment - Starter Code

This module provides function stubs for working with file I/O operations.
Complete each function according to the assignment requirements.
"""

def read_and_display_file(filename):
    """
    Read a file and display its contents with line numbers.
    
    Args:
        filename (str): The name of the file to read
        
    Returns:
        int: The total number of lines read
    """
    # TODO: Open the file and read line by line
    # TODO: Print each line with its line number
    # TODO: Handle FileNotFoundError if file doesn't exist
    # TODO: Return the total line count
    pass


def write_scores_to_file(scores_dict, output_filename):
    """
    Write student scores to a file with formatting.
    
    Args:
        scores_dict (dict): Dictionary with student names as keys and scores as values
        output_filename (str): Name of the file to write to
        
    Returns:
        int: Number of records written
    """
    # TODO: Open output file for writing
    # TODO: Write a header with the current date
    # TODO: Format and write each student's name and score
    # TODO: Close the file
    # TODO: Return the number of records written
    pass


def filter_and_append_file(input_filename, output_filename, keyword):
    """
    Filter lines from input file and append matching ones to output file.
    
    Args:
        input_filename (str): Source file to read from
        output_filename (str): File to append filtered lines to
        keyword (str): Keyword to filter by
        
    Returns:
        int: Number of lines appended
    """
    # TODO: Open and read the input file
    # TODO: Filter lines that contain the keyword
    # TODO: Open output file in append mode
    # TODO: Write filtered lines to output file
    # TODO: Return count of lines appended
    pass


# Example usage (uncomment after implementing functions):
# if __name__ == "__main__":
#     # Test read_and_display_file
#     total_lines = read_and_display_file("input.txt")
#     print(f"Total lines: {total_lines}")
#
#     # Test write_scores_to_file
#     scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
#     records = write_scores_to_file(scores, "results.txt")
#     print(f"Records written: {records}")
#
#     # Test filter_and_append_file
#     appended = filter_and_append_file("data.txt", "filtered.txt", "python")
#     print(f"Lines appended: {appended}")

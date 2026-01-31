# 📘 Assignment: File Input and Output

## 🎯 Objective

Learn how to read from and write to files in Python. You'll practice opening files, processing their contents, and saving data to new files—essential skills for working with real-world data.

## 📝 Tasks

### 🛠️ Read and Process a Text File

#### Description
Write a program that reads a text file line by line, processes the content, and displays it to the user.

#### Requirements
Completed program should:

- Open and read a file named `input.txt`
- Print each line with its line number
- Count and display the total number of lines
- Handle the case where the file doesn't exist with an appropriate error message


### 🛠️ Write Data to a File

#### Description
Create a function that takes a list of student names and test scores, formats them nicely, and writes the results to a new file.

#### Requirements
Completed program should:

- Accept a dictionary where keys are student names and values are test scores
- Format each entry as: `[Name]: [Score]/100`
- Write all formatted entries to a file named `results.txt`
- Include a header line with the current date
- Print a confirmation message showing how many records were written


### 🛠️ Append to an Existing File

#### Description
Write a function that reads data from one file and appends selected entries to another file based on a condition.

#### Requirements
Completed program should:

- Read lines from `data.txt`
- Filter lines that meet a condition (e.g., contain a specific keyword or exceed a certain length)
- Append matching lines to a file named `filtered.txt`
- Display how many lines were appended
- Create the output file if it doesn't exist

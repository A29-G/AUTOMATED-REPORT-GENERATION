# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: AISHWARYA VEERANAGOUDA GIRIYAL

*INTERN ID*: CT04WU10

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

*DESCRIPTION*





###  **Project Description: Automated PDF Report Generator using Python**

The **Automated PDF Report Generator** is a Python-based project designed to read structured data from a CSV file, perform basic data analysis, and generate a professionally formatted PDF report. This project is ideal for beginners who want to learn how to automate simple tasks using Python and gain hands-on experience with data processing, file handling, and report generation.

The project simplifies the manual process of analyzing tabular data and compiling results into a report. With a single execution, the program reads student score data from a CSV file, calculates key statistics, and outputs a well-structured PDF summary. This process can be adapted for various applications such as academic result summaries, performance evaluations, survey reports, and more.

The project is organized in a simple and beginner-friendly structure:
- The **`data/`** folder contains the input file `sample_data.csv`, which holds records of student names and their scores.
- The **`report_generator.py`** script performs data reading, analysis, and PDF creation.
- The **`report/`** folder stores the output report file named `generated_report.pdf`.

The working of the script can be broken down into five key steps:

1. **Reading CSV Data**: Using Python’s built-in `csv` module, the script reads data from the input file. Each row is stored as a dictionary, with the score field converted to an integer to allow accurate analysis.

2. **Data Analysis**: The script computes the total number of entries, the average score of all students, the student with the highest score, and the student with the lowest score. This analysis is performed using basic Python operations such as list comprehensions, `sum()`, `max()`, and `min()` functions.

3. **PDF Report Generation**: The `fpdf` library is used to generate a PDF file. The report includes a header title, followed by the total number of students, the average score, and details of the highest and lowest scoring students. The formatting is clean and readable, making the output suitable for academic or professional use.

4. **Folder and File Handling**: Before saving the output report, the script checks if the target folder exists using `os.makedirs()` and creates it if necessary. This ensures the program runs without errors related to missing directories.

5. **Script Execution**: The program runs as a standalone Python script and can be executed from the terminal using the command `python report_generator.py`. Once executed, it generates the report automatically and confirms successful completion via a printed message.

This project helps users understand several core programming concepts, including:
- Reading and processing external data files
- Performing statistical analysis
- Using third-party libraries for document creation
- Structuring code for clarity and reusability

The code is modular, well-commented, and easy to modify. It serves as a great starting point for anyone interested in automating reporting tasks using Python. Overall, the Automated PDF Report Generator provides a practical and educational example of how simple scripting can streamline everyday data handling and documentation processes.



*OUTPUT*

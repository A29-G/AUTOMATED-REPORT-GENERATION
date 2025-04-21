import csv
from fpdf import FPDF
import os

# Step 1: Read data from CSV file
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)  # Reads each row as a dictionary
        for row in reader:
            row['Score'] = int(row['Score'])  # Convert score to number
            data.append(row)
    return data

# Step 2: Analyze the data (total, average, highest, lowest)
def analyze_data(data):
    scores = [row['Score'] for row in data]
    total = len(scores)
    average = sum(scores) / total
    highest = max(data, key=lambda x: x['Score'])
    lowest = min(data, key=lambda x: x['Score'])

    return {
        'total': total,
        'average': average,
        'highest': highest,
        'lowest': lowest
    }

# Step 3: Create a simple PDF Report using FPDF
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Student Score Report', ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_report_content(self, summary):
        self.set_font('Arial', '', 12)
        self.ln(10)
        self.cell(0, 10, f"Total Students: {summary['total']}", ln=True)
        self.cell(0, 10, f"Average Score: {summary['average']:.2f}", ln=True)
        self.cell(0, 10, f"Highest Score: {summary['highest']['Name']} ({summary['highest']['Score']})", ln=True)
        self.cell(0, 10, f"Lowest Score: {summary['lowest']['Name']} ({summary['lowest']['Score']})", ln=True)

# Step 4: Main function to combine all steps
def generate_pdf_report(input_csv, output_pdf):
    data = read_csv(input_csv)
    summary = analyze_data(data)

    pdf = PDFReport()
    pdf.add_page()
    pdf.add_report_content(summary)
    pdf.output(output_pdf)
    print("PDF report created successfully!")

# Step 5: Run the script
if __name__ == "__main__":
    # File paths
    input_file = "data/sample_data.csv"
    output_file = "report/generated_report.pdf"

    # Create output folder if it doesn't exist
    os.makedirs("report", exist_ok=True)

    # Generate the report
    generate_pdf_report(input_file, output_file)

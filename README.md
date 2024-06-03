## Automated Skiptrace Process
This comprehensive suite of Python scripts is designed for managing skiptrace data, facilitating a streamlined workflow to process, integrate, and generate reports on litigators. It is structured to work in three main stages, each handled by an individual script:

skiptrace.py: Pre-processes skiptrace data by filtering and removing duplicates.

before_t1.py: Integrates processed skiptrace data with the main T1Skiptrace file.

after_t1.py: Identifies litigators and generates various reports.

## Detailed Workflow
## 1. skiptrace.py: Pre-processing Skiptrace Data
Objective: Cleans and prepares input files containing "SMS" or "Cold Calling" data, ensuring they are free from unwanted entries and duplicates.

Key Actions:

Creates the output directory if it doesn't exist.

Lists all relevant Excel files in the input directory.

Reads each file, filtering out rows without "Skiptrace" in the TAGS column and with all phone numbers empty.

Removes duplicates between "SMS" and "Cold Calling" files based on mailing address criteria.

Saves the filtered data to the output directory with the suffix - BST.

Outcome: Produces cleaned and filtered Excel files ready for integration. The rows are sorted in descending order based on Score.

## 2. before_t1.py: Integrating Skiptrace Data
Objective: Integrates the filtered skiptrace data with a main T1Skiptrace BST_out file and prepares it for further processing.

Key Actions:

Ensures the output directory exists.

Finds and reads the relevant files in the input directory.

Verifies the number of rows matches between the T1Skiptrace and Cold Calling/SMS files.

Inserts the Folio column and modifies the DEC and BNK columns.

Renames columns according to the provided mapping.

Saves the modified data and generates the "Litigator scrubbing" file.

Outcome: Produces an integrated and cleaned dataset, ready for litigator identification and report generation.

## 3. after_t1.py: Identifying Litigators and Creating Reports
Objective: Identifies litigators and creates various reports based on the integrated data.

Key Actions:

Ensures all necessary directories exist.

Reads the all_clean, Litigator scrubbing, and T1Skiptrace BST_out files.

Identifies numbers not in all_clean and their associated IDs.

Filters and saves data, including flagged litigators and "Non Hits".

Creates the Import Flagged Litigators file with specified columns and additional values.

Outcome: Generates final reports and datasets, including flagged litigators (must include the second TAG column as "Litigator") and "Non Hits", ready for further analysis or action manually.

## Setup and Requirements
Before running the scripts, ensure your Python environment is set up with Python 3.x and the necessary libraries (pandas and openpyxl). Organize your Excel files according to the input requirements of each script, and adjust the scripts' parameters to match your dataset and goals.

No file contained in any of the folders can be open at the time of running the code.

## Execution Guide
Run skiptrace.py: Start with the data pre-processing script to prepare your data files. Ensure all unwanted data is filtered out and the data is consistent.

Proceed with before_t1.py: After cleaning, integrate the filtered skiptrace data with the main T1Skiptrace dataset.

Finalize with after_t1.py: Identify litigators and generate the necessary reports and datasets.

## Important Notes
Each script is designed to operate sequentially but can be adjusted for standalone use if required.

Customize folder paths, criteria for filtering and sorting, and other parameters in the scripts to fit your specific needs.

This suite is an invaluable tool for professionals looking to optimize their skiptrace data management processes, from initial cleaning to the strategic generation of reports and datasets.

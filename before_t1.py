import os
import pandas as pd

def integrate_skiptrace_data(input_folder="t1 input", output_folder="t1 output"):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Find the T1Skiptrace and Cold Calling or SMS files in the input folder
    t1_files = [f for f in os.listdir(input_folder) if "T1Skiptrace BST_out" in f and f.endswith('.xlsx')]
    calling_sms_files = [f for f in os.listdir(input_folder) if ("Cold Calling" in f or "SMS" in f) and f.endswith('.xlsx')]
    
    if not t1_files:
        print("No T1Skiptrace BST_out file found.")
        return
    if not calling_sms_files:
        print("No Cold Calling or SMS file found.")

        return

    # Read the Excel files                           
    t1_file_path = os.path.join(input_folder, t1_files[0])
    calling_sms_file_path = os.path.join(input_folder, calling_sms_files[0])
    try:
        t1_data = pd.read_excel(t1_file_path)
        calling_sms_data = pd.read_excel(calling_sms_file_path)
    except Exception as e:
        print(f"Failed to read the files: {e}")
        return
    
    # Verify the number of rows matches
    if len(t1_data) != len(calling_sms_data):
        print("The number of rows in T1Skiptrace BST_out does not match the Cold Calling/SMS file.")
        return
    
    # Insert the Folio column at the beginning of the T1Skiptrace file
    t1_data.insert(0, 'Folio', calling_sms_data['Folio'])

    # Modify DEC and BNK columns
    t1_data['DEC: Deceased (Y/N)'] = t1_data['DEC: Deceased (Y/N)'].replace({'N': '', 'Y': '1'})
    t1_data['BNK: Bankrupt (Y/N)'] = t1_data['BNK: Bankrupt (Y/N)'].replace({'N': '', 'Y': '1'})

    # Rename columns
    columns_to_rename = {
        'INPUT: First Name': 'First Name',
        'INPUT: Last Name': 'Last Name',
        'INPUT: Address 1': 'Mailing Address',
        'INPUT: City': 'Mailing city',
        'INPUT: State': 'Mailing state',
        'INPUT: Zip Code': 'Mailing zip',
        'INPUT: Extra 1': 'Property Address',
        'INPUT: Extra 2': 'Property city',
        'INPUT: Extra 3': 'Property State',
        'INPUT: Extra 4': 'Property zip',
        'BNK: Bankrupt (Y/N)': 'Bankrupcy',
        'DEC: Deceased (Y/N)': 'Estate',
        'ADD: Address1': 'Golden Address',
        'ADD: Address1 City': 'Golden city',
        'ADD: Address1 State': 'Golden State',
        'ADD: Address1 Zip': 'Golden Zip'
    }
    
    t1_data.rename(columns=columns_to_rename, inplace=True)

    # Add ID column starting at 1 and incrementing by 1 for each row
    t1_data.insert(0, 'ID', range(1, len(t1_data) + 1))

    # Prepare the Litigator scrubbing file
    phone_columns = [
        'PH: Phone1', 'PH: Phone2', 'PH: Phone3', 'PH: Phone4', 'PH: Phone5',
        'REL1: Phone 1', 'REL1: Phone 2', 'REL1: Phone 3',
        'REL2: Phone 1', 'REL2: Phone 2', 'REL2: Phone 3',
        'REL3: Phone 1', 'REL3: Phone 2', 'REL3: Phone 3'
    ]
    
    litigator_data = t1_data[['ID'] + phone_columns]
    litigator_data = litigator_data.set_index('ID')
    litigator_data = litigator_data.stack().reset_index(name='Numbers').drop('level_1', axis=1)
    litigator_data = litigator_data[litigator_data['Numbers'].notnull()]

    # Save the modified T1Skiptrace file
    t1_output_path = os.path.join(output_folder, f"modified_{os.path.basename(t1_file_path)}")
    litigator_output_path = os.path.join(output_folder, "Litigator scrubbing.xlsx")
    try:
        t1_data.to_excel(t1_output_path, index=False)
        print(f"Modified file saved successfully at {t1_output_path}")
        # Save the Litigator scrubbing file
        litigator_data.to_excel(litigator_output_path, index=False)
        print(f"Litigator scrubbing file saved successfully at {litigator_output_path}")
    except Exception as e:
        print(f"Failed to save the modified files: {e}")

# Uncomment the following line to run the function
integrate_skiptrace_data()

import csv
 

# # 1.
# file = open('test.csv', 'w')
# # 2.
# writer = csv.writer(file)
# # 3.
# data = ["This", "is", "a", "Test"]
# writer.writerow(data)
# # 4.
# file.close()

import os
 
 
# input arguments your track dict
# input arguments the filename of the newly created csv
def _export_to_csv(input_dict: dict = None, export_filename: str = None):
    try:
        # example.csv is the name of our exported file
        # mode = a+ we open a file handled in append plus mode
        with open(export_filename, mode="a+", newline='') as out_csv:
 
            writer = csv.DictWriter(out_csv, fieldnames=input_dict.keys())
 
            # checking file size to determine if we need a header row
            if os.stat(export_filename).st_size == 0:
                writer.writeheader()
 
            # writing the data in your dict to the csv
            writer.writerow(input_dict)
        return "Success"
    # catch any exceptions and print them to the terminal
    except Exception as e:
        print(e)
        return "Failure"
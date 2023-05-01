# ivadomed_five_fold

 ## Steps to run five fold cross validation using [ivadomed](https://ivadomed.org)

 ### Step 1: Run the extract_train_val.py to extract a smaller dataset from the original BIDS dataset.
 - The random seed has to be changed 5 times to get 5 different sets the cross validation.
 - The extracted small BIDS datasets will provide us with the train and validation sets for each fold. The rest of the data will be used as the test set.

 Example command:
 ```
 python extract_train_val.py -i path/to/BIDS/dataset -o path/of/small/BIDS/dataset -n 10 -c T2w -d 0 -s 1234
 ```

 ### Step 2: Run the test_file_names.py to get the list of test files for each fold. The ouptut file is stored as a .txt file. The folder names inside the script have to be changed. 

 Example command:
 ```
 python test_file_names.py
 ```

 ### Step 3: Run the copy_test.py to copy the test files to a new folder. The text file names recieved from the second step have to be changed in the script.

 Example command:
 ```
 python copy_test.py
 ```

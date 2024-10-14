# Machine Learning Models for Disease Classification

Binary classification for diagnosing liver disease (as a results of hepatitic C infection)

## Reading order / executing the program

1. Please run read the document titled main.pdf - this is acompanied by the R markdown file main.Rmd
2. At the point of over-sampling, please run the Rmd file smote.Rmd. Note, it is useful to run this file chunk by chunk, since we require the running of another Python file in the middle. 
3. In the sixth code chunk, we write our data into a csv file -- please adjust the file path to your desired location. This will be located at .../train.csv.
4. Please run the file smote.py, editing the file path in the program to the location of train.csv (.../train.csv). This will create a 'zip' file of the over-sampled synthetic data called 'sm_train.zip'. 
5. Please open this file (sm_train.zip), and save the data in your desired location so that you can run the next chunk, and read the file in R -- to do this, again, please change the file path in the following chunk of code to .../sm_train.csv
6. Now, run the rest of the code
7. Continue from the point you left in main.Rmd. This is where we discuss the results.

### Dependencies

Dependensies should be dealt with in the programs themselves if any additional package is required. 

Note that, in the file 'smote.py', we need to revert to an older version (1.2.2) of scikit-learn for program to work. This should be dealt with in the program script.


## Authors

ex. Thomas Pagulatos


## License

See the LICENSE.md file for details

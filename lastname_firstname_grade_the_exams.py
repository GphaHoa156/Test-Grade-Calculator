# Import libraries
import re
import os

import pandas as pd
import numpy as np


# Main class
class Autogradesystem():
    
    
    """Initialize function
    """
    def __init__(self, answer_key, ID_pattern):
        self.ID_pattern = ID_pattern
        self.answer_key = answer_key


    """ Read file and check if there is any error
    """
    def read_file(self):
        self.file_name = input("Enter a class to grade (i.e. class1 for class1.txt): ")
        try:
            with open(f"{self.file_name}.txt", 'r') as f:
                self.file_contents = f.readlines() 
                print(f"Successfully opened {self.file_name}.txt")
        except FileNotFoundError:
            print("File cannot be found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None


    """ Check invalid lines in the file and print them out
    """
    def clean_file(self):
        print("**** ANALYZING ****\n")
        
        valid_lines = []    # Using list to store valid lines
        invalid_lines = []  # Invalid lines will be a list of tuples where each tuple is (error name, line content)
        
        for line in self.file_contents:
            parts = line.strip().split(",") 
            ID = parts[0]
            answers = parts[1:]
            if not re.match(self.ID_pattern, ID):  
                invalid_lines.append(
                    (line.strip(), "N# is invalid")
                )
            elif len(answers) != len(self.answer_key):
                invalid_lines.append(
                    (line.strip(), "does not contain exactly 26 values:")
                )
            else:
                valid_lines.append(parts)
        
        # Create table from valid lines
        self.valid_table = pd.DataFrame(
            valid_lines,
            columns=["ID"] + [f"Q{i}" for i in range(1, len(self.answer_key) + 1)]
        )
        for line, error in invalid_lines:
            print(f"""{error}: 
{line}
""")
        
        print(f"""**** REPORT ****
Total valid lines of data: {len(self.valid_table)}
Total invalid lines of data: {len(invalid_lines)}
""")


    """ Calculate grade for each student 
    """
    def mark_result(self):
        # Use boolean numpy array to compare student answer to correct answer
        correct_arr = np.array(self.answer_key)
        student_answers = self.valid_table.iloc[:, 1:].to_numpy()
        correct_mask = student_answers == correct_arr  
        skip_mask = student_answers == ""             
        incorrect_mask = ~correct_mask & ~skip_mask  
        
        # Calculate grade base on number of correct and wrong answer 
        grades = (4 * correct_mask.sum(axis=1)  
                  - incorrect_mask.sum(axis=1))
        self.valid_table["Grade"] = grades
        
        # Create a counter list to count number of skip(false) answer for each question
        self.skip_counter = skip_mask.sum(axis=0).tolist()       
        self.false_counter = incorrect_mask.sum(axis=0).tolist()

    """ Calculate descriptive statistic of grade data
    """
    def describe_grade(self):
        marks_series = self.valid_table["Grade"]

        #Calculate min, max, mean, median,..
        high_grade_number = (marks_series > 80).sum()
        mean_grade = marks_series.mean()
        highest_grade = marks_series.max()
        lowest_grade = marks_series.min()
        grade_range = highest_grade - lowest_grade
        median_grade = marks_series.median()

        # Find the index of the question that mostly skipped(failed)
        skip_question = [
            i+1 for i, count in enumerate(self.skip_counter) if count == max(self.skip_counter)
        ]
        fail_question = [
            i+1 for i, count in enumerate(self.false_counter) if count == max(self.false_counter)
        ]

        # Calculate skip(fail) percentage
        skip_percent = max(self.skip_counter) / len(marks_series) if len(marks_series) > 0 else 0
        fail_percent = max(self.false_counter) / len(marks_series) if len(marks_series) > 0 else 0

        # Create string: question index - skip(fail) time - percentage
        skip_list = ", ".join(
            f"{q} - {max(self.skip_counter)} - {skip_percent:.3f}" for q in skip_question
        )
        fail_list = ", ".join(
            f"{q} - {max(self.false_counter)} - {fail_percent:.3f}" for q in fail_question
        )
        
        # print result
        print(
            f"""Total student of high scores: {high_grade_number}
Mean (average) score: {mean_grade}
Highest score: {highest_grade}
Lowest score: {lowest_grade}
Range of scores: {grade_range}
Median score: {median_grade}
Question that most people skip: {skip_list}
Question that most people answer incorrectly: {fail_list}
""")
        
    """ Print result to a txt file
    """
    def print_grade(self):
        # Create table with ID and grade column, then extract to txt file
        df = pd.DataFrame({
        "ID": self.valid_table["ID"], 
        "Grade": self.valid_table["Grade"]})
        output_file = f"{self.file_name}_grades.txt"
        df.to_csv(output_file, index=False, header=False)       
        
    """ Check if the printed file is correct or not by compare it with the file in expected output
    """
    def compare_file(self):
        file1 = os.path.join(
            "Expected Output", f"{self.file_name}_grades.txt"
        )
        file2 = f"{self.file_name}_grades.txt"
        
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read().strip()
            content2 = f2.read().strip()
        
        if content1 == content2:
            print("SUCCEEDED!!")
        else:
            print("FAILED!!!")
    
    # Func to run all system
    def process_all(self):
        self.read_file()
        self.clean_file()
        self.mark_result()
        self.describe_grade()
        self.print_grade()
        self.compare_file()


# Run the system and process all steps
if __name__ == "__main__":
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    ID_pattern = r"^N\d{8}$"
    system = Autogradesystem(answer_key.split(","), ID_pattern)
    system.process_all()
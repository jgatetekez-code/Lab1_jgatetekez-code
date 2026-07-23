import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print("Error: The file '{}' was not found.".format(filename)
)
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print("An error occurred while reading the file: {}".format(e))
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)

    for assignment in data:
        if assignment["score"] < 0 or assignment["score"] > 100:
          print("Invalid score found in {}".format(assignment["assignment"]))
          return

    print("All scores are valid.")

# TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    formative_weight = 0
    summative_weight = 0

    for assignment in data:
        if assignment["group"] == "Formative":
           formative_weight += assignment["weight"]
        elif assignment["group"] == "Summative":
           summative_weight += assignment["weight"]

    total_weight = formative_weight + summative_weight

    print("Formative Weight:", formative_weight)
    print("Summative Weight:", summative_weight)
    print("Total Weight:", total_weight)


    # TODO: c) Calculate the Final Grade and GPA

    total_grade = 0
    for assignment in data:
        total_grade += (assignment["score"] * assignment["weight"]) / 100
    GPA = (total_grade / 100) * 5.0

    print(f"Final GPA = {round(GPA, 4)}")

    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)

    total_formative = 0.0
    total_sumamtive = 0.0
    for assignment in data:
        if assignment["group"] == "Formative":
            total_formative += (assignment["score"] * assignment["weight"]) / 100
        else:
            total_sumamtive += (assignment["score"] * assignment["weight"]) / 100

    
    percentage_formative = (total_formative * 100) / 60
    percentage_summative = (total_sumamtive * 100) / 40
    if  percentage_formative >= 50 and percentage_summative >= 50:
        print("Status: PASSED")
    else:
        print("Status: FAILED")
        
    print(f"Formative(60): {round(total_formative, 2)}")
    print(f"Summative(40): {round(total_sumamtive, 2)}")
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.

    resubmission_assignments = []
    low_scored_assignments = []
    individual_weights = []

    for assignment in data:
        if assignment["group"] == "Formative" and assignment["score"] < 50:
            individual_weights.append(assignment["weight"])
            low_scored_assignments.append(assignment)

    if individual_weights:
        highest_weight = max(individual_weights)
        for assignment in low_scored_assignments:
            if assignment["weight"] == highest_weight:
                resubmission_assignments.append(assignment["assignment"])
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)

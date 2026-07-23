# Lab 1: Grade Evaluator & Archiver

## Project Overview

This project automates two important course-related tasks:

1. Evaluating student performance from a CSV grade file using a set of rubric-based rules.
2. Archiving and resetting the working grade file so the next batch of scores can be processed cleanly.

The repository contains:

- `grade-evaluator.py`: reads `grades.csv`, validates the records, calculates the final grade, and prints a PASS/FAIL outcome with resubmission guidance.
- `organizer.sh`: archives the current `grades.csv` file into an `archive/` folder with a timestamp, creates a fresh empty `grades.csv`, and writes a log entry to `organizer.log`.

## Dataset Format

The program expects a CSV file with the following columns:

- `assignment`: the name of the coursework item
- `group`: either `Formative` or `Summative`
- `score`: the score out of 100
- `weight`: the contribution of that assignment to the course total

## Grading Rules Implemented

The evaluator checks the following:

1. All scores must be valid percentages in the range `0` to `100`.
2. The total category weights must align with the course requirements:
   - Formative = 60%
   - Summative = 40%
   - Total = 100%
3. The final grade is computed using weighted scores.
4. The student passes only if both:
   - Formative performance is at least 50%
   - Summative performance is at least 50%
5. For formative assignments below 50%, the script identifies the highest weighted failed item(s) for resubmission.

## Example Input Data

The provided course data is:

```csv
assignment                         , group    , score, weight
Quiz                               , Formative,    85,     20
Group Exercise                     , Formative,    40,     20
Functions and Debugging Lab        , Formative,    45,     20
Midterm Project - Simple Calculator, Summative,    70,     20
Final Project - Text-Based Game    , Summative,    60,     20
```

## Expected Outcome

Using the sample dataset above:

- Formative weighted contribution = 60%
- Summative weighted contribution = 40%
- Final GPA = 3.0
- Status = PASS
- Resubmission recommendation = `Group Exercise` and `Functions and Debugging Lab`

## How to Run

### 1. Run the grade evaluator

```bash
python3 grade-evaluator.py
```

When the script runs, it will prompt for the CSV filename and then print the grading summary to the terminal.

### 2. Archive and reset the grade file

```bash
chmod +x organizer.sh
./organizer.sh
```

This will:

- create the `archive/` directory if it does not exist
- rename `grades.csv` into a timestamped archive file such as `grades_20260723-120000.csv`
- create a new empty `grades.csv`
- append the archive action to `organizer.log`

## File Structure

```text
.
├── grade-evaluator.py
├── organizer.sh
├── grades.csv
├── organizer.log
└── archive/
```

## Purpose of the Project

This lab demonstrates a complete workflow for:

- processing structured grade information
- enforcing grading rules automatically
- archiving course records safely
- keeping the working directory ready for the next class submission batch

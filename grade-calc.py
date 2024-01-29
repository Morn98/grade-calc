#! /usr/bin/env python3 

import argparse
import csv

## color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    LIGHT_GRAY = "\033[0;37m"
    ENDC = '\033[0m'

## class type for the grades
class Grade: 
    def __init__(self, module, grade, ects):
        self.module = module
        self.grade = grade
        self.ects = ects
            
## print arguments
def printArgs(args):
    if args.imp != None or args.exp != None:
        print(Colors.OKBLUE + "### --- Arguments --- ###" + Colors.ENDC)
    if args.imp != None:
        print(Colors.OKBLUE + "[+] Import file: " + args.imp + Colors.ENDC)
    if args.exp != None:
        print(Colors.OKBLUE + "[+] Export file: " + args.exp + Colors.ENDC)

## import csv
def importCsv(args):
    print(Colors.OKCYAN + "[+] Importing CSV file: " + args.imp + Colors.ENDC)
    grades = []
    with open(args.imp, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            module = row['Module']
            grade = float(row['Grade'])
            ects = int(row['ECTS'])
            grades.append(Grade(module, grade, ects))
    return grades

## enter grades
def enterGrades(): 
    print(Colors.OKCYAN + "[+] Entering grades" + Colors.ENDC)
    grades = []
    while True:
        module = input(Colors.LIGHT_GRAY + "Enter module name (exit to calc): " + Colors.ENDC)
        if module == "exit":
            break
        grade = float(input(Colors.LIGHT_GRAY + "Enter grade: " + Colors.ENDC))
        ects = int(input(Colors.LIGHT_GRAY + "Enter ECTS: " + Colors.ENDC))
        grades.append(Grade(module, grade, ects))
    return grades

## calculate grade
def calculateGrade(grades):
    print(Colors.OKCYAN + "[+] Calculating grade" + Colors.ENDC)
    total_weighted_grade = 0
    total_ects = 0
    for grade in grades: 
        total_weighted_grade += grade.grade * grade.ects
        total_ects += grade.ects
    if total_ects == 0:
        return 0
    return total_weighted_grade / total_ects

## print result
def printResult(result):
    print(Colors.OKGREEN + "[+] Result: " + str(result) + Colors.ENDC)

## export csv
def exportCsv(args, grades):
    print(Colors.OKCYAN + "[+] Exporting CSV file: " + args.exp + Colors.ENDC)
    with open(args.exp, 'w', newline='') as csvfile:
        fieldnames = ['Module', 'Grade', 'ECTS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for grade in grades:
            writer.writerow({'Module': grade.module, 'Grade': grade.grade, 'ECTS': grade.ects})

authorSignature = 'grade-calc.py - Published by Moritz Nentwig\n'
authorSignature += '-------------------------------------------'

## print header first
print("")
print(Colors.HEADER + authorSignature + Colors.ENDC)

def main(): 
    ## parse arguments
    parser = argparse.ArgumentParser(
        description='Calculate your grade.',
        epilog='--- grade-calc.py ---', 
        add_help=True)

    parser.add_argument('-i', '--imp', help="CSV import file")
    parser.add_argument('-e', '--exp', help="CSV export file")
    args = parser.parse_args()

    ## print arguments 
    printArgs(args)

    grades = []

    ## import csv
    if (args.imp != None):
        grades = importCsv(args)
    else:
        print("") 
        grades = enterGrades()
        print("")
    
    ## calculate grade
    result = calculateGrade(grades)

    ## print result
    printResult(result)

    ## export csv
    if (args.exp != None):
        exportCsv(args, grades)

## start main
if __name__ == "__main__":
    main()

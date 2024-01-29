# grade-calc
A Python-based grade calculator designed for use during my university studies.

## Build with 
* Python3 

## Usage 

grade-calc.py implements a CLI interface (using [argparse](https://docs.python.org/3/library/argparse.html)):

```bash
python3 grade-calc.py [-h] [-i IMP] [-e EXP]
```

## Where 

- `-i` or `--imp`: The path to the CSV import file. (optional)
- `-e` or `--exp`: The path to the CSV export file. (optional)

## Example: 

### Helper

```bash
python3 grade-calc.py -h

grade-calc.py - Published by Moritz Nentwig
-------------------------------------------
usage: grade-calc.py [-h] [-i IMP] [-e EXP]

Calculate your grade.

options:
  -h, --help         show this help message and exit
  -i IMP, --imp IMP  CSV import file
  -e EXP, --exp EXP  CSV export file

--- grade-calc.py ---
```

### Simple grade calculation

```bash
❯ python3 grade-calc.py

grade-calc.py - Published by Moritz Nentwig
-------------------------------------------

[+] Entering grades
Enter module name (exit to calc): advanced mathematics
Enter grade: 2.3
Enter ECTS: 10
Enter module name (exit to calc): digital forensics
Enter grade: 1.3
Enter ECTS: 5
Enter module name (exit to calc): exit

[+] Calculating grade
[+] Result: 1.9666666666666666
```

### Importing CSV 

```bash
❯ python3 grade-calc.py --imp grades.csv

grade-calc.py - Published by Moritz Nentwig
-------------------------------------------
### --- Arguments --- ###
[+] Import file: grades.csv
[+] Importing CSV file: grades.csv
[+] Calculating grade
[+] Result: 1.9666666666666666

```

### Exporting CSV

```bash
❯ python3 grade-calc.py --exp grades.csv

grade-calc.py - Published by Moritz Nentwig
-------------------------------------------
### --- Arguments --- ###
[+] Export file: grades.csv

[+] Entering grades
Enter module name (exit to calc): advanced mathematics
Enter grade: 2.3
Enter ECTS: 10
Enter module name (exit to calc): digital forensics
Enter grade: 1.3
Enter ECTS: 5
Enter module name (exit to calc): exit

[+] Calculating grade
[+] Result: 1.9666666666666666
[+] Exporting CSV file: grades.csv

```

## Contributing

Feel free to contribute. 

## Authors

* Moritz Nentwig -- Initial idea and work 

## License

This project is licensed under the MIT Licensee -- see the [LICENSE](LICENSE) for details. 
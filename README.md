## data-cleaning-python-coding


Hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. 

The company recently decided to purchase a new HR system, and unfortunatelY, the new system requires employee records be stored completely differently.

The task was to help bridge the gap by creating a Python script able to convert the employee records to the required format. The script will be in the following:


* Imported the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:


```
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* Then converted and export the data to use the following format instead:


```
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

* In summary, the required conversions are as follows:

  * The `Name` column is in split into separate `First Name` and `Last Name` columns.

  * The `DOB` data is in re-written format into `DD/MM/YYYY` format.

  * The `SSN` data is in re-written format such that the first five numbers are hidden from view.

  * The `State` data is in re-written format as simple two-letter abbreviations.
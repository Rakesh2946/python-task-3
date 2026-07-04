Python 3.11.0 (main, Oct 24 2022, 18:13:38) [MSC v.1933 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: D:\Python\python task 3.py =====================
==================================================
EMPLOYEE DATA ANALYSIS USING PANDAS
==================================================

CSV File Loaded Successfully!

First 5 Records
    ID    Name Department   Salary  Experience
0  101  Rakesh  Logistics  35000.0         2.0
1  102     Ram      Sales  45000.0         5.0
2  103    Sita         HR  40000.0         3.0
3  104    Arun  Logistics      NaN         4.0
4  105   Priya      Sales  50000.0         6.0

Dataset Information
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   ID          10 non-null     int64  
 1   Name        10 non-null     object 
 2   Department  10 non-null     object 
 3   Salary      9 non-null      float64
 4   Experience  9 non-null      float64
dtypes: float64(2), int64(1), object(2)
memory usage: 388.0+ bytes
None

Statistical Summary
              ID        Salary  Experience
count   10.00000      9.000000    9.000000
mean   105.50000  42333.333333    4.111111
std      3.02765   4795.831523    1.536591
min    101.00000  35000.000000    2.000000
25%    103.25000  39000.000000    3.000000
50%    105.50000  42000.000000    4.000000
75%    107.75000  45000.000000    5.000000
max    110.00000  50000.000000    6.000000

Missing Values
ID            0
Name          0
Department    0
Salary        1
Experience    1
dtype: int64

Missing values after cleaning
ID            0
Name          0
Department    0
Salary        0
Experience    0
dtype: int64

Employees earning more than 40,000
    ID   Name Department        Salary  Experience
1  102    Ram      Sales  45000.000000         5.0
3  104   Arun  Logistics  42333.333333         4.0
4  105  Priya      Sales  50000.000000         6.0
6  107    Anu  Logistics  42000.000000         5.0
7  108  Vijay      Sales  47000.000000         4.0
9  110    Raj  Logistics  45000.000000         6.0

Average Salary Department Wise
Department
HR           39000.000000
Logistics    41083.333333
Sales        47333.333333
Name: Salary, dtype: float64

Maximum Salary Department Wise
Department
HR           40000.0
Logistics    45000.0
Sales        50000.0
Name: Salary, dtype: float64

Employee Count Department Wise
Department
HR           3
Logistics    4
Sales        3
Name: ID, dtype: int64

Highest Paid Employee
ID                105
Name            Priya
Department      Sales
Salary        50000.0
Experience        6.0
Name: 4, dtype: object

Cleaned dataset saved as cleaned_employees.csv

Analysis Completed Successfully!

# CT22_EKP_Fuzzy

1 / on-prem
main.py
ekfuzzy.py  

run main.py with 1 argument as a SQL statement you want to check for likeness

You need to have a PostGres instance and upload some sql statements you want to check against

the .sql scripts are self-explanatory

Feb 17 2023 :
- the fuzzy computation is now a separate thread it can take as much time as it need
- the reference of SQLs is no autogenerated. Each new SQL you test is added to the reference list

2 / in the Cloud 
coming up next


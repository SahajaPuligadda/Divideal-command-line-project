# Divideal-command-line-project

A command line application to split your expenses and simplify them to their minimum number of transactions possible.

This CLI python app takes the user input and calculates the total debts each person in the group has. At the end, we run Ford-fulkerson or a simple greedy approach to reduce the number of transactions to their minimum.

Input for CLI:

<EXPENSE/SHOW> (Type of splits) (Payee Amount) (No.of users) (Users involved) <Space separated Amounts/Values>

We can make 5 different kinds of splits:

1. EQUAL
2. EXACT
3. SHARES
4. PERCENT
5. ADJUST

SHOW command is used to display the balance sheet (with/without simplify).

We also made a flask application on the same functionality.
You can access the same app from our flask app at https://divideal.pythonanywhere.com/

Thank you.

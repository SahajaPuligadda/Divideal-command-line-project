# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# EXPENSE U6 5000 2 U3 U6 PERCENT 50 50
# EXPENSE U4 2000 3 U1 U2 U3 ADJUST 2000 0 0


from user import *
from split import *
from expense import *
from expenseType import *
from expenseService import *
from expenseManager import *
from ford_fulkerson import *
import os
import json
from balance_sheet import *
from pots import *
from edit_participants import *
import sqlite3
from simplify2 import *


def get_connection():
    connection = sqlite3.connect("database.db")
    return connection


if __name__ == '__main__':
    expenseManager = ExpenseManager()
    max_flow = simplify()
    db_balance_sheet = balancesheet()
    db_pot = pots()
    pot_id = 0
    connection = get_connection()

    expenseManager.addUser(User("U1", "User1", "gaurav@workat.tech", "9876543012"))
    expenseManager.addUser(User("U2", "User2", "sagar@workat.tech", "9874563210"))
    expenseManager.addUser(User("U3", "User3", "hi@workat.tech", "9876543210"))
    expenseManager.addUser(User("U4", "User4", "mock-interviews@workat.tech", "9834375980"))
    expenseManager.addUser(User("U5", "User5", "abc@gmail.com", "9823568310"))
    expenseManager.addUser(User("U6", "User6", "hihello@yahoo.in", "8956382754"))
    expenseManager.addUser(User("U7", "User7", "hi@workat.tech", "9876543210"))
    expenseManager.addUser(User("U8", "User8", "mock-interviews@workat.tech", "9834375980"))
    expenseManager.addUser(User("U9", "User9", "abc@gmail.com", "9823568310"))
    expenseManager.addUser(User("U10", "User10", "hihello@yahoo.in", "8956382754"))

    if input("Enter OPEN or NEW: ") == "OPEN":
        # for file in os.listdir("C:/Users/91880/PycharmProjects/splitwise"):
        #    if file.endswith(".txt"):
        #        print(file)
        # expense_name = input("Enter any 1 filename: ")
        pots = db_pot.get_pots(connection)
        if len(pots) == 0:
            expense_name = input("No pots exist- \nCreate new pot-\nEnter a new pot name: ")
            db_pot.set_pot(expense_name, "3480290sheiefiuv", connection)
            pot_id = db_pot.get_potid(expense_name, connection)
            participant_entry = database_entry()
            participant_entry.add_every_participant(pot_id[0], connection, expenseManager.userMap)
            pot_id = pot_id[0]
        else:
            print(pots)
            pot_id = int(input("Give id of pot: "))
            balancesheet = db_pot.getbalance(pot_id, connection)
            expenseManager.balanceSheet = balancesheet
        # with open(expense_name+".txt") as file:
        #    prev_bal_sheet = json.load(file)
        # expenseManager.balanceSheet = prev_bal_sheet

    else:
        # expense_name = input("Enter a new transaction name: ")
        expense_name = input("Enter a new pot name: ")
        db_pot.set_pot(expense_name, "3480290sheiefiuv", connection)
        pot_id = db_pot.get_potid(expense_name, connection)
        participant_entry = database_entry()
        participant_entry.add_every_participant(pot_id[0], connection, expenseManager.userMap)
        pot_id = pot_id[0]

    while 1:
        commands = input().split()
        commandType = commands[0]

        if commandType == "SHOW":
            if input("Simplify? yes or no: ") == "yes":
                # expenseManager.balanceSheet = max_flow.final_simplify(expenseManager.balanceSheet)
                expenseManager.balanceSheet = simplify.simplify(expenseManager.balanceSheet)
            expenseManager.showBalances()

        elif commandType == "EXPENSE":
            paidby = commands[1]
            amount = float(commands[2])
            noOfUsers = int(commands[3])
            expensetype = commands[4 + noOfUsers]
            splits = []
            item_name = input("Enter description for expense: ")

            if expensetype == "EQUAL":
                for i in range(noOfUsers):
                    splits.append(EqualSplit(expenseManager.userMap.get(commands[4 + i])))
                expenseManager.addExpense(expenseType[2], amount, paidby, splits, pot_id, connection, item_name)

            elif expensetype == "EXACT":
                for i in range(noOfUsers):
                    splits.append(ExactSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                expenseManager.addExpense(expenseType[0], amount, paidby, splits, pot_id, connection, item_name)

            elif expensetype == "PERCENT":
                for i in range(noOfUsers):
                    splits.append(PercentSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                expenseManager.addExpense(expenseType[1], amount, paidby, splits, pot_id, connection, item_name)

            elif expensetype == "SHARES":
                for i in range(noOfUsers):
                    splits.append(SharesSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                expenseManager.addExpense(expenseType[3], amount, paidby, splits, pot_id, connection, item_name)

            elif expensetype == "ADJUST":
                for i in range(noOfUsers):
                    splits.append(AdjustSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                expenseManager.addExpense(expenseType[4], amount, paidby, splits, pot_id, connection, item_name)

            db_balance_sheet.update_balance_sheet(expenseManager.balanceSheet, pot_id, connection)
            connection.commit()

        else:
            # with open(expense_name+".txt", "w") as file:
            #    json.dump(expenseManager.balanceSheet, file)
            # break
            connection.close()
            break

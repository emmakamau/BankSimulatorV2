#!/usr/bin/env python3
import typing
# Set initial balances for account holders
BALANCES :typing.Dict= {'Henry':0, 'Jane':0, 'Akinyi':0,'Mary':0,'Lavender':0,'Wanjiru':0,'Juma':0,'Marigold':0,'Daisy':0,'Linda':0}
WITHDRAWALFEE = 30.00

def bank_simulator():
    # Open and read account logs from account_logs.txt
    with open('logs.txt', 'r') as logs:
        data:typing.List = logs.readlines()
        
        # Define an empty array to hold all logs
        account_logs :typing.List[typing.List]= []

        for logs in data:
            log = logs.split(':') # Split data where there is a :
            account_logs.append(log) # Add each log to the list

        
        for index,log in enumerate(account_logs):
            '''
            Loop through account_logs list checking whether
            a transaction is a Deposit,Withdraw or Transfer
            Deposit - Increment account balance by amount:
                Bal = 0 , Deposit = 100
                Return Bal + Deposit ; 100
            Withdraw - Check account balance, if amount is 
            enough reduce the bal:
                Bal = 500 , Withdraw = 300
                Return Bal-Withdraw ; 200
            Transfer - Check account balance, if amount is 
            enought reduce bal and increase bal for other acc
                Bal acc A = 900, Transfer = 500
                Return Bal acc A Bal-Transfer ; 400
                
                Bal acc B = 200 , Transfer = 500
                Return Bal acc B Bal+Transfer ; 700
            '''
            # BALANCES = {'Wanjiru':0, 'Juma':0, 'Linda':0}
            # List sample - ['DEPOSIT', 'Wanjiru', '152.00\n']
            transaction = log[0].upper()
            if transaction == 'DEPOSIT' and log[1] in BALANCES:
                # float for decimal numbers
                amount = float(BALANCES[log[1]]) + float(log[2])
                BALANCES[log[1]] = amount
                print(index,'Deposit successful:', BALANCES)
            elif transaction == 'WITHDRAW' and log[1] in BALANCES:
                if float(BALANCES[log[1]]) >= (float(log[2]) + WITHDRAWALFEE):
                    amount = float(BALANCES[log[1]]) - (float(log[2]) + WITHDRAWALFEE)
                    BALANCES[log[1]] = amount
                    print(index,'Withdrawal successful:', BALANCES)
                else:
                    print(index,'Insufficient balance:', BALANCES)
            elif transaction == 'CREDIT' and log[1] in BALANCES:
                if float(BALANCES[log[1]]) >= float(log[2]):
                    amount = float(BALANCES[log[1]]) - float(log[2])
                    BALANCES[log[1]] = amount
                    print(index,'Credit successful:', BALANCES)
                else:
                    print(index,'Insufficient balance', BALANCES)
            elif transaction == 'TRANSFER' and log[1] in BALANCES and log[2] in BALANCES and len(log)>3:
                # List sample - ['TRANSFER', 'Juma', 'Linda', '500.00\n']
                if float(BALANCES[log[1]]) >= float(log[3]):
                    BALANCES[log[1]] = float(BALANCES[log[1]])-float(log[3])
                    BALANCES[log[2]] = float(BALANCES[log[2]])+float(log[3])
                    print(index,'Transfer successful:', BALANCES)
                else:
                    print(index,'Insufficient balance:', BALANCES)
            else:
                print(index,'No Transaction')
        print("\n")
        print('Final balances: ',BALANCES)
        return BALANCES

bank_simulator()
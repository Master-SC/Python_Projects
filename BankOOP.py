# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:36:34 2020

@author: TCS WFH
"""


class Bank:
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        
    def owner(self):
        return self.owner
    
    def __str__(self):
        return (f"account Owner: {self.owner}\n"+\
                f"account Balance: ${self.balance}")
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        return "Deposit accepted"
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            return "Withdraw accepted"
        else:
            return "Funds not avilable ..."
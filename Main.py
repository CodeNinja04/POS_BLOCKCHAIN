from Transaction import Transaction
from Wallet import Wallet
import json

if __name__ == '__main__':
    
    sender="sender"
    receiver="receiver"
    amount = 1
    type="TRANSFER"
    
    transaction = Transaction(sender,receiver,amount,type)
    #print(transaction.toJson())
    
    wallet =Wallet()
    signature = wallet.sign(transaction.toJson())
    #print(signature)
    
    
    transaction.sign(signature)
    #print(transaction.toJson())
    
    signatureValid = Wallet.signatureValid(transaction.toJson(),signature,wallet.publicKeyString())
    
    print(signatureValid)
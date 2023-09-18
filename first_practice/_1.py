def amount_payment(payment):
    
    sum_of_payments = 0
    for value in payment:
        if value < 0:
            continue
        sum_of_payments += value
    return sum_of_payments   
            
    
    
amount_payment([1, -3, 4])

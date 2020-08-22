customer1 = {

    "phone": "0244414445",
    "customer_name": "Justice"
    "customer_balance" 11000,
    "pin": "1234"
}

customer2 = {
    "phone": "0245555666",
    "customer_name": "Larry",
    "customer_balance": 500,
    "pin": "4321"


}
vendor= {
    "p": "0245454545",
    "pin": "5768"
    "bal": 5399,
    "name":"kay"

}

telco = {
    "tel_code": 318

}

def deposit ():
    code = input("dial telco code:")
    gh = telco["tel_code"]
    if code== gh:
        cnumber = input("enter momo number:")
        if cnumber==customer["p"]:
        print("ok")

        else:
            print("enter a valid momo number")
        amount= eval(input("enter amount")) 
        if amount >=1:
            print("successful")   
            else:
                print("enter a valid amount.")





                
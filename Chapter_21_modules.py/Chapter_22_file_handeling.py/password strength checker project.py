import re 
def check_password_strength(password):
    strength=0
    remarks=""
    #1.length check 
    if len(password)>=8:
        strength+=1
    else :
        remarks+="password should be atleast 8 characters long "

    #2.upper case 
    if re.search(r"[A-Z]",password):
        strength+=1
    else :
        remarks+="include atleast 1 uppercase letter"

    #3.lower case 
    if re.search(r"[a-z]",password):
        strength+=1
    else :
        remarks+="include atleast 1 lowercase  letter"

    #4.digit 

    if re.search(r"[0-9]",password):
        strength+=1
    else :
        remarks+="include atleast 1 digit letter"

    #5.special symbols 
    if re.search(r"[!,@,#,$,%,^,&,*,(),_,+]",password):
        strength+=1
    else :
        remarkfs+="include atleast 1 special character letter"

    #result 
    if strength ==5:
        return "Strong Password!"
    elif 3<=strength<5:
        return "Moderate Password"+remarks
    else:
        return "Week Passsword"+remarks
    
password=input("Enter your password:")
print(check_password_strength(password))
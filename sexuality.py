print("Hello we can help you detemine your sexuality by answering our questions")
sex=str(input("Are you a male or a female ")).lower()
if (sex=="male"):
    attract1=str(input("Are you attracted your fellow males? yes/no ")).lower()
    attract2=str(input("Are you romantically attracted to females? yes/no ")).lower()
    attract3=str(input("Are you attracted to other things aside humans? yes/no ")).lower()
    
    if attract1=="yes" and attract2=="no" and attract3=="no":
        print("Then you are a homosexual")
    elif attract1=="no" and attract2=="yes" and attract3=="no":
        print("You are hetorosexual")
    elif attract1=="yes" and attract2=="yes" and attract3=="no":
        print("You are a bisexual")
    elif attract1=="yes" and attract2=="yes" and attract3=="yes":
        print("You are a pansexual")
    elif(attract1=="no" and attract2=="no" and attract3=="yes"):
            print("You are a demisexual") 
    elif(attract1=="no" and attract2=="no" and attract3=="no"):
            print("You are an asexual")     
        
if (sex=="female"):
    attract1=str(input("Are you attracted males? yes/no ")).lower()
    attract2=str(input("Are you romantically attracted to your fellow females? yes/no ")).lower()
    attract3=str(input("Are you attracted to other things aside humans? yes/no ")).lower()
    
    if attract1=="yes" and attract2=="no" and attract3=="no":
        print("Then you are a homosexual")
    elif attract1=="no" and attract2=="yes" and attract3=="no":
        print("You are hetorosexual")
    elif attract1=="yes" and attract2=="yes" and attract3=="no":
        print("You are a bisexual")
    elif attract1=="yes" and attract2=="yes" and attract3=="yes":
        print("You are a pansexual")
    elif(attract1=="no" and attract2=="no" and attract3=="yes"):
        print("You are a demisexual")
    elif(attract1=="no" and attract2=="no" and attract3=="no"):
          print("You are an asexual")    
          

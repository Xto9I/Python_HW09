import re

contacts = {}  

def input_error(funk):
      
    def inner(*args,**kwargs):  
        try:
            return funk(*args,**kwargs)
        except KeyError: 
            return "This name does not exist."
        except IndexError:
            return "Did not receive a name or number."
        except:
            return "Option entered incorrectly."
    return inner


@input_error
def add(text):
    phone_number = re.findall(r"\d+", text)[-1]
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    contacts[phone_name] =  phone_number
    return "Number added."


@input_error
def change(text):
    phone_number = re.findall(r"\d+", text)[-1]
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    old_phone_number = contacts[phone_name] 
    contacts[phone_name] =  phone_number
    result = f"{phone_name}\'s number {old_phone_number} changed to {phone_number}."
    return result


@input_error
def end(text):
    return "Good bye!"
    

@input_error
def hello(text):
    return "How can I help you?"


@input_error
def phone(text):
    
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    return contacts[phone_name]


@input_error
def show_all(text):
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    start = True

    while start:
        access = False
        entered_text = input()
        
        for key in user_command.keys():
            if bool(re.search(key, entered_text, flags=re.IGNORECASE)):
                access = True
                print(user_command[key](entered_text))
                if key in ["exit","good bye","close"]:
                    start = False  
                break
        if not access:
            print("Option entered incorrectly...")
               
      
user_command = {
    "add": add,
    "change": change,
    "exit": end,
    "good bye": end,
    "close": end,
    "hello": hello,
    "phone": phone,
    "show all": show_all,
}


if __name__ == "__main__":
    main()
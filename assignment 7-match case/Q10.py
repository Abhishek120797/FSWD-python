color=input("Hey user Enter your favorite color this format (I like red colour) : ")
match color:
    case "I like yellow colour":
        print("Monday")
    case "I like blue colour":
        print("Tuesday")
    case "I like orange colour":
        print("Wednesday")
    case "I like white colour":
        print("Thursday")
    case "I like black colour":
        print("Friday")
    case "I like red colour":
        print("Saturday")
    case _:
        print("Sunday")

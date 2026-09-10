def user_input(requirement):
    print("\n\nEnter 0 To Exit.\n")
    while True:
        print(requirement)
        answer = input("\n> ").lower().strip()
        
        match answer:
            case "0":
                return 0
            case "":
                continue

        return answer

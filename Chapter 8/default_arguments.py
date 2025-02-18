def goodDay(name, ending = "Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Ankit", "Thanks")
goodDay("Ankit")

# Here, ending="" is working as a default parameter. If we will give any value as a second argument then the 'ending' value will be ignored and if we don't give any value then 'ending' value will gets printed as a second argument

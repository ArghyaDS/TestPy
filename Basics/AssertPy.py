#AssertionError handling in simple operation
div=int(input("Enter dividend: "))
divs=int(input("Enter divisor: "))
try:
    assert divs!=0, "You can not divide by zero"
    quo=div/divs
    print(f"Result: {quo}")
except:
    print("You should not try to divide by zero")

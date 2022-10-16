start = input("What number to start with?")
end = input("What number to end with?")
status = input("Even or Odd?")
for i in range(start, end):
    if status == "even":
        if i % 2 == 0:
            print(i)
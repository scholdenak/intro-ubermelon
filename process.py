log_file = open("um-server-01.txt")


def sales_reports(log_file):
#sets funtion with argument
    for line in log_file:
    # iterates over log_file
        line = line.rstrip()
        # breaks apart each line as a new data strip
        day = line[0:3]
        # shows where the day is according to index
        if day == "Mon":
        # creates conditional that acts if the day equals day requested
            print(line)
        # prints out information so its visable in terminal


sales_reports(log_file)

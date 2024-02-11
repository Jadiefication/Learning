import os, pickle, datetime, time

file_name = "server.pkl"

try:
    with open(file_name, "rb") as f:
        list = pickle.load(f)
except Exception as e:
    list = []
    print(e)
    
class Clock:
    
    def clock(self):
        while True:
            time2 = datetime.datetime.now().strftime("%H:%M:%S")
            time.sleep(1)
            return time2
            
class App(Clock):

    def __init__(self, status):
        self.status = status

    def on(self):
        while True:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            list.append(time)
            list.append(date)
            print("Time: ", time, "\nDate: ", date)
            
            while True:
                command = input("Enter command(Use help to print the commands): ").lower()
                if command == "exit":
                    self.off()
                elif command == "status":
                    print(self.status)
                elif command == "directory":
                    print(os.getcwd())
                elif command == "list":
                    print(list)
                elif command == "help":
                    print(" exit - Exit the program, \n status - Check the status of the server, \n directory - Get the current directory, \n list - Show the list of the dates and times the server started")
                else:
                    print("Invalid command")
                
    def off(self):
        print("Server shutting down")
        with open(file_name, "wb") as f:
            pickle.dump(list, f)
        exit()

if __name__ == "__main__":
    app = App("On")
    app.on()

    

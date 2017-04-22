from datetime import datetime
class Message():    
    FILE_NAME = r'C:\MyProjects\msg_test.txt'
    SEVERITIES = {0: 'Critical',
                  1: 'Error',
                  2: 'Important',
                  3: 'Warning',
                  4: 'Information'}

    def __init__(self, severity, text):        
        self.severity = self.SEVERITIES[severity]
        self.text = text
   
    def notify(self):
        echo = True
        log = True
        msg = self.text
        if echo:
            print(msg)
        if log:
            file = open(self.FILE_NAME,'a')
            file.write('['+self.severity+'] ')
            msg = datetime.now().strftime("%y-%m-%d-%H:%M:%S")+' ' + self.text
            file.write(msg)
            file.write('\n')
            file.close()

def main():
    msg = Message(2, 'testing123')
    msg.notify()    
    msg2 = Message(0, 'This is an important message!')
    msg2.notify()
    
if __name__ == "__main__":
    main()


class Logger:
    _instance = None
    messages = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance= super().__new__(cls)
        return cls._instance
    
    def log(self,msg):
        if msg.strip():
            Logger.messages.append(msg)
    
    @classmethod
    def get_logs(cls):
        if cls.messages:
           for msg in cls.messages:
                print(f"{msg}\n")
        else:
            print("No messages!")

    @staticmethod
    def format_msg(msg):
        words = msg.split('_')
        camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
        return camel_case_string
        
logger1 = Logger()
logger2= Logger()
print(logger1 is logger2)

logger1.log("hello_world")
logger2.log("sheetal_kandhare")

Logger.get_logs()

print(Logger.format_msg("hello_world"))
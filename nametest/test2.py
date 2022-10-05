import inspect
import test1

if __name__ == "__main__":
    print("test2.py is running directly")
else:
    print(f"test2.py is running from module {inspect.stack()[-1].filename}")    

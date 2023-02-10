from threading import *
class Java(Thread):
    def run(self):
        for i in range(11):
            print("Learning java")

class Python(Thread):
    def run(self):
        for i in range(11):
            print("Learning python")

def main():
    print("Placements Starts here")
    j = Java()
    j.start()
    p = Python()
    p.start()
    j.join()
    p.join()
    print("Placements ends here")
main()
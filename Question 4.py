class OddNumber:
    def __init__(self):
        self.word=""
        self.output=""

    def indexcheck(self):
        self.word=input("Enter a string = ")

        for i in self.word:
            if self.word.index(i)%2==1:
                self.output+=i

        return self.output

    def print_output(self):
        print("Answer is ", self.output)

if __name__ =="__main__":
    test = OddNumber()
    test.indexcheck()
    test.print_output()
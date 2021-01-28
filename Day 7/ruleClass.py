class Rule:

    def __init__(self, line) -> None:
        temp = line.split(" bags contain ")
        self.bag = temp[0]
        self.contents = dict()
        print("BAG: " + self.bag)

        for content in temp[1].split(", "):
            #remove "bag", "bags" and "."
            content = content.replace(" bag", "")
            content = content.replace("s.", "")
            content = content = content.replace(".", "")
            numBag = content.split(" ")[0]
            typeBag = content.replace(numBag, "")
            print("NUM: {} BAG: {}".format(numBag, typeBag))
            print(content, end = "\n")

        print("CONTENTS: ")
        print(self.contents)
        print("...")



        # self.bag = temp[0]
        # contents = dict()
        # for content in temp[1].split(", "):
        #     contents[content.split(" ")[1]] = content.split(" ")[0]
        # # contents[content] = contents[contents][:-1]
        # self.contents = contents    
        # print(type(self.contents))

    def __str__(self) -> str:
        string = self.bag
        for content in self.contents:
            string += "|" + content

        return string


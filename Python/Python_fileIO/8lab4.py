# 4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.0
def display_words():
    count = 0
    with open("C:\\Users\\DELL\\PycharmProjects\\project 1\\ABC.txt","r") as file:
        file1= file.read()
        text = file1.split()
        for char in text:
            if len(char) <4:
                print(char)
                count += 1
        return count

print(f"total number less than 4 are : {display_words()}")





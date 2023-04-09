from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
import openai


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()
        self.setMinimumSize(800, 600)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 500, 400)
        self.chat_area.setReadOnly(True)
        # add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 520, 400, 40)
        # add button
        self.button = QPushButton("send", self)
        self.button.setGeometry(540, 520, 100, 40)
        self.button.clicked.connect(self.send_message)
        self.Show()


    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333;'>ME: {user_input} </p>")
        self.input_field.clear()


        resource = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333;backrruond-color:#E9E9E9;'>Bot: {resource}</p>")



class Chatbot:
    def __init__(self):
        openai.api_key = "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"
    
    
    def get_response(self, user_input):
        res = openai.Completion.create(
            engine = "text-davinci-003",prompt= user_input, max_tokens = 3000,
            temperature = 0.5
        ).choices[0].text
        return res
        


#app = QApplication(sys.argv)
#main_window = ChatbotWindow()

#sys.exit(app.exec())

chat = Chatbot()
resp = chat.get_response("Write joke for bird")
print(resp)

input()

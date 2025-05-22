from tkinter import *
from antlr4 import InputStream, CommonTokenStream
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser

root = Tk()
root.title("تحليل MyLang")

input_field = Text(root, height=5, width=50)
input_field.pack()

output_field = Text(root, height=10, width=50)
output_field.pack()

def lexical_analysis():
    code = input_field.get("1.0", END).strip()
    if not code:
        output_field.delete("1.0", END)
        output_field.insert(END, "يرجى إدخال كود.")
        return

    input_stream = InputStream(code)
    lexer = MyLangLexer(input_stream)
    tokens = lexer.getAllTokens()

    output_field.delete("1.0", END)
    for token in tokens:
        token_type = token.type
        # التحقق من أن النوع ضمن الحدود
        if 0 <= token_type < len(MyLangLexer.symbolicNames):
            token_name = MyLangLexer.symbolicNames[token_type]
        else:
            token_name = f"UNKNOWN({token_type})"

        output_field.insert(END, f"{token.text} -> {token_name}\n")

# تحليل Syntax
def syntax_analysis():
    code = input_field.get("1.0", END).strip()
    if not code:
        output_field.delete("1.0", END)
        output_field.insert(END, "يرجى إدخال كود.")
        return

    input_stream = InputStream(code)
    lexer = MyLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyLangParser(stream)

    tree = parser.program()
    output_field.delete("1.0", END)
    output_field.insert(END, tree.toStringTree(recog=parser))

# أزرار التحليل
buttons_frame = Frame(root)
buttons_frame.pack()

lexical_button = Button(buttons_frame, text="تحليل Lexical", command=lexical_analysis)
lexical_button.pack(side=LEFT, padx=5)

syntax_button = Button(buttons_frame, text="تحليل Syntax", command=syntax_analysis)
syntax_button.pack(side=LEFT, padx=5)

# تشغيل الواجهة
root.mainloop()

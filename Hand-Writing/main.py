import pywhatkit as pw 

txt = """Python is a high-level interpreted dynamically typed programming language"""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])

print(" END ")


import cgi
import re
import math

form = cgi.FieldStorage()
expr = form.getvalue("expr", "")

expr_clean = re.sub(r'\s+', '', expr)

if expr_clean and not re.fullmatch(r'[\d.+\-*/()^raiz]+', expr_clean):
    resultado = "Expresión inválida. Solo use números, +, -, *, /, **, (), raiz."
else:
    try:
        expr_eval = re.sub(r'raiz', 'math.sqrt', expr_clean)
        expr_eval = re.sub(r'\^', '**', expr_eval)
        resultado = eval(expr_eval, {"__builtins__": None}, {"math": math})
   
    except Exception as e:
        resultado = f"Error en la expresión: {str(e)}"

print("Content-Type: text/html; charset=utf-8\n")


print('''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Web</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <form action="cgi-bin/calculadora.py" method="post">
        <h2>Calculadora</h2>
        <label for="expr">Ingrese la expresion:</label>
        <input type="text" id="expr" name="expr" placeholder="Ej: 12+(34*7/(6-8))-1" value="{}" required>
        <button type="submit">Calcular</button>
    </form>
    <div class="resultado">Resultado: {}</div>
</body>
</html>'''.format(expr, resultado))
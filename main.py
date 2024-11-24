from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro

        # Aplicar descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        # Devolver solo los datos necesarios
        return jsonify({
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento_aplicado': descuento_aplicado,
            'total_a_pagar': total_con_descuento
        })
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return jsonify({'mensaje': mensaje})
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)

var mensaje = "mensaje local";
// var global , let scope local, const constante
//si no declaro entonces siempre hace referencia al mismo objeto
resultado += 2;

var datos = {}; //asi creo una -variable- Obj

//puedo generar propiedades como en python
datos.mensaje = "mensaje local del objeto";
datos.resultado = 120;
//obj.propety = value genera una propiedad ligada a mi objeto

// how to declare a function
function saludar(soy_argumento) {
    console.log(mensaje);
    console.log(resultado);
    console.log(datos.mensaje);
    console.log(datos.resultado);
    console.log("Datos es un objeto: \n" + datos);
    console.log(soy_argumento)
}

saludar(1231231)
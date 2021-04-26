var tienda = {
    nombre: "Tienda las 4 esquinas",
    sumar: function(costo1, costo2) { // permite funciones anonimas == LAMBDA(en python)
        return costo1 + costo2;
    },
    saludar: function() {
        let saludo = "Hola estudiante";
        return saludo;
    },
    saludar_con_nombre: function(name) {
        let persona = name;
        return name + persona;
    }
};
var btnSaludar = document.getElementById("btnSaludar");
// a mi objeto HTML le aplico una funcion de EventListener
// la cual le debo indicar cual evento esta esperando?
// y que logica ejecutar cuando suceda el evento:
//btnSaludar.addEventListener('click', function() { console.log(tienda.saludar('64-bit')); });
btnSaludar.addEventListener("click", function() { console.log(tienda.saludar("Fernando")); })
    // CALL BACK IMPLEMENTATION

var mi_segundo_boton = document.getElementById("Mi_Tipo_De_Botom");
mi_segundo_boton.addEventListener("click", function() { console.log("Segunda function"); });
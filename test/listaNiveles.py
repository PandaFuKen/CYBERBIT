from niveles import nivel1,nivel2,nivel3, nivel4
#Almacenamos los distintos objetos, escenarios de fondo, enemigos, y diseños del suelo para cada nivel
nivel_dict = {
    1: {#En caso de que el nivel seleccionado sea 1, importamos estos datos al juego
        "matriz": nivel1,
        "fondo": "./Assets/images/Fondos/nivelSelva.png",
        "suelo": "./Assets/images/Suelo.png"
    },
    2: {
        "matriz": nivel2,
        "fondo": "./Assets/images/Fondos/nivelCueva.png",
        "suelo": "./Assets/images/Suelo.png"
    },
    3: {
        "matriz": nivel3,
        "fondo": "./Assets/images/Fondos/nivel.png",
        "suelo": "./Assets/images/Suelo2.png"
    },
    4: {
        "matriz": nivel4,
        "fondo": "./Assets/images/Fondos/Fondo4.png",
        "suelo": "./Assets/images/Suelo.png"
    }
}
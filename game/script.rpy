#DEFINICIONES
define protagonista = Character("Carlos Tejedor", color="#f2b118")
#IMAGENES 
image  bg_tarde = "images/bg/bg_tarde.jpg"
image  bg_nubes = "images/bg/bg_nubes.jpg"
image  bg_infierno = "images/bg/bg_infierno.jpg"
image  pj = "images/personajes/pj.png"

#INICIO
label start:

    play music "audio/misterio_bucle.mp3"
    jump  bg_tarde

#ESCENA TARDE
label bg_tarde:
    scene bg_tarde
    show pj at center 
    
    play sound "audio/ladrido.mp3"

    protagonista "hola"

    menu decisión:
        "cielo":
            jump llegas_al_cielo
        " infierno":
            jump llegas_al_infierno       

#ESCENA NUBES
label llegas_al_cielo:
    scene bg_nubes
    show pj 
    play music "audio/paseo.mp3"
    "llegas al cielo. "
    "le robas a san pedro."
    "te hechan de cielo."
    "fin"
    play music "audio/misterio_bucle.mp3"
    jump bg_tarde


#ESCENA INFIERNO
label llegas_al_infierno:
    scene bg_infierno
    show pj
    play music "audio/infierno.mp3"
    protagonista "hace calor"
    "llegas al infierno."
    "el diablo te hecha."
    "fin."
    play music "audio/misterio_bucle.mp3"
    jump bg_tarde


# Modulo2VyO
Modulo 2 Validaciones y Operaciones 

En esta ocasión la base de los programas ha sido la validación directa de casos diferentes de la misma situación. En el primer programa debiamos sepra tres tipos 
diferentes de las longitudes de una palabra mediante su longitud y enbase a ello originar una respuesta difrentes. La primra complicación era asegurarnos de que 
lo que nos ofreciera el usuario era una cadena exclusiv de letras, evitando signos y numeros, y obligarlo a que cada vez que cometiera un error su respuesta fuera 
de nuevo exigida y eso se logra mediante los ciclos . Una vez hecho esto era una cuestion simple de separación mediante condicionales y comparación de longitudes
la aplicacion del caso correspondiente. Unicamente por gramatica agregue el caso de una sola letra, para que no quedara rara la redacción para la respuesta al usuario,
pero bien se puede prescindir de él.

En el caso del cartesiano tuvimos que validar que exclusivamente se nos dieran numero y no cualquier otro simbolo, por lo cual usamos una validación usando una 
estructura try except para cachar el error de conversion mediante la funcion int para un numero y asi dirimir qué valores pasaban, forzando al usuario a dar un valor 
válido mediante ciclos while infinitos o controlados por banderas si esperabamos una respuesta del usuario para continuar o reiniciar el proceso.
Una vez obtenidos los números, bastaba con una serie de condicionales if para separa los casos y aplicar la respuesta apropiada.


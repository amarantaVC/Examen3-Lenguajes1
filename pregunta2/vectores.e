-- CI3641 - LENGUAJES DE PROGRAMACION I
-- EXAMEN3 - PREGUNTA 4
-- AMARANTA VILLEGAS 16-11247
-- Vectores.e : Dadas dos vectores del mismo tamaño (representados como un arreglo), realizar
-- el producto punto.

-- Funcion para calcular el producto punto de dos vectores
function producto_punto(vector1, vector2)
    suma := 0
    for i = 1 to length(vector1) do
        suma += vector1[i] * vector2[i]
    end for
    return suma
end function

-- Función para realizar el calculo en una tarea
function tarea_producto_punto(vector1, vector2, resultado)
    resultado[1] = producto_punto(vector1, vector2)
end function

-- Vectores de ejemplo
vector_a = {1, 2, 3, 4, 5}
vector_b = {5, 4, 3, 2, 1}

-- Resultado del producto punto (inicializado con cero)
resultado = {0}

-- Crear la tarea
tarea := task_create(routine_id(tarea_producto_punto), {vector_a, vector_b, resultado})

-- Programar la tarea
task_schedule(tarea, {0, 0})

-- Esperar a que la tarea termine
task_wait(tarea)

-- El resultado estará en la posición 1 del arreglo "resultado"
printf("El producto punto es: %d\n", resultado[1])

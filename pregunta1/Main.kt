/*
CI3641 - LENGUAJES DE PROGRAMACION I 
EXAMEN3 - PREGUNTA 1
AMARANTA VILLEGAS 16-11247
*/


//SECUENCIA: Es una interfaz que representa una colección ordenada de elementos. 
//Debe tener los siguientes métodos: agregar, remover y vacio.
// agregar recibe un elemento y lo agrega a la secuencia, remover devuelve un elemento de la secuencia
// y lo elimina de la misma. Arroja error si esta vacia.
// vacio dice si la secuencia esta vacia, es decir, que no tiene elementos.

interface Secuencia<T> {
    fun agregar(t: T)
    fun remover(): T
    fun vacio(): Boolean
}

// PILA: Es una clase en la que los elementos se manejan de tal forma que el último en ser agregado
// es el primero en ser removido.

class Pila<T> : Secuencia<T> {
    private val elementos = mutableListOf<T>()

    override fun agregar(t: T) {
        elementos.add(t)
    }

    @Throws(RuntimeException::class)
    override fun remover(): T {
        if (vacio()) {
            throw RuntimeException("Pila Vacia")
        }
        return elementos.removeAt(elementos.size - 1)
    }

    override fun vacio(): Boolean {
        return elementos.isEmpty()
    }

    override fun toString(): String {
        return elementos.joinToString(" <- ", postfix = " <- null")
    }
}

// COLA:Es una clase en la que los elementos se manejan de tal forma que el primero en ser agregado es el
// primero en ser removido.
class Cola<T> : Secuencia<T> {
    private val elementos = mutableListOf<T>()

    override fun agregar(t: T) {
        elementos.add(t)
    }

    @Throws(RuntimeException::class)
    override fun remover(): T {
        if (vacio()) {
            throw RuntimeException("Cola Vacia")
        }
        return elementos.removeAt(0)
    }

    override fun vacio(): Boolean {
        return elementos.isEmpty()
    }

    override fun toString(): String {
        return elementos.joinToString(" <- ", postfix = " <- null")
    }
}

// Definición del tipo de datos para representar grafos como listas de adyacencias
class Grafo {
    private val adyacencias: MutableMap<Int, MutableList<Int>> = mutableMapOf()

    val numV: Int
        get() = adyacencias.keys.size

    fun agregarArista(origen: Int, destino: Int) {
        adyacencias.getOrPut(origen) { mutableListOf() }.add(destino)
        adyacencias.getOrPut(destino) { mutableListOf() }.add(origen)
    }

    fun obtenerNodosAdyacentes(nodo: Int): List<Int> {
        return adyacencias[nodo] ?: emptyList()
    }
}

// Definición de la clase abstracta Busqueda
abstract class Busqueda(var grafo: Grafo) {
    abstract var sec: Secuencia<Int>

    /**
     * Función que determina el número de vértices explorados
     * en la búsqueda de un vértice, partiendo desde otro
     * Args:
     *    D (Int): Vértice de partida
     *    H (Int): Vértice buscado
     * Retorna:
     *    Int: Número de vértices explorados en la búsqueda, si no
     *    encuentra el vértice, retorna -1
     */
    fun buscar(D: Int, H: Int): Int {
        val maxVertex = grafo.numV
        val color = IntArray(maxVertex)
        var u: Int
        var count: Int = 0

        color[D] = 1
        sec.agregar(D)

        while (!(sec.vacio())) {
            u = sec.remover()
            count++
            if (u == H) {
                return count
            }
            grafo.obtenerNodosAdyacentes(u).forEach {
                if (it < maxVertex && color[it] == 0) {
                    color[it] = 1
                    sec.agregar(it)
                }
            }
        }

        return -1
    }
}


// Implementación de la clase concreta DFS
class DFS(grafo: Grafo) : Busqueda(grafo) {
    override var sec: Secuencia<Int> = Pila<Int>()
}

// Implementación de la clase concreta BFS
class BFS(grafo: Grafo) : Busqueda(grafo) {
    override var sec: Secuencia<Int> = Cola<Int>()
}


//el main para probar las clases

fun main() {
    val pila : Pila<Int> = Pila<Int>()
    val cola : Cola<Int> = Cola<Int>()

    println("Pila inicial vacia? ${pila.vacio()}")

    for (i in (0..3)){
        pila.agregar(i)
    }

    for (i in (0..3)){
        println("El tope de la pila es: ${pila.remover()}")
    }

    println("Pila final vacia? ${pila.vacio()}")

    try {
        pila.remover()
    } catch (e : RuntimeException){
        println("Excepcion de pila vacia capturada")
    }


    println("------------------------------------------------------")
    println("Cola inicial vacia? ${cola.vacio()}")

    for (i in (0..5)){
        cola.agregar(i)
    }

    for (i in (0..5)){
        println("El tope de la cola es: ${cola.remover()}")
    }

    println("cola final vacia? ${cola.vacio()}")

    try {
        cola.remover()
    } catch (e : RuntimeException){
        println("Excepcion de cola vacia capturada")
    }

    println("EL GRAFOOOOOOOOOOOOOOOOOOOO")
       // Crear un grafo de ejemplo
    val grafo = Grafo()
    grafo.agregarArista(1, 2)
    grafo.agregarArista(1, 3)
    grafo.agregarArista(2, 4)
    grafo.agregarArista(2, 5)
    grafo.agregarArista(3, 6)

    // Mostrar resultados de búsqueda DFS
    val dfs = DFS(grafo)
    val nodosExploradosDFS = dfs.buscar(1, 5)
    println("DFS: Nodos explorados desde 1 hasta 5: $nodosExploradosDFS")

    // Mostrar resultados de búsqueda BFS
    val bfs = BFS(grafo)
    val nodosExploradosBFS = bfs.buscar(1, 5)
    println("BFS: Nodos explorados desde 1 hasta 5: $nodosExploradosBFS")
}
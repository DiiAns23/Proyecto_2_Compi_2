/*----HEADER----*/
package main

var t0, t1, t2, t3, t4, t5 float64
var P, H float64
var stack [30101999]float64
var heap [30101999]float64

func main() {
	/* Compilacion del Struct Datos */
	/* Compilacion de valor de variable */
	/* Creando Struct Datos */
	t0 = H
	t1 = H
	H = H + 3

	t2 = H
	heap[int(H)] = 68
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 103
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t1)] = t2
	t1 = t1 + 1

	t3 = H
	heap[int(H)] = 79
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t1)] = t3
	t1 = t1 + 1

	/* Compilacion del Array */
	t4 = H
	t5 = t4 + 1
	heap[int(H)] = 3
	H = H + 4

	heap[int(t5)] = 1
	t5 = t5 + 1

	heap[int(t5)] = 2
	t5 = t5 + 1

	heap[int(t5)] = 3
	t5 = t5 + 1

	heap[int(t1)] = t4
	t1 = t1 + 1

	/* Fin de la asignacion */
	stack[int(1)] = t0
	/* Fin de valor de variable */

}

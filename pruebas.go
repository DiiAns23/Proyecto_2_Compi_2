/*----HEADER----*/
package main

var t0, t1, t2, t3, t4, t5 float64
var P, H float64
var stack [30101999]float64
var heap [30101999]float64

func main() {
	/* Compilacion del Array */
	t0 = H
	t1 = t0 + 1
	heap[int(H)] = 4
	H = H + 5

	heap[int(t1)] = 1
	t1 = t1 + 1

	heap[int(t1)] = 2
	t1 = t1 + 1

	heap[int(t1)] = 3
	t1 = t1 + 1

	/* Compilacion del Array */
	t2 = H
	t3 = t2 + 1
	heap[int(H)] = 2
	H = H + 3

	heap[int(t3)] = 4
	t3 = t3 + 1

	/* Compilacion del Array */
	t4 = H
	t5 = t4 + 1
	heap[int(H)] = 2
	H = H + 3

	heap[int(t5)] = 5
	t5 = t5 + 1

	heap[int(t5)] = 6
	t5 = t5 + 1

	heap[int(t3)] = t4
	t3 = t3 + 1

	heap[int(t1)] = t2
	t1 = t1 + 1

	stack[int(0)] = t0
	/* Fin de la compilacion del Array */

}

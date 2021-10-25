/*----HEADER----*/
package main

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11 float64
var P, H float64
var stack [50]float64
var heap [50]float64

/*-----NATIVES-----*/
func printString() {
	t7 = P + 1
	t8 = stack[int(t7)]
L5:
	t9 = heap[int(t8)]
	if t9 == -1 {
		goto L4
	}
	fmt.Printf("%c", int(t9))
	t8 = t8 + 1
	goto L5
L4:
	return
}

func main() {
	/* Compilacion de valor de variable */
	t0 = H
	heap[int(H)] = 79
	H = H + 1
	heap[int(H)] = 76
	H = H + 1
	heap[int(H)] = 67
	H = H + 1
	heap[int(H)] = 50
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	stack[int(0)] = t0
	/* Fin de valor de variable */

	/* Inicia Loop For */
	/* Compilacion de Acceso */
	t1 = stack[int(0)]
	/* Fin compilacion acceso */

L0:
	/* Compilacion de valor de variable */
	stack[int(1)] = t1
	/* Fin de valor de variable */
	t2 = stack[int(1)]
	t3 = heap[int(t2)]
	if t3 != -1 {
		goto L1
	}
	goto L2
L1:
	/* Compilacion de Acceso */
	t4 = stack[int(1)]
	/* Fin compilacion acceso */

	t5 = heap[int(t4)]
	fmt.Printf("%c", int(t5))
	t6 = H
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t10 = P + 2
	t10 = t10 + 1
	stack[int(t10)] = t6
	P = P + 2
	printString()
	t11 = stack[int(P)]
	P = P - 2
	goto L3
L3:
	t1 = t1 + 1
	goto L0
L2:
}

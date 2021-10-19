package main

import (
	"fmt"
)

var stack [100]float64
var heap [100]float64
var sp, hp float64
var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27 float64

func printString() {
	t16 = sp + 1
	t17 = stack[int(t16)]
l0:
	t18 = heap[int(t17)]
	if t18 == -1 {
		goto l1
	}
	fmt.Printf("%c", int(t18))
	t17 = t17 + 1
	goto l0
l1:
}

func main() {
	t0 = hp
	heap[int(hp)] = 68
	hp = hp + 1
	heap[int(hp)] = 105
	hp = hp + 1
	heap[int(hp)] = 101
	hp = hp + 1
	heap[int(hp)] = 103
	hp = hp + 1
	heap[int(hp)] = 111
	hp = hp + 1
	heap[int(hp)] = -1
	hp = hp + 1
	stack[int(0)] = t0

	t1 = hp
	heap[int(hp)] = 74
	hp = hp + 1
	heap[int(hp)] = 111
	hp = hp + 1
	heap[int(hp)] = 115
	hp = hp + 1
	heap[int(hp)] = 101
	hp = hp + 1
	heap[int(hp)] = -1
	hp = hp + 1
	stack[int(1)] = t1

	t2 = hp
	heap[int(hp)] = 75
	hp = hp + 1
	heap[int(hp)] = 114
	hp = hp + 1
	heap[int(hp)] = 105
	hp = hp + 1
	heap[int(hp)] = 115
	hp = hp + 1
	heap[int(hp)] = -1
	hp = hp + 1
	stack[int(2)] = t2

	t3 = hp
	t4 = t3 + 1       // Se establece la posicion del primer elemento
	heap[int(hp)] = 3 // En la primera posicion se pone el tamño del vector
	hp = hp + 4       // Se reserva el espacio del vector y su tamño

	t5 = stack[0]
	heap[int(t4)] = t5
	t4 = t4 + 1
	t6 = stack[1]
	heap[int(t4)] = t6
	t4 = t4 + 1
	t7 = stack[2]
	heap[int(t4)] = t7
	t4 = t4 + 1

	stack[int(3)] = t3

	t8 = stack[3]
	stack[int(4)] = t8

	t10 = stack[4]
	t11 = hp
	heap[int(hp)] = 67
	hp = hp + 1
	heap[int(hp)] = 97
	hp = hp + 1
	heap[int(hp)] = 109
	hp = hp + 1
	heap[int(hp)] = 98
	hp = hp + 1
	heap[int(hp)] = 105
	hp = hp + 1
	heap[int(hp)] = 111
	hp = hp + 1
	heap[int(hp)] = -1
	hp = hp + 1
	t9 = t10 + 2        // posicion de elemento accedido
	heap[int(t9)] = t11 // cambito de valor
	t12 = stack[3]
	t13 = t12            // Se obtiene indice de inicio del arreglo en el heap
	t14 = t13 + 2        // Se obtiene el indice del elemento deseado del arreglo en el heap
	t15 = heap[int(t14)] // Se obtiene el elemento deseado

	/* Inicio paso de parametros */
	t19 = sp + 6
	stack[int(t19)] = t15
	/* Fin paso de parametros */

	/* Inicio llamda a nativa de impresion */
	sp = sp + 5
	printString()
	sp = sp - 5
	/* Fin llamda a nativa de impresion */

	fmt.Printf("%c", 10)

	t20 = stack[4]
	t21 = t20            // Se obtiene indice de inicio del arreglo en el heap
	t22 = t21 + 2        // Se obtiene el indice del elemento deseado del arreglo en el heap
	t23 = heap[int(t22)] // Se obtiene el elemento deseado

	/* Inicio paso de parametros */
	t27 = sp + 6
	stack[int(t27)] = t23
	/* Fin paso de parametros */

	/* Inicio llamda a nativa de impresion */
	sp = sp + 5
	printString()
	sp = sp - 5
	/* Fin llamda a nativa de impresion */

	fmt.Printf("%c", 10)

}

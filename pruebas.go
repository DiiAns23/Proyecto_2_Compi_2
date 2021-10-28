/*----HEADER----*/
package main

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38,
	t39, t40 float64
var P, H float64
var stack [30101999]float64
var heap [30101999]float64

/*-----NATIVES-----*/
func length() {
	t3 = P + 1
	t4 = stack[int(t3)]
	t5 = heap[int(t4)]
	stack[int(P)] = t5
	goto L1
L1:
	return
}
func BoundsError() {
	fmt.Printf("%c", int(66))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(110))
	fmt.Printf("%c", int(100))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(10))
	return
}

/*-----FUNCS-----*/
func array() {
	/* Llamada de la Funcion length */
	/* Compilacion de Acceso */
	t1 = P + 1
	t0 = stack[int(t1)]
	/* Fin compilacion acceso */

	t2 = P + 3
	stack[int(t2)] = t0
	P = P + 2
	length()
	t2 = stack[int(P)]
	P = P - 2
	/* Fin de la llamada a la funcion length */

	fmt.Printf("%d", int(t2))
	fmt.Printf("%c", int(10))
	/* Llamada de la Funcion length */
	/* Compilacion de Acceso de la variable array */
	t7 = P + 1
	t6 = stack[int(t7)]
	t8 = t6 + 1
	if 1 < 1 {
		goto L2
	}
	t10 = heap[int(t6)]
	if 1 > t10 {
		goto L2
	}
	goto L3
L2:
	BoundsError()
	goto L4
L3:
	t9 = heap[int(t8)]
	goto L4
L4:
	/* Fin compilacion de acceso de la variable array */
	t11 = P + 3
	stack[int(t11)] = t9
	P = P + 2
	length()
	t11 = stack[int(P)]
	P = P - 2
	/* Fin de la llamada a la funcion length */

	fmt.Printf("%d", int(t11))
	fmt.Printf("%c", int(10))
	/* Llamada de la Funcion length */
	/* Compilacion de Acceso de la variable array */
	t13 = P + 1
	t12 = stack[int(t13)]
	t14 = t12 + 1
	if 1 < 1 {
		goto L5
	}
	t16 = heap[int(t12)]
	if 1 > t16 {
		goto L5
	}
	goto L6
L5:
	BoundsError()
	goto L7
L6:
	t15 = heap[int(t14)]
	goto L7
L7:
	t17 = t15 + 1
	if 1 < 1 {
		goto L8
	}
	t19 = heap[int(t15)]
	if 1 > t19 {
		goto L8
	}
	goto L9
L8:
	BoundsError()
	goto L10
L9:
	t18 = heap[int(t17)]
	goto L10
L10:
	/* Fin compilacion de acceso de la variable array */
	t20 = P + 3
	stack[int(t20)] = t18
	P = P + 2
	length()
	t20 = stack[int(P)]
	P = P - 2
	/* Fin de la llamada a la funcion length */

	fmt.Printf("%d", int(t20))
	fmt.Printf("%c", int(10))
	goto L0
L0:
	/* Fin de la Compilacion de la Funcion array */
	return
}

func main() {
	/* Compilacion de la Funcion array */

	/* Compilacion del Array */
	t21 = H
	t22 = t21 + 1
	heap[int(H)] = 2
	H = H + 3

	/* Compilacion del Array */
	t23 = H
	t24 = t23 + 1
	heap[int(H)] = 3
	H = H + 4

	/* Compilacion del Array */
	t25 = H
	t26 = t25 + 1
	heap[int(H)] = 4
	H = H + 5

	heap[int(t26)] = 1
	t26 = t26 + 1

	heap[int(t26)] = 2
	t26 = t26 + 1

	heap[int(t26)] = 3
	t26 = t26 + 1

	heap[int(t26)] = 4
	t26 = t26 + 1

	heap[int(t24)] = t25
	t24 = t24 + 1

	/* Compilacion del Array */
	t27 = H
	t28 = t27 + 1
	heap[int(H)] = 4
	H = H + 5

	heap[int(t28)] = 5
	t28 = t28 + 1

	heap[int(t28)] = 6
	t28 = t28 + 1

	heap[int(t28)] = 7
	t28 = t28 + 1

	heap[int(t28)] = 8
	t28 = t28 + 1

	heap[int(t24)] = t27
	t24 = t24 + 1

	/* Compilacion del Array */
	t29 = H
	t30 = t29 + 1
	heap[int(H)] = 4
	H = H + 5

	heap[int(t30)] = 9
	t30 = t30 + 1

	heap[int(t30)] = 0
	t30 = t30 + 1

	heap[int(t30)] = 1
	t30 = t30 + 1

	heap[int(t30)] = 2
	t30 = t30 + 1

	heap[int(t24)] = t29
	t24 = t24 + 1

	heap[int(t22)] = t23
	t22 = t22 + 1

	/* Compilacion del Array */
	t31 = H
	t32 = t31 + 1
	heap[int(H)] = 3
	H = H + 4

	/* Compilacion del Array */
	t33 = H
	t34 = t33 + 1
	heap[int(H)] = 4
	H = H + 5

	heap[int(t34)] = 1
	t34 = t34 + 1

	heap[int(t34)] = 2
	t34 = t34 + 1

	heap[int(t34)] = 3
	t34 = t34 + 1

	heap[int(t34)] = 4
	t34 = t34 + 1

	heap[int(t32)] = t33
	t32 = t32 + 1

	/* Compilacion del Array */
	t35 = H
	t36 = t35 + 1
	heap[int(H)] = 4
	H = H + 5

	heap[int(t36)] = 5
	t36 = t36 + 1

	heap[int(t36)] = 6
	t36 = t36 + 1

	heap[int(t36)] = 7
	t36 = t36 + 1

	heap[int(t36)] = 8
	t36 = t36 + 1

	heap[int(t32)] = t35
	t32 = t32 + 1

	/* Compilacion del Array */
	t37 = H
	t38 = t37 + 1
	heap[int(H)] = 4
	H = H + 5

	heap[int(t38)] = 9
	t38 = t38 + 1

	heap[int(t38)] = 0
	t38 = t38 + 1

	heap[int(t38)] = 1
	t38 = t38 + 1

	heap[int(t38)] = 2
	t38 = t38 + 1

	heap[int(t32)] = t37
	t32 = t32 + 1

	heap[int(t22)] = t31
	t22 = t22 + 1

	stack[int(0)] = t21
	/* Fin de la compilacion del Array */
	/* Llamada de la Funcion array */
	/* Compilacion de Acceso */
	t39 = stack[int(0)]
	/* Fin compilacion acceso */

	t40 = P + 2
	stack[int(t40)] = t39
	P = P + 1
	array()
	t40 = stack[int(P)]
	P = P - 1
	/* Fin de la llamada a la funcion array */

}

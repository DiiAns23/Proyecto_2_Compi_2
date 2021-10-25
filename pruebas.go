/*----HEADER----*/
package main

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23,
	t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80,
	t81, t82, t83, t84, t85, t86, t87, t88, t89, t90, t91, t92, t93, t94, t95, t96, t97, t98 float64
var P, H float64
var stack [100]float64
var heap [100]float64

/*-----NATIVES-----*/
func length() {
	t29 = P + 1
	t30 = stack[int(t29)]
	t31 = heap[int(t30)]
	stack[int(P)] = t31
	goto L12
L12:
	return
}
func potencia() {
	t76 = P + 1
	t75 = stack[int(t76)]
	t77 = t75
	t78 = t75
	t76 = P + 2
	t75 = stack[int(t76)]
	if t75 == 0 {
		goto L25
	}
L26:
	if t75 <= 1 {
		goto L24
	}
	t77 = t77 * t78
	t75 = t75 - 1
	goto L26
L24:
	stack[int(P)] = t77
	goto L27
L25:
	stack[int(P)] = 1
L27:
	return
}

/*-----FUNCS-----*/
func swap() {
	/* Compilacion de valor de variable */
	/* Compilacion de Acceso de la variable arr */
	t1 = P + 3
	t0 = stack[int(t1)]
	/* Compilacion de Acceso */
	t5 = P + 1
	t4 = stack[int(t5)]
	/* Fin compilacion acceso */

	t2 = t0 + t4
	if t4 < 1 {
		goto L1
	}
	if t4 > 0 {
		goto L1
	}
	goto L2
L1:
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
	goto L3
L2:
	t3 = heap[int(t2)]
	goto L3
L3:
	/* Fin compilacion de acceso de la variable arr */
	t6 = P + 4
	stack[int(t6)] = t3
	/* Fin de valor de variable */

	/* Compilacion de Cambio de Valor */
	t8 = P + 3
	t9 = stack[int(t8)]
	/* Compilacion de Acceso de la variable arr */
	t11 = P + 3
	t10 = stack[int(t11)]
	/* Compilacion de Acceso */
	t15 = P + 2
	t14 = stack[int(t15)]
	/* Fin compilacion acceso */

	t12 = t10 + t14
	if t14 < 1 {
		goto L4
	}
	if t14 > 0 {
		goto L4
	}
	goto L5
L4:
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
	goto L6
L5:
	t13 = heap[int(t12)]
	goto L6
L6:
	/* Fin compilacion de acceso de la variable arr */
	/* Compilacion de Acceso */
	t17 = P + 1
	t16 = stack[int(t17)]
	/* Fin compilacion acceso */

	t7 = t9 + t16
	heap[int(t7)] = t13
	/* Fin de compilacion de Cambio de Valor */

	/* Compilacion de Cambio de Valor */
	t19 = P + 3
	t20 = stack[int(t19)]
	/* Compilacion de Acceso */
	t22 = P + 4
	t21 = stack[int(t22)]
	/* Fin compilacion acceso */

	/* Compilacion de Acceso */
	t24 = P + 2
	t23 = stack[int(t24)]
	/* Fin compilacion acceso */

	t18 = t20 + t23
	heap[int(t18)] = t21
	/* Fin de compilacion de Cambio de Valor */

	goto L0
L0:
	/* Fin de la Compilacion de la Funcion swap */
	return
}
func bubbleSort() {
	/* Inicia Loop For */
	/* Compilacion de valor de variable */
	t25 = P + 2
	stack[int(t25)] = 0
	/* Fin de valor de variable */

	/* Llamada de la Funcion length */
	/* Compilacion de Acceso */
	t27 = P + 1
	t26 = stack[int(t27)]
	/* Fin compilacion acceso */

	t28 = P + 4
	stack[int(t28)] = t26
	P = P + 3
	length()
	t28 = stack[int(P)]
	P = P - 3
	/* Fin de la llamada a la funcion length */

	t32 = t28 - 1
L8:
	t33 = P + 2
	t34 = stack[int(t33)]
	if t34 <= t32 {
		goto L9
	}
	goto L10
L9:
	/* Inicia Loop For */
	/* Compilacion de valor de variable */
	t35 = P + 3
	stack[int(t35)] = 1
	/* Fin de valor de variable */

	/* Llamada de la Funcion length */
	/* Compilacion de Acceso */
	t37 = P + 1
	t36 = stack[int(t37)]
	/* Fin compilacion acceso */

	t38 = P + 5
	stack[int(t38)] = t36
	P = P + 4
	length()
	t38 = stack[int(P)]
	P = P - 4
	/* Fin de la llamada a la funcion length */

	t39 = t38 - 1
L13:
	t40 = P + 3
	t41 = stack[int(t40)]
	if t41 <= t39 {
		goto L14
	}
	goto L15
L14:
	/* Inicia condicional If */
	/* Inicio de la expresion relacional */
	/* Compilacion de Acceso de la variable arr */
	t43 = P + 1
	t42 = stack[int(t43)]
	/* Compilacion de Acceso */
	t47 = P + 3
	t46 = stack[int(t47)]
	/* Fin compilacion acceso */

	t44 = t42 + t46
	if t46 < 1 {
		goto L17
	}
	if t46 > 0 {
		goto L17
	}
	goto L18
L17:
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
	goto L19
L18:
	t45 = heap[int(t44)]
	goto L19
L19:
	/* Fin compilacion de acceso de la variable arr */
	/* Compilacion de Acceso de la variable arr */
	t49 = P + 1
	t48 = stack[int(t49)]
	/* Compilacion de Acceso */
	t53 = P + 3
	t52 = stack[int(t53)]
	/* Fin compilacion acceso */

	t54 = t52 + 1
	t50 = t48 + t54
	if t54 < 1 {
		goto L20
	}
	if t54 > 0 {
		goto L20
	}
	goto L21
L20:
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
	goto L22
L21:
	t51 = heap[int(t50)]
	goto L22
L22:
	/* Fin compilacion de acceso de la variable arr */
	/* Fin de la expresion Relacional */

	/* Llamada de la Funcion swap */
	/* Compilacion de Acceso */
	t56 = P + 3
	t55 = stack[int(t56)]
	/* Fin compilacion acceso */

	/* Compilacion de Acceso */
	t58 = P + 3
	t57 = stack[int(t58)]
	/* Fin compilacion acceso */

	t59 = t57 + 1
	/* Compilacion de Acceso */
	t61 = P + 1
	t60 = stack[int(t61)]
	/* Fin compilacion acceso */

	t62 = P + 5
	stack[int(t62)] = t55
	t62 = t62 + 1
	stack[int(t62)] = t59
	t62 = t62 + 1
	stack[int(t62)] = t60
	P = P + 4
	swap()
	t62 = stack[int(P)]
	P = P - 4
	/* Fin de la llamada a la funcion swap */

	goto L23

L23:
	/* Termina condicional If */
	goto L16
L16:
	t63 = P + 3
	t64 = P + 3
	t65 = stack[int(t64)]
	t66 = t65 + 1
	stack[int(t63)] = t66
	goto L13
L15:

	goto L11
L11:
	t67 = P + 2
	t68 = P + 2
	t69 = stack[int(t68)]
	t70 = t69 + 1
	stack[int(t67)] = t70
	goto L8
L10:

	goto L7
L7:
	/* Fin de la Compilacion de la Funcion bubbleSort */
	return
}

func main() {
	/* Compilacion de la Funcion swap */

	/* Compilacion de la Funcion bubbleSort */

	/* Compilacion del Array */
	t71 = H
	t72 = t71 + 1
	heap[int(H)] = 16
	H = H + 17

	heap[int(t72)] = 32
	t72 = t72 + 1

	t73 = 7 * 3
	heap[int(t72)] = t73
	t72 = t72 + 1

	heap[int(t72)] = 7
	t72 = t72 + 1

	heap[int(t72)] = 89
	t72 = t72 + 1

	heap[int(t72)] = 56
	t72 = t72 + 1

	heap[int(t72)] = 909
	t72 = t72 + 1

	heap[int(t72)] = 109
	t72 = t72 + 1

	heap[int(t72)] = 2
	t72 = t72 + 1

	heap[int(t72)] = 9
	t72 = t72 + 1

	t79 = P + 0
	t79 = t79 + 1
	stack[int(t79)] = 9874
	t79 = t79 + 1
	stack[int(t79)] = 0
	P = P + 0
	potencia()
	t74 = stack[int(P)]
	P = P - 0
	heap[int(t72)] = t74
	t72 = t72 + 1

	heap[int(t72)] = 44
	t72 = t72 + 1

	heap[int(t72)] = 3
	t72 = t72 + 1

	t80 = 820 * 10
	heap[int(t72)] = t80
	t72 = t72 + 1

	heap[int(t72)] = 11
	t72 = t72 + 1

	t81 = 8 * 0
	t82 = t81 + 8
	heap[int(t72)] = t82
	t72 = t72 + 1

	heap[int(t72)] = 10
	t72 = t72 + 1

	stack[int(0)] = t71
	/* Fin de la compilacion del Array */
	/* Llamada de la Funcion bubbleSort */
	/* Compilacion de Acceso */
	t83 = stack[int(0)]
	/* Fin compilacion acceso */

	t84 = P + 2
	stack[int(t84)] = t83
	P = P + 1
	bubbleSort()
	t84 = stack[int(P)]
	P = P - 1
	/* Fin de la llamada a la funcion bubbleSort */

	/* Inicia Loop For */
	/* Compilacion de valor de variable */
	t85 = P + 1
	stack[int(t85)] = 1
	/* Fin de valor de variable */

	/* Llamada de la Funcion length */
	/* Compilacion de Acceso */
	t86 = stack[int(0)]
	/* Fin compilacion acceso */

	t87 = P + 3
	stack[int(t87)] = t86
	P = P + 2
	length()
	t87 = stack[int(P)]
	P = P - 2
	/* Fin de la llamada a la funcion length */

L28:
	t88 = P + 1
	t89 = stack[int(t88)]
	if t89 <= t87 {
		goto L29
	}
	goto L30
L29:
	/* Compilacion de Acceso de la variable arreglo */
	t90 = stack[int(0)]
	/* Compilacion de Acceso */
	t94 = P + 1
	t93 = stack[int(t94)]
	/* Fin compilacion acceso */

	t91 = t90 + t93
	if t93 < 1 {
		goto L32
	}
	if t93 > 16 {
		goto L32
	}
	goto L33
L32:
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
	goto L34
L33:
	t92 = heap[int(t91)]
	goto L34
L34:
	/* Fin compilacion de acceso de la variable arreglo */
	fmt.Printf("%d", int(t92))
	fmt.Printf("%c", int(10))
	goto L31
L31:
	t95 = P + 1
	t96 = P + 1
	t97 = stack[int(t96)]
	t98 = t97 + 1
	stack[int(t95)] = t98
	goto L28
L30:
}

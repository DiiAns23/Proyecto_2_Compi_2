/*----HEADER----*/
package main

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99, t100, t101, t102, t103, t104, t105, t106, t107, t108, t109, t110, t111, t112, t113, t114, t115, t116, t117, t118, t119 float64
var P, H float64
var stack [500]float64
var heap [1000]float64

/*-----NATIVES-----*/
func printString() {
	t31 = P + 1
	t32 = stack[int(t31)]
L5:
	t33 = heap[int(t32)]
	if t33 == -1 {
		goto L4
	}
	fmt.Printf("%c", int(t33))
	t32 = t32 + 1
	goto L5
L4:
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
func contratar() {
	/* Creando Struct Contrato */
	t12 = H
	t13 = H
	H = H + 2

	/* Compilacion de Acceso */
	t15 = P + 1
	t14 = stack[int(t15)]
	/* Fin compilacion acceso */

	heap[int(t13)] = t14
	t13 = t13 + 1

	/* Compilacion de Acceso */
	t17 = P + 2
	t16 = stack[int(t17)]
	/* Fin compilacion acceso */

	heap[int(t13)] = t16
	t13 = t13 + 1

	/* Fin de la asignacion */
	/* Resultado a retornar en la funcion */
	stack[int(P)] = t12
	goto L0
	/* Fin del resultado a retornar */
	goto L0
L0:
	/* Fin de la Compilacion de la Funcion contratar */
	return
}
func crearActor() {
	/* Creando Struct Actor */
	t18 = H
	t19 = H
	H = H + 2

	/* Compilacion de Acceso */
	t21 = P + 1
	t20 = stack[int(t21)]
	/* Fin compilacion acceso */

	heap[int(t19)] = t20
	t19 = t19 + 1

	/* Compilacion de Acceso */
	t23 = P + 2
	t22 = stack[int(t23)]
	/* Fin compilacion acceso */

	heap[int(t19)] = t22
	t19 = t19 + 1

	/* Fin de la asignacion */
	/* Resultado a retornar en la funcion */
	stack[int(P)] = t18
	goto L1
	/* Fin del resultado a retornar */
	goto L1
L1:
	/* Fin de la Compilacion de la Funcion crearActor */
	return
}
func crearPelicula() {
	/* Creando Struct Pelicula */
	t24 = H
	t25 = H
	H = H + 2

	/* Compilacion de Acceso */
	t27 = P + 1
	t26 = stack[int(t27)]
	/* Fin compilacion acceso */

	heap[int(t25)] = t26
	t25 = t25 + 1

	/* Compilacion de Acceso */
	t29 = P + 2
	t28 = stack[int(t29)]
	/* Fin compilacion acceso */

	heap[int(t25)] = t28
	t25 = t25 + 1

	/* Fin de la asignacion */
	/* Resultado a retornar en la funcion */
	stack[int(P)] = t24
	goto L2
	/* Fin del resultado a retornar */
	goto L2
L2:
	/* Fin de la Compilacion de la Funcion crearPelicula */
	return
}
func imprimir() {
	t30 = H
	heap[int(H)] = 65
	H = H + 1
	heap[int(H)] = 99
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 58
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t34 = P + 2
	t34 = t34 + 1
	stack[int(t34)] = t30
	P = P + 2
	printString()
	t35 = stack[int(P)]
	P = P - 2
	/* Compilacion de Acceso de la variable contrato */
	t39 = P + 1
	t36 = stack[int(t39)]
	t37 = t36 + 0
	t38 = heap[int(t37)]
	t37 = t38 + 0
	t38 = heap[int(t37)]
	t40 = P + 2
	t40 = t40 + 1
	stack[int(t40)] = t38
	P = P + 2
	printString()
	t41 = stack[int(P)]
	P = P - 2
	t42 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 69
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 58
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t43 = P + 2
	t43 = t43 + 1
	stack[int(t43)] = t42
	P = P + 2
	printString()
	t44 = stack[int(P)]
	P = P - 2
	/* Compilacion de Acceso de la variable contrato */
	t48 = P + 1
	t45 = stack[int(t48)]
	t46 = t45 + 0
	t47 = heap[int(t46)]
	t46 = t47 + 1
	t47 = heap[int(t46)]
	fmt.Printf("%d", int(t47))
	fmt.Printf("%c", int(10))
	t49 = H
	heap[int(H)] = 80
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 99
	H = H + 1
	heap[int(H)] = 117
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 58
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t50 = P + 2
	t50 = t50 + 1
	stack[int(t50)] = t49
	P = P + 2
	printString()
	t51 = stack[int(P)]
	P = P - 2
	/* Compilacion de Acceso de la variable contrato */
	t55 = P + 1
	t52 = stack[int(t55)]
	t53 = t52 + 1
	t54 = heap[int(t53)]
	t53 = t54 + 0
	t54 = heap[int(t53)]
	t56 = P + 2
	t56 = t56 + 1
	stack[int(t56)] = t54
	P = P + 2
	printString()
	t57 = stack[int(P)]
	P = P - 2
	t58 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 71
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 58
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t59 = P + 2
	t59 = t59 + 1
	stack[int(t59)] = t58
	P = P + 2
	printString()
	t60 = stack[int(P)]
	P = P - 2
	/* Compilacion de Acceso de la variable contrato */
	t64 = P + 1
	t61 = stack[int(t64)]
	t62 = t61 + 1
	t63 = heap[int(t62)]
	t62 = t63 + 1
	t63 = heap[int(t62)]
	fmt.Printf("%d", int(t63))
	fmt.Printf("%c", int(10))
	goto L3
L3:
	/* Fin de la Compilacion de la Funcion imprimir */
	return
}
func contratos() {
	/* Inicia Loop For */
	/* Compilacion de valor de variable */
	t65 = P + 1
	stack[int(t65)] = 1
	/* Fin de valor de variable */

	t66 = 1 * 1
	t67 = t66 + 2
L7:
	t68 = P + 1
	t69 = stack[int(t68)]
	if t69 <= t67 {
		goto L8
	}
	goto L9
L8:
	/* Compilacion de valor de variable */
	/* Creando Struct Contrato */
	t70 = H
	t71 = H
	H = H + 2

	/* Guardado de temporales */
	/* Fin de guardado de temporales */
	/* Creando Struct Actor */
	t73 = H
	t74 = H
	H = H + 2

	t75 = H
	heap[int(H)] = -1
	H = H + 1
	heap[int(t74)] = t75
	t74 = t74 + 1

	heap[int(t74)] = 0
	t74 = t74 + 1

	/* Fin de la asignacion */
	/* Recuperacion de Temporales */
	/* Fin de recuperacion de temporales */
	/* Guardado de temporales */
	/* Fin de guardado de temporales */
	/* Creando Struct Pelicula */
	t78 = H
	t79 = H
	H = H + 2

	t80 = H
	heap[int(H)] = -1
	H = H + 1
	heap[int(t79)] = t80
	t79 = t79 + 1

	heap[int(t79)] = 0
	t79 = t79 + 1

	/* Fin de la asignacion */
	/* Recuperacion de Temporales */
	/* Fin de recuperacion de temporales */
	/* Fin de la asignacion */
	t82 = P + 2
	stack[int(t82)] = t70
	/* Fin de valor de variable */

	/* Inicia condicional If */
	/* Inicio de la expresion relacional */
	/* Compilacion de Acceso */
	t84 = P + 1
	t83 = stack[int(t84)]
	/* Fin compilacion acceso */

	if t83 < 4 {
		goto L11
	}
	goto L12
	/* Fin de la expresion Relacional */

L11:
	/* Compilacion de valor de variable */
	/* Llamada de la Funcion crearActor */
	/* Compilacion de Acceso de la variable actores */
	t85 = stack[int(0)]
	/* Compilacion de Acceso */
	t90 = P + 1
	t89 = stack[int(t90)]
	/* Fin compilacion acceso */

	t86 = t85 + t89
	if t89 < 1 {
		goto L13
	}
	t88 = heap[int(t85)]
	if t89 > t88 {
		goto L13
	}
	goto L14
L13:
	BoundsError()
	goto L15
L14:
	t87 = heap[int(t86)]
	goto L15
L15:
	/* Fin compilacion de acceso de la variable actores */
	/* Compilacion de Acceso */
	t92 = P + 1
	t91 = stack[int(t92)]
	/* Fin compilacion acceso */

	t93 = t91 + 38
	t94 = P + 4
	stack[int(t94)] = t87
	t94 = t94 + 1
	stack[int(t94)] = t93
	P = P + 3
	crearActor()
	t94 = stack[int(P)]
	P = P - 3
	/* Fin de la llamada a la funcion crearActor */

	t95 = P + 3
	stack[int(t95)] = t94
	/* Fin de valor de variable */

	/* Compilacion de valor de variable */
	/* Llamada de la Funcion crearPelicula */
	/* Compilacion de Acceso de la variable peliculas */
	t96 = stack[int(1)]
	/* Compilacion de Acceso */
	t101 = P + 1
	t100 = stack[int(t101)]
	/* Fin compilacion acceso */

	t97 = t96 + t100
	if t100 < 1 {
		goto L16
	}
	t99 = heap[int(t96)]
	if t100 > t99 {
		goto L16
	}
	goto L17
L16:
	BoundsError()
	goto L18
L17:
	t98 = heap[int(t97)]
	goto L18
L18:
	/* Fin compilacion de acceso de la variable peliculas */
	/* Compilacion de Acceso */
	t103 = P + 1
	t102 = stack[int(t103)]
	/* Fin compilacion acceso */

	t104 = P + 5
	stack[int(t104)] = t98
	t104 = t104 + 1
	stack[int(t104)] = t102
	P = P + 4
	crearPelicula()
	t104 = stack[int(P)]
	P = P - 4
	/* Fin de la llamada a la funcion crearPelicula */

	t105 = P + 4
	stack[int(t105)] = t104
	/* Fin de valor de variable */

	/* Compilacion de valor de variable */
	/* Llamada de la Funcion contratar */
	/* Compilacion de Acceso */
	t107 = P + 3
	t106 = stack[int(t107)]
	/* Fin compilacion acceso */

	/* Compilacion de Acceso */
	t109 = P + 4
	t108 = stack[int(t109)]
	/* Fin compilacion acceso */

	t110 = P + 6
	P = P + 5
	contratar()
	t110 = stack[int(P)]
	P = P - 5
	/* Fin de la llamada a la funcion contratar */

	t111 = P + 2
	stack[int(t111)] = t110
	/* Fin de valor de variable */

	goto L19
L12:
L19:
	/* Termina condicional If */
	/* Llamada de la Funcion imprimir */
	/* Compilacion de Acceso */
	t113 = P + 2
	t112 = stack[int(t113)]
	/* Fin compilacion acceso */

	t114 = P + 4
	P = P + 3
	imprimir()
	t114 = stack[int(P)]
	P = P - 3
	/* Fin de la llamada a la funcion imprimir */

	goto L10
L10:
	t115 = P + 1
	t116 = P + 1
	t117 = stack[int(t116)]
	t118 = t117 + 1
	stack[int(t115)] = t118
	goto L7
L9:

	goto L6
L6:
	/* Fin de la Compilacion de la Funcion contratos */
	return
}

func main() {
	/* Compilacion del Struct Actor */
	/* Compilacion del Struct Pelicula */
	/* Compilacion del Struct Contrato */
	/* Compilacion del Array */
	t0 = H
	t1 = t0 + 1
	heap[int(H)] = 4
	H = H + 5

	t2 = H
	heap[int(H)] = 69
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 122
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 104
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 79
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t1)] = t2
	t1 = t1 + 1

	t3 = H
	heap[int(H)] = 65
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 109
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 83
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t1)] = t3
	t1 = t1 + 1

	t4 = H
	heap[int(H)] = 67
	H = H + 1
	heap[int(H)] = 104
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 66
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t1)] = t4
	t1 = t1 + 1

	t5 = H
	heap[int(H)] = 74
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 102
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 65
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t1)] = t5
	t1 = t1 + 1

	stack[int(0)] = t0
	/* Fin de la compilacion del Array */
	/* Compilacion del Array */
	t6 = H
	t7 = t6 + 1
	heap[int(H)] = 4
	H = H + 5

	t8 = H
	heap[int(H)] = 65
	H = H + 1
	heap[int(H)] = 118
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 103
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = 58
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 65
	H = H + 1
	heap[int(H)] = 103
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 102
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 85
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t7)] = t8
	t7 = t7 + 1

	t9 = H
	heap[int(H)] = 77
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 46
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 68
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t7)] = t9
	t7 = t7 + 1

	t10 = H
	heap[int(H)] = 66
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 109
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 58
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 84
	H = H + 1
	heap[int(H)] = 104
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 68
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 107
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 75
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 103
	H = H + 1
	heap[int(H)] = 104
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t7)] = t10
	t7 = t7 + 1

	t11 = H
	heap[int(H)] = 77
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 121
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 38
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 77
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	heap[int(t7)] = t11
	t7 = t7 + 1

	stack[int(1)] = t6
	/* Fin de la compilacion del Array */
	/* Compilacion de la Funcion contratar */

	/* Compilacion de la Funcion crearActor */

	/* Compilacion de la Funcion crearPelicula */

	/* Compilacion de la Funcion imprimir */

	/* Compilacion de la Funcion contratos */

	/* Llamada de la Funcion contratos */
	t119 = P + 3
	P = P + 2
	contratos()
	t119 = stack[int(P)]
	P = P - 2
	/* Fin de la llamada a la funcion contratos */

}

/*----HEADER----*/
package main

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11 float64
var P, H float64
var stack [30101999]float64
var heap [30101999]float64

/*-----FUNCS-----*/
func factorial() {
	/* Inicia condicional If */
	/* Inicio de la expresion relacional */
	/* Compilacion de Acceso */
	t1 = P + 1
	t0 = stack[int(t1)]
	/* Fin compilacion acceso */

	if t0 == 1 {
		goto L1
	}
	goto L2
	/* Fin de la expresion Relacional */

L1:
	/* Resultado a retornar en la funcion */
	stack[int(P)] = 1
	goto L0
	/* Fin del resultado a retornar */
	goto L3
L2:
	/* Compilacion de Acceso */
	t3 = P + 1
	t2 = stack[int(t3)]
	/* Fin compilacion acceso */

	/* Guardado de temporales */
	t4 = P + 2
	stack[int(t4)] = t2
	/* Fin de guardado de temporales */
	/* Llamada de la Funcion factorial */
	/* Compilacion de Acceso */
	t6 = P + 1
	t5 = stack[int(t6)]
	/* Fin compilacion acceso */

	t7 = t5 - 1
	t8 = P + 4
	stack[int(t8)] = t7
	P = P + 3
	factorial()
	t8 = stack[int(P)]
	P = P - 3
	/* Fin de la llamada a la funcion factorial */

	/* Recuperacion de Temporales */
	t9 = P + 2
	t2 = stack[int(t9)]
	/* Fin de recuperacion de temporales */
	t10 = t2 * t8
	/* Resultado a retornar en la funcion */
	stack[int(P)] = t10
	goto L0
	/* Fin del resultado a retornar */
L3:
	/* Termina condicional If */
	goto L0
L0:
	/* Fin de la Compilacion de la Funcion factorial */
	return
}

func main() {
	/* Compilacion de la Funcion factorial */

	/* Llamada de la Funcion factorial */
	t11 = P + 1
	stack[int(t11)] = 5
	P = P + 0
	factorial()
	t11 = stack[int(P)]
	P = P - 0
	/* Fin de la llamada a la funcion factorial */

	fmt.Printf("%d", int(t11))
	fmt.Printf("%c", int(10))

}

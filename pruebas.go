/*----HEADER----*/
package main;

import(
        "fmt"
);
var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;



func main(){
        /* Compilacion de valor de variable */
        stack[int(0)]=20;
        /* Fin de valor de variable */

        /* Compilacion de valor de variable */
        stack[int(1)]=40;
        /* Fin de valor de variable */

        /* Inicia Loop For */
        /* Compilacion de valor de variable */
        stack[int(0)]=1;
        /* Fin de valor de variable */

        L0:
        t1 = P + 2;
        t0=stack[int(t1)];
        if t0 <= 4 {goto L1;}
        goto L2;
        L1:
        /* Compilacion de Acceso */
        t2=stack[int(0)];
        /* Fin compilacion acceso */

        fmt.Printf("%d", int(t2));
        fmt.Printf("%c", int(10));
        /* Compilacion de valor de variable */
        stack[int(1)]=10;
        /* Fin de valor de variable */

        /* Compilacion de Acceso */
        t3=stack[int(1)];
        /* Fin compilacion acceso */

        fmt.Printf("%d", int(t3));
        fmt.Printf("%c", int(10));
        /* Compilacion de valor de variable */
        t4 = P + 2;
        stack[int(t4)]=40;
        /* Fin de valor de variable */

        goto L3;
        L3:
        t5 = P + 2;
        t7 = P + 2;
        t6=stack[int(t7)];
        t8 = t6 + 1;
        stack[int(t5)]=t8;
        goto L0;
        L2:

        /* Compilacion de Acceso */
        t9=stack[int(0)];
        /* Fin compilacion acceso */

        fmt.Printf("%d", int(t9));
        fmt.Printf("%c", int(10));
        /* Compilacion de Acceso */
        t10=stack[int(1)];
        /* Fin compilacion acceso */

        fmt.Printf("%d", int(t10));
        fmt.Printf("%c", int(10));
        /* Compilacion de Acceso */
        fmt.Printf("%c", int(10));

}
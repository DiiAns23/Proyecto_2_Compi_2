package main

import (
	"fmt"
	"math"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99, t100 float64
var P, H float64
var stack [30101999]float64
var heap [30101999]float64

func printString() {
	t2 = P + 1
	t3 = stack[int(t2)]
L1:
	t4 = heap[int(t3)]
	if t4 == -1 {
		goto L0
	}
	fmt.Printf("%c", int(t4))
	t3 = t3 + 1
	goto L1
L0:
	return
}

func potencia() {
	t27 = P + 1
	t26 = stack[int(t27)]
	t28 = t26
	t29 = t26
	t27 = P + 2
	t26 = stack[int(t27)]
	if t26 == 0 {
		goto L5
	}
L6:
	if t26 <= 1 {
		goto L4
	}
	t28 = t28 * t29
	t26 = t26 - 1
	goto L6
L4:
	stack[int(P)] = t28
	goto L7
L5:
	stack[int(P)] = 1
L7:
	return
}

func compareString() {
	t76 = P + 1
	t77 = stack[int(t76)]
	t76 = t76 + 1
	t78 = stack[int(t76)]
L37:
	t79 = heap[int(t77)]
	t80 = heap[int(t78)]
	if t79 != t80 {
		goto L39
	}
	if t79 == -1 {
		goto L38
	}
	t77 = t77 + 1
	t78 = t78 + 1
	goto L37
L38:
	stack[int(P)] = 1
	goto L36
L39:
	stack[int(P)] = 0
L36:
	return
}

func main() {
	stack[int(0)] = 1
	stack[int(1)] = 10
	stack[int(2)] = 2021.202
	t0 = stack[int(0)]
	fmt.Printf("%d", int(t0))
	t1 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t5 = P + 3
	t5 = t5 + 1
	stack[int(t5)] = t1
	P = P + 3
	printString()
	t6 = stack[int(P)]
	P = P - 3
	t7 = stack[int(1)]
	fmt.Printf("%d", int(t7))
	t8 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t9 = P + 3
	t9 = t9 + 1
	stack[int(t9)] = t8
	P = P + 3
	printString()
	t10 = stack[int(P)]
	P = P - 3
	t11 = stack[int(2)]
	fmt.Printf("%f", t11)
	fmt.Printf("%c", int(10))
	t12 = H
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t13 = P + 3
	t13 = t13 + 1
	stack[int(t13)] = t12
	P = P + 3
	printString()
	t14 = stack[int(P)]
	P = P - 3
	fmt.Printf("%c", int(10))
	t15 = stack[int(0)]
	t16 = t15 + 41
	t17 = 123 * 4
	t18 = 2 * 2
	t19 = 2 + t18
	if t19 != 0 {
		goto L2
	}
	fmt.Printf("%c", int(77))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(104))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(10))
	t21 = 0
	goto L3
L2:
	t20 = t17 / t19
L3:
	t22 = t16 - t20
	t23 = math.Mod(125, 5)
	t24 = 10 + t23
	t30 = P + 3
	t30 = t30 + 1
	stack[int(t30)] = 2
	t30 = t30 + 1
	stack[int(t30)] = 2
	P = P + 3
	potencia()
	t25 = stack[int(P)]
	P = P - 3
	t31 = t24 * t25
	t32 = t22 - t31
	stack[int(0)] = t32
	t33 = 0 - 10
	t34 = 12 + t33
	t35 = math.Mod(11, t34)
	t36 = 11 * t35
	if 2 != 0 {
		goto L8
	}
	fmt.Printf("%c", int(77))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(104))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(10))
	t38 = 0
	goto L9
L8:
	t37 = 22 / 2
L9:
	t39 = t36 + t37
	stack[int(1)] = t39
	t41 = P + 3
	t41 = t41 + 1
	stack[int(t41)] = 12
	t41 = t41 + 1
	stack[int(t41)] = 2
	P = P + 3
	potencia()
	t40 = stack[int(P)]
	P = P - 3
	t42 = 5 * t40
	t44 = P + 3
	t44 = t44 + 1
	stack[int(t44)] = 2
	t44 = t44 + 1
	stack[int(t44)] = t42
	P = P + 3
	potencia()
	t43 = stack[int(P)]
	P = P - 3
	if 5 != 0 {
		goto L10
	}
	fmt.Printf("%c", int(77))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(104))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(10))
	t46 = 0
	goto L11
L10:
	t45 = 25 / 5
L11:
	t47 = t43 + t45
	stack[int(2)] = t47
	t48 = H
	heap[int(H)] = 80
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 103
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 99
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 243
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 118
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 121
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 109
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 116
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 99
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t49 = P + 3
	t49 = t49 + 1
	stack[int(t49)] = t48
	P = P + 3
	printString()
	t50 = stack[int(P)]
	P = P - 3
	fmt.Printf("%c", int(10))
	t51 = stack[int(0)]
	fmt.Printf("%f", t51)
	t52 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t53 = P + 3
	t53 = t53 + 1
	stack[int(t53)] = t52
	P = P + 3
	printString()
	t54 = stack[int(P)]
	P = P - 3
	t55 = stack[int(1)]
	fmt.Printf("%f", t55)
	t56 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t57 = P + 3
	t57 = t57 + 1
	stack[int(t57)] = t56
	P = P + 3
	printString()
	t58 = stack[int(P)]
	P = P - 3
	t59 = stack[int(2)]
	fmt.Printf("%f", t59)
	fmt.Printf("%c", int(10))
	t60 = H
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t61 = P + 3
	t61 = t61 + 1
	stack[int(t61)] = t60
	P = P + 3
	printString()
	t62 = stack[int(P)]
	P = P - 3
	fmt.Printf("%c", int(10))
	t63 = stack[int(0)]
	t64 = stack[int(1)]
	t65 = t63 - t64
	if t65 != 24 {
		goto L14
	}
L15:
	goto L16
	goto L14
L16:
	goto L17
	goto L12
L17:
	if 5 < 5 {
		goto L14
	}
L14:
	t66 = 7 * 7
	t67 = 15 + 555
	if t66 == t67 {
		goto L18
	}
L18:
	t68 = 0 - 61
	if t68 <= 51 {
		goto L13
	}
L12:
	stack[int(3)] = 1
	goto L19
L13:
	stack[int(3)] = 0
L19:
	t69 = 7 * 7
	t70 = 15 + 555
	if t69 > t70 {
		goto L21
	}
	if 1 >= 2 {
		goto L21
	}
	stack[int(4)] = 1
	goto L23
L21:
	stack[int(4)] = 0
L23:
	if 0 != 0 {
		goto L28
	}
	t71 = 1
	goto L29
L28:
	t71 = 0
L29:
	if 532 <= 532 {
		goto L31
	}
	t72 = 1
	goto L32
L31:
	t72 = 0
L32:
	if t71 == t72 {
		goto L34
	}
L33:
	t73 = 1
	goto L35
L34:
	t73 = 0
L35:
	t74 = H
	heap[int(H)] = 72
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t75 = H
	heap[int(H)] = 72
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t81 = P + 5
	t81 = t81 + 1
	stack[int(t81)] = t74
	t81 = t81 + 1
	stack[int(t81)] = t75
	P = P + 5
	compareString()
	t82 = stack[int(P)]
	P = P - 5
	if t82 != 1 {
		goto L41
	}
L40:
	t83 = 1
	goto L42
L41:
	t83 = 0
L42:
	if t73 != t83 {
		goto L25
	}
L26:
	goto L43
	goto L24
L43:
	goto L45
	goto L44
L44:
	t84 = 1
	goto L46
L45:
	t84 = 0
L46:
	goto L47
	goto L48
L47:
	t85 = 1
	goto L49
L48:
	t85 = 0
L49:
	if t84 != t85 {
		goto L25
	}
L24:
	stack[int(5)] = 1
	goto L50
L25:
	stack[int(5)] = 0
L50:
	t86 = H
	heap[int(H)] = 80
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 100
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 114
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 99
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 110
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 101
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 121
	H = H + 1
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = 108
	H = H + 1
	heap[int(H)] = 111
	H = H + 1
	heap[int(H)] = 103
	H = H + 1
	heap[int(H)] = 105
	H = H + 1
	heap[int(H)] = 99
	H = H + 1
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 115
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t87 = P + 6
	t87 = t87 + 1
	stack[int(t87)] = t86
	P = P + 6
	printString()
	t88 = stack[int(P)]
	P = P - 6
	fmt.Printf("%c", int(10))
	t89 = stack[int(3)]
	if t89 != 1 {
		goto L52
	}
L51:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
	goto L53
L52:
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
L53:
	t90 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t91 = P + 6
	t91 = t91 + 1
	stack[int(t91)] = t90
	P = P + 6
	printString()
	t92 = stack[int(P)]
	P = P - 6
	t93 = stack[int(4)]
	if t93 != 1 {
		goto L55
	}
L54:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
	goto L56
L55:
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
L56:
	t94 = H
	heap[int(H)] = 32
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t95 = P + 6
	t95 = t95 + 1
	stack[int(t95)] = t94
	P = P + 6
	printString()
	t96 = stack[int(P)]
	P = P - 6
	t97 = stack[int(5)]
	if t97 != 1 {
		goto L58
	}
L57:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
	goto L59
L58:
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
L59:
	fmt.Printf("%c", int(10))
	t98 = H
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = 45
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	t99 = P + 6
	t99 = t99 + 1
	stack[int(t99)] = t98
	P = P + 6
	printString()
	t100 = stack[int(P)]
	P = P - 6
	fmt.Printf("%c", int(10))
}

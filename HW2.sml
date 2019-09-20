(*
Eric Furukawa
Assignment 2

Discussion Note: I Helped explain to Jimmy Zheng my approaches vaguely on problems IN WORDS ONLY
*)




(*Helper Functions*)
fun fold f base [] = base
|	fold f base (x::rest) = f x (fold f base rest)

fun filter pred [] = []
|	filter pred (x::rest) =
	if (pred x) then x::(filter pred rest)
	else (filter pred rest)
;

(*Problem 1*)
(*a*)
fun merge2 L [] = L
|	merge2 [] L = L
|	merge2 (x::L1) (y::L2) =
	if (x >= y) then y::(merge2 (x::L1) L2)
	else x::(merge2 L1 (y::L2))
;
(*merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]
;
merge2 [1,2,3] [4,5]
;*)
(*b*)
fun merge2Tail L [] = L
|	merge2Tail [] L = L
|	merge2Tail L1 L2 =
	let
	fun revAppend [] L = L
	|	revAppend (x::rest) L = revAppend rest (x::L)
	fun merger L [] acc = (revAppend L acc)
	|	merger [] L acc = (revAppend L acc)
	|	merger (x::L1) (y::L2) acc =
		if (x >= y) then merger (x::L1) L2 (y::acc)
		else merger L1 (y::L2) (x::acc)
	in
	rev(merger L1 L2 [])
	end
;
(*merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]
;*)
(*c*)
fun mergeN [[]] = []
|	mergeN LL = (fold merge2 [] LL)
;
(*mergeN [[1,2],[10,12],[2,5,6,8,9]]
;*)

(*Problem 2*)
(*a*)
fun getInRange v1 v2 [] = []
|	getInRange v1 v2 L =
	let
	fun greaterThan x =
	if (x > v1) then true
	else false
	
	fun lesserThan x =
	if (x < v2) then true
	else false
	
	in
	filter greaterThan (filter lesserThan L)
	end
;
(*getInRange 3 10 [1,2,3,4,5,6,7,8,9,10,11]
;*)
(*b*)
fun countInRange v1 v2 [[]] = 0
|	countInRange v1 v2 LL =
	let
	fun turnOne x = 1
	fun add x y  = x + y
	fun getInRangeHelp L = fold add 0 (map turnOne (getInRange v1 v2 L))
	in
	fold add 0 (map getInRangeHelp LL)
	end
;
(*LENGTH Version*)
(*fun countInRange v1 v2 [[]] = 0
|	countInRange v1 v2 LL =
	let
	fun length [] = 0
	|	length (x::rest) = length rest + 1 (*For non-recursive, could map all array values to 1 and total for length*)
	fun add x y  = x + y
	fun getInRangeHelp L = length (getInRange v1 v2 L)
	in
	fold add 0 (map getInRangeHelp LL)
	end
;*)
(*countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]
;*)

(*Problem 3*)
(*a*)
datatype lengthUnit = INCH of int | FOOT of int | YARD of int

fun addLengths (INCH I1) (INCH I2) = INCH(I1+I2)
|	addLengths (INCH I1) (FOOT F1) = INCH(I1+(12*F1))
|	addLengths (INCH I1) (YARD Y1) = INCH(I1+(36*Y1))
|	addLengths (FOOT F1) (FOOT F2) = INCH((F1*12) + (F2*12))
|	addLengths (FOOT F1) (YARD Y1) = INCH((F1*12) + (Y1*36))
|	addLengths (YARD Y1) (YARD Y2) = INCH((Y1*36) + (Y2*36))
|	addLengths (FOOT F1) (INCH I1) = INCH(I1+(12*F1))
|	addLengths (YARD Y1) (FOOT F1) = INCH((F1*12) + (Y1*36))
|	addLengths (YARD Y1) (INCH I1) = INCH(I1 + (Y1*36))
;
(*addLengths (FOOT 2) (INCH 5)
;*)
(*b*)
fun addAllLengths [[]] = INCH(0)
|	addAllLengths LL =
	let
	fun lengthHelp L = fold addLengths (INCH(0)) L
	in
	fold addLengths (INCH(0)) (map lengthHelp LL)
	end
;
(*addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10], [YARD 3]] (*lengthUnit list list*)
;*)

(*Problem 4*)
(*a*)
datatype 'a Tree = LEAF of 'a | NODE of 'a * ('a Tree) * ('a Tree)

fun sumTree (NODE (value,left,right)) = (sumTree left) + (sumTree right)
|	sumTree (LEAF value) = value
;
(*val t1 = NODE (1, NODE(2, NODE (3,LEAF 4, LEAF 5), LEAF 6), NODE(7, LEAF 8, LEAF 9))
;
sumTree t1
;*)
(*b*)
fun createSumTree (NODE (value,left,right)) = NODE((sumTree(left)+sumTree(right)),createSumTree(left),createSumTree(right))
|	createSumTree (LEAF value) = LEAF value
;
(*val t3 = NODE (0, NODE(0, NODE (0,LEAF 4, LEAF 5), LEAF 6), NODE(0, LEAF 8, LEAF 9))
;
createSumTree t3
;*)
(*Problem 5*)
(*a*)
datatype 'a listTree = listLEAF of ('a list) | listNODE of ('a listTree list)

(*fun fold f base [] = base
|	fold f base (x::rest) = f x (fold f base rest)*)
fun add x y = x+y
;
fun foldListTree f base (listLEAF (nodeList)) = fold f base nodeList
|	foldListTree f base (listNODE (treeList)) =
	let
	fun foldListTreeHelp (listLEAF (nodeList)) = fold f base nodeList
	|	foldListTreeHelp (listNODE (treeList)) = fold f base (map foldListTreeHelp treeList)
	in
	fold f base (map foldListTreeHelp treeList)
	end
;
(*val t4 = listNODE(
[ listNODE ([ listLEAF [1,2,3],listLEAF [4,5],listNODE([listLEAF [6], listLEAF []]) ]),
 listNODE([]),
 listLEAF [7,8],
 listNODE([listLEAF [], listLEAF []]) ])
 ;
(*val t4 = listNODE ([ listNODE ([ listLEAF [1,2,3],listLEAF [4,5],listNODE([listLEAF[6],listLEAF []]) ]),listNODE([]),listLEAF([7,8]),listNODE([listLEAF [], listLEAF []])])*)
foldListTree add 0 t4
;*)







(*use "C:\\Users\\Eric Furukawa\\Desktop\\HW2.sml"*)
(*TESTS*)
(*************************************)
(*Assignment 2 - Tests*)
(*************************************)
fun merge2Test () =
   let 
     val merge2T1 = (merge2 [2,5,6,8,9] [1,3,4,5,7,8,10] = [1,2,3,4,5,5,6,7,8,8,9,10] )
	 val merge2T2 = (merge2 [1,2] [0,10,12] = [0,1,2,10,12] )
	 val merge2T3 = (merge2 [1,3,3,5,5] [~1,2,4] = [~1,1,2,3,3,4,5,5] )
	 val merge2T2 = (merge2 [1,2,3] [] = [1,2,3] )
     val merge2T4 = (merge2 [] [1,2] = [1,2]) (*first list empty*)
     val merge2T5 = (merge2 [] [] = [] ) (*Both lists empty*)
   in 
     print ("\n------------- \nmerge2:\n" ^ 
            "  test1: " ^ Bool.toString(merge2T1) ^ "\n" ^
            "  test2: " ^ Bool.toString(merge2T2) ^ "\n" ^
 	        "  test3: " ^ Bool.toString(merge2T3) ^ "\n" ^
			"  test4: " ^ Bool.toString(merge2T4) ^ "\n" ^
            "  test5: " ^ Bool.toString(merge2T5) ^ "\n")		
   end
val _ = merge2Test()

fun merge2TailTest () =
   let 
     val merge2TailT1 = (merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10] = [1,2,3,4,5,5,6,7,8,8,9,10] )
     val merge2TailT2 = (merge2Tail [1,2] [0,10,12] = [0,1,2,10,12] )
     val merge2TailT3 = (merge2Tail [1,3,3,5,5] [~1,2,4] = [~1,1,2,3,3,4,5,5] )
	 val merge2TailT4 = (merge2Tail [1,2,3] [] = [1,2,3] )
     val merge2TailT5 = (merge2Tail [] [1,2] = [1,2] )
     val merge2TailT6 = (merge2Tail [] [] = [] )
   in 
     print ("\n------------- \nmerge2Tail:\n" ^ 
            "  test1: " ^ Bool.toString(merge2TailT1) ^ "\n" ^
            "  test2: " ^ Bool.toString(merge2TailT2) ^ "\n" ^
 	        "  test3: " ^ Bool.toString(merge2TailT3) ^ "\n" ^
			"  test4: " ^ Bool.toString(merge2TailT4) ^ "\n" ^
            "  test5: " ^ Bool.toString(merge2TailT5) ^ "\n" ^
 	        "  test6: " ^ Bool.toString(merge2TailT6) ^ "\n")		
   end
val _ = merge2TailTest()


fun mergeNTest () =
   let 
     val mergeNT1 = (mergeN [[1,2],[10,12],[2,5,6,8,9]] = [1,2,2,5,6,8,9,10,12] )
     val mergeNT2 = (mergeN [[3,4],[~3,~2,~1],[1,2,5,8,9]] = [~3,~2,~1,1,2,3,4,5,8,9] )
     val mergeNT3 = (mergeN [[],[3]] = [3] )
	 val mergeNT4 = (mergeN [[]] = [] ) (*only empty list of lists*)
     val mergeNT5 = (mergeN [[1]] = [1] ) (*single list*)
     val mergeNT6 = (mergeN [[~1,3],[~2,4]] = [~2,~1,3,4] ) (*interwoven negative and positive*)
   in 
     print ("\n------------- \nmergeN:\n" ^ 
            "  test1: " ^ Bool.toString(mergeNT1) ^ "\n" ^
            "  test2: " ^ Bool.toString(mergeNT2) ^ "\n" ^
 	        "  test3: " ^ Bool.toString(mergeNT3) ^ "\n" ^
			"  test4: " ^ Bool.toString(mergeNT4) ^ "\n" ^
            "  test5: " ^ Bool.toString(mergeNT5) ^ "\n" ^
 	        "  test6: " ^ Bool.toString(mergeNT6) ^ "\n")		
   end
val _ = mergeNTest()


fun getInRangeTest () =
   let 
     val getInRangeT1 = (getInRange 3 10 [1,2,3,4,5,6,7,8,9,10,11] = [4,5,6,7,8,9] )
     val getInRangeT2 = (getInRange ~5 5 [~10,~5,0,5,10] = [0] )
     val getInRangeT3 = (getInRange ~1 1 [~2,2,3,4,5] = [] )
	 val getInRangeT4 = (getInRange 1 1 [0,1,2,3,4] = [] ) (*range of 0*)
     val getInRangeT5 = (getInRange 1 3 [2,2,2] = [2,2,2] ) (*multiple same values*)
     val getInRangeT6 = (getInRange 3 1 [0,1,2,3,4] = [] ) (*non existant range*)
   in 
     print ("\n------------- \ngetInRange:\n" ^ 
            "  test1: " ^ Bool.toString(getInRangeT1) ^ "\n" ^
            "  test2: " ^ Bool.toString(getInRangeT2) ^ "\n" ^
 	        "  test3: " ^ Bool.toString(getInRangeT3) ^ "\n"	^
			"  test4: " ^ Bool.toString(getInRangeT4) ^ "\n" ^
            "  test5: " ^ Bool.toString(getInRangeT5) ^ "\n" ^
 	        "  test6: " ^ Bool.toString(getInRangeT6) ^ "\n")		
   end
val _ = getInRangeTest()


fun countInRangeTest () =
   let 
     val countInRangeT1 = (countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]] = 6 )
     val countInRangeT2 = (countInRange ~5 5 [[~10,~5,~4],[0,4,5],[],[10]] = 3 )
     val countInRangeT3 = (countInRange 1 5 [[1,5],[1],[5],[]] = 0 )
	 val countInRangeT4 = (countInRange 3 10 [[]] = 0 ) (*empty list of lists*)
     val countInRangeT5 = (countInRange 1 1 [[0,1,2],[0,1,2]] = 0 ) (*range of 0 abd identical*)
     val countInRangeT6 = (countInRange 1 3 [[2,2,2],[2,2]] = 5 ) (*multiple same values in difft lists*)
   in 
     print ("\n------------- \ncountInRange:\n" ^ 
            "  test1: " ^ Bool.toString(countInRangeT1) ^ "\n" ^
            "  test2: " ^ Bool.toString(countInRangeT2) ^ "\n" ^
 	        "  test3: " ^ Bool.toString(countInRangeT3) ^ "\n" ^
			"  test4: " ^ Bool.toString(countInRangeT4) ^ "\n" ^
            "  test5: " ^ Bool.toString(countInRangeT5) ^ "\n" ^
 	        "  test6: " ^ Bool.toString(countInRangeT6) ^ "\n")		
   end
val _ = countInRangeTest()

fun addLengthsTest () =
   let 
     val addLengthsT1 = (addLengths (FOOT 2) (INCH 5) = INCH 29 )
     val addLengthsT2 = (addLengths (YARD 3) (INCH 3) = INCH 111 )
     val addLengthsT3 = (addLengths (FOOT 3) (FOOT 5) = INCH 96 )
	 val addLengthsT4 = (addLengths (YARD 0) (YARD 0) = INCH 0 ) (*zeros*)
     val addLengthsT5 = (addLengths (FOOT ~2) (INCH ~5) = INCH ~29 ) (*negative values*)
     val addLengthsT6 = (addLengths (FOOT 1) (addLengths (FOOT 1) (FOOT 1)) = INCH 36 ) (*nested call for 3 vals*)
   in 
     print ("\n------------- \naddLengths:\n" ^ 
            "  test1: " ^ Bool.toString(addLengthsT1) ^ "\n" ^
            "  test2: " ^ Bool.toString(addLengthsT2) ^ "\n" ^
 	        "  test3: " ^ Bool.toString(addLengthsT3) ^ "\n" ^
			"  test4: " ^ Bool.toString(addLengthsT4) ^ "\n" ^
            "  test5: " ^ Bool.toString(addLengthsT5) ^ "\n" ^
 	        "  test6: " ^ Bool.toString(addLengthsT6) ^ "\n")		
   end
val _ = addLengthsTest()

fun addAllLengthsTest () =
   let 
     val addAllLengthsT1 = (addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10], [YARD 3]] = INCH 262 )
     val addAllLengthsT2 = (addAllLengths [[FOOT 2], [FOOT 2, INCH 2],[]] = INCH 50 )
     val addAllLengthsT3 = (addAllLengths [] = INCH 0 )
	 val addAllLengthsT4 = (addAllLengths [[], [INCH 1]] = INCH 1 ) (*one empty list*)
     val addAllLengthsT5 = (addAllLengths [[FOOT ~1, FOOT ~1], [FOOT ~1]] = INCH ~36 ) (*negatives*)
     val addAllLengthsT6 = (addAllLengths [[YARD 1], [INCH 1, FOOT 1]] = INCH 49 ) (*one of each datatype*)
   in 
     print ("\n------------- \naddAllLengths:\n" ^ 
            "  test1: " ^ Bool.toString(addAllLengthsT1) ^ "\n" ^
            "  test2: " ^ Bool.toString(addAllLengthsT2) ^ "\n" ^
 	        "  test3: " ^ Bool.toString(addAllLengthsT3) ^ "\n" ^
			"  test4: " ^ Bool.toString(addAllLengthsT4) ^ "\n" ^
            "  test5: " ^ Bool.toString(addAllLengthsT5) ^ "\n" ^
 	        "  test6: " ^ Bool.toString(addAllLengthsT6) ^ "\n")		
   end
val _ = addAllLengthsTest()


fun treeTest () =
   let 
	 (*GIVEN TREES*)
	 val tree1 = NODE (1, NODE(2, NODE (3,LEAF 4, LEAF 5), LEAF 6), NODE(7, LEAF 8, LEAF 9))
	 val tree2 = NODE (0, NODE(0, NODE (0,LEAF 4, LEAF 5), LEAF 6), NODE(0, LEAF 8, LEAF 9))
	 val tree3 = listNODE(
[ listNODE ([ listLEAF [1,2,3],listLEAF [4,5],listNODE([listLEAF [6], listLEAF []]) ]),
 listNODE([]),
 listLEAF [7,8],
 listNODE([listLEAF [], listLEAF []]) ]) 
	 
	 (*NEW TREES*)
	 val tree4 = NODE (5, NODE(3, NODE(6, LEAF 4, NODE(~3, LEAF ~4, LEAF 5)), LEAF 6), NODE(9, LEAF 2, LEAF 4))
	 
	 val tree5 = listNODE( [listLEAF [1,5,6], listNODE( [listNODE([listLEAF [1,4], listNODE([listLEAF [1]]), listLEAF [~5]])]),listLEAF[1,2] ] )
	 val tree6 = listLEAF [1,2,3]
	 
     val sumTreeT1 = (sumTree tree1 = 32)
     val createSumTreeT1 = (createSumTree tree2 = NODE (32, NODE (15, NODE (9,LEAF 4,LEAF 5),LEAF 6), NODE (17,LEAF 8,LEAF 9)))
     val foldListTreeT1 = (foldListTree add 0 tree3 = 36)
	 val sumTreeT2 = (sumTree tree4 = 17 )
     val createSumTreeT2 = (createSumTree tree4 = NODE (17, NODE (11, NODE (5, LEAF 4, NODE (1, LEAF ~4, LEAF 5)), LEAF 6), NODE(6, LEAF 2, LEAF 4)))
     val foldListTreeT2 = (foldListTree add 0 tree5 = 16 )
	 val foldListTreeT3 = (foldListTree add 0 tree6 = 6 )
   in 
     print ("\n------------- \nTree Tests:\n" ^ 
            "  sumTree test1: " ^ Bool.toString(sumTreeT1) ^ "\n" ^
            "  createSumTree test1: " ^ Bool.toString(createSumTreeT1) ^ "\n" ^
 	        "  foldListTree test1: " ^ Bool.toString(foldListTreeT1) ^ "\n" ^
			"  sumTree test2: " ^ Bool.toString(sumTreeT2) ^ "\n" ^
            "  createSumTree test2: " ^ Bool.toString(createSumTreeT2) ^ "\n" ^
 	        "  foldListTree test2: " ^ Bool.toString(foldListTreeT2) ^ "\n" ^
			"  foldListTree test3: " ^ Bool.toString(foldListTreeT3) ^ "\n") (*Edge case bug removed (single leaf)*)
   end
val _ = treeTest()

;

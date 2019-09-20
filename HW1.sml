
// Eric Furukawa
// Cpts 355 HW1
//

//Problem 1 -> exists
fun exists (x,[]) = false
| 	exists (x,(y::search)) =
	if y = x then true
	else exists (x,search)
;

val search = 5
val slist = [4,5,6]
;
exists (search,slist)
;

//Problem 2 -> listUnion (use exists inside this one) // :: in parameter is split, else it is an append
fun listUnion list1 [] = []
|	listUnion [] list2 = []
|	listUnion (x::rest) list2 = 
	if exists(x, list2) then x::(listUnion rest list2)
	else listUnion rest list2
;

val exList1 = [1,2,3]
val exList2 = [3,4,5]
;
listUnion (exList1,exList2)
;

//Problem 3

//Problem 4

//Problem 5

//Problem 6



//hint on 6 -> Reverse the list
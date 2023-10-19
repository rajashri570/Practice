//write a program to compare two arrays
package main

import "fmt"

func main() {
	var arr = [4]int{45, 34, 22, 77}
	var arr2 = [4]int{11, 22, 44, 33}
	var arr3 = arr
	if arr == arr2 {
		fmt.Println("both are same")
	} else {
		fmt.Println("not same")
	}
	if arr == arr3 {
		fmt.Println("Both array are same")
		fmt.Println(arr)
		fmt.Println(arr3)
	} else {
		fmt.Println("Both arrays are not same")
	}
}

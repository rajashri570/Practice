//write a program to create array from existing array.
package main

import "fmt"

func main() {
	var arr1 = [5]int{3, 5, 6, 8, 0}
	var arr2 = arr1
	fmt.Println("first array: ", arr1)
	fmt.Println("Second array: ", arr2)
	arr2[4] = 30

	fmt.Println("second array: ", arr2)
}

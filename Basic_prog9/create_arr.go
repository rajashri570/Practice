package main

import "fmt"

func main() {
	var arr [5]int
	arr[0] = 2
	arr[1] = 4
	arr[2] = 5
	arr[3] = 6

	for i := 0; i <= 4; i++ {
		fmt.Printf("%d", arr[i])
		fmt.Print(" ")
	}
	fmt.Println()
	fmt.Println("length of array: ", len(arr))
}

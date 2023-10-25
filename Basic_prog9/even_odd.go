// Write a program to check given number is even or odd.

package main

import "fmt"

func main() {
	var num int
	fmt.Println("Enter the number: ")
	fmt.Scan(&num)
	if num%2 == 0 {
		fmt.Println(num, "is even number")

	} else {
		fmt.Println(num, "is Odd number")
	}

}

// Write a program to create multplication table for  given number

package main

import "fmt"

func main() {
	var num int
	fmt.Println("Enter the number:")
	fmt.Scan(&num)
	for i := 1; i <= 10; i++ {
		fmt.Println(num, "*", i, "=", num*i)
	}
}

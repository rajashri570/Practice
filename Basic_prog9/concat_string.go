package main

import "fmt"

func main() {
	fmt.Print("Enter First String: ") //Print function is used to display output in same line
	var str1 string
	fmt.Scanln(&str1) // Take input from user
	fmt.Println("Enter Second String: ")
	var str2 string
	fmt.Scanln(&str2)
	fmt.Println(str1 + str2) // Addition of two string
}

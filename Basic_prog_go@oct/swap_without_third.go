package main
import "fmt"

func main(){
	var num1,num2 int
	num1 = 23
	num2 = 30

	fmt.Println("Num1:",num1)
	fmt.Println("Num2:",num2)

	num1,num2 = num2,num1

	fmt.Println("---after swapping----")
	fmt.Println("Num1:",num1)
	fmt.Println("Num2:",num2)

}
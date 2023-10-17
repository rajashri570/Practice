package main
import "fmt"


func swap(num1,num2 int)(int,int){
	var temp int
	temp = num1
	num1 = num2
	num2 = temp
	return num1,num2
}

func main(){
	var num1 int
	var num2 int

	fmt.Println("Enter the value of num1:")
	fmt.Scan(&num1)
	fmt.Println("Enter the value of num2:")
    fmt.Scan(&num2)
	fmt.Println("Num1:",num1,"Num2:",num2)
	var x,y int
	x,y = swap(num1,num2)
	fmt.Println("num1:",x,"num2:",y)

}
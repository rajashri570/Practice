package main
import "fmt"

func fact(num int)int{
	if num == 0 || num == 1{
		return 1
	}
	return (num*fact(num-1))
	
}

func main(){
	var num int
	fmt.Println("Enter the number:")
	fmt.Scan(&num)
	var res = fact(num)
	fmt.Print(res)

}
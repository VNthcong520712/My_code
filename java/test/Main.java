import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);
        int n = Integer.valueOf(inp.nextLine());
        String y = inp.nextLine();
        String[] arr = y.split(" ");
        if(arr.length == n){
            int max = Integer.valueOf(arr[0]);
            for(String i : arr){
                int u = Integer.parseInt(i);
                if(u > max) max = u;
            }
            System.out.print(max);
        }
        inp.close();
    }
}
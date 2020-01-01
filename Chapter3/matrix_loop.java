import java.util.*;

public class matrix_loop{
	public static void main(String[] args){
		
		int randomNum = 0;
		
		Random rand = new Random();
		
		for(int i = 0; i < 100000; i++){
			
			randomNum = rand.nextInt(2);
			System.out.print(randomNum);
			
		}
		
	}
}
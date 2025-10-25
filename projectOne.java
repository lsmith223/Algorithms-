import java.io.FileWriter;
import java.io.IOException;

public class projectOne {
//Binary Part A

		private long additions;

	    public projectOne() {
	        additions = 0;
	    }

	    // Recursively count # of BO in n
	    public int NumBinaryDigits(int n) {
	        if (n == 1) {
	            return 1; //base case
	        } else {
	            additions++; 
	            return NumBinaryDigits(n / 2) + 1;
	        }
	    }

	    public long getAdditions() {
	        return additions;
	    }

	    // Reset operation counter before each new test
	    public void resetAdditions() {
	        additions = 0;
	    }
	

	    public static void main(String[] args) {
	    	
	    	projectOne binary = new projectOne();
	    
	    	try (FileWriter writer = new FileWriter("projectOneBinary.txt")) {
	    		writer.write(String.format("n     NumBinaryDigits(n)     Basic Operations(Addition)"));
	    		
	    		for (int n = 1; n <= 50; n++) {
		            binary.resetAdditions();
		            int digits = binary.NumBinaryDigits(n);
		            long bo = binary.getAdditions();

		            writer.write(String.format(n + "      " + digits + "     " + bo));
	    		}   
	    		
	    		System.out.println("Output successfully written to file");
	    		} catch (IOException e) {
	    			System.out.println("Error writing to file");
	    			e.printStackTrace();
	    		}
	    	
	    	}
	    

}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
       	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());

        st=new StringTokenizer(br.readLine());
        int B = Integer.parseInt(st.nextToken());

        int hundredsDigit = B / 100; // 백의 자리 수
        int tensDigit = (B / 10) % 10; // 십의 자리 수
        int unitsDigit = B % 10; // 일의 자리 수

        System.out.println(A*unitsDigit); //(3)
        System.out.println(A*tensDigit); //(4)
        System.out.println(A*hundredsDigit); //(5)
        System.out.println(A*B); //(6)
    }
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int result = 0;
        if (A==B && B==C) result = 10000+A*1000;
        else if(A==B) result = 1000+A*100;
        else if(B==C) result = 1000+B*100;
        else if(C==A) result = 1000+C*100;
        else{
            int max = A;
            if(max<B) max = B;
            if(max<C) max = C;
            result = max*100;
        }
        System.out.println(result);
    }
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String result = "";
        int N = Integer.parseInt(st.nextToken());

        for(int i=0; i<N/4; i++){
            result += "long ";
        }
        System.out.println(result+"int");
    }
}

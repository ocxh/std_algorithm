import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
                BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
                StringTokenizer st=new StringTokenizer(br.readLine());

                int N = Integer.parseInt(st.nextToken());
                int M = Integer.parseInt((st.nextToken()));
                int[] S = new int[N+1];

                int start = 0;
                int end = 0;

                st = new StringTokenizer(br.readLine());
                //합 배열 구하기
                for(int i=1; i<=N; i++){
                    S[i] = S[i-1] + Integer.parseInt(st.nextToken());
                }
                //구간 합 구하기
                for(int i=0; i<M; i++){
                    st = new StringTokenizer(br.readLine());
                    start = Integer.parseInt(st.nextToken());
                    end = Integer.parseInt(st.nextToken());

                    System.out.println(S[end]-S[start-1]);
                }

    }
}

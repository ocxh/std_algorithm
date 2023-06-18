package PrefixSum;
public class BasicPrefixSum {
    public static void main(String[] args) throws Exception {
        int s=2, e=5; // s째부터 e번째까지

        int[] A = {1, 15, 3, 6, 11, 13};
        int[] S = getSumArray(A);

        System.out.println(getPrefixSumArray(S, s, e));
    }
    //합배열 구하기
    //S[i] = S[i-1] + A[i];
    public static int[] getSumArray(int[] arr) {
        int n = arr.length;
        int[] sumArray = new int[n];
        
        sumArray[0] = arr[0]; // 첫 번째 원소는 그대로 복사

        for (int i = 1; i < n; i++) {
            sumArray[i] = sumArray[i - 1] + arr[i];
        }

        return sumArray;
    }
    public static int getPrefixSumArray(int[] arr, int start, int end) {
        //구간합 구하기(3번째~5번째)
        //S[j] - S[i-1], i번째~j까지
        return arr[end]-arr[start-1];
    }
}

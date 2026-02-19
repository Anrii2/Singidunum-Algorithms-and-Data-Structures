import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        SelectSort select = new SelectSort();
        System.out.println("Hello, World!");
        System.out.println("Ovo je pocetak ucenja Jave po drugi put");
        int[] arr = {12, 34, 19, 1, 53, 82, 32};
        System.out.println(Arrays.toString(arr));
        select.selectSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}

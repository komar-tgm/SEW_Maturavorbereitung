public class ReverseString {
    public static String revers(String text){
        String output="";
        for (int i=text.length()-1;i>=0;i--){
            output+=text.charAt(i);
        }
        return output;
    }
}

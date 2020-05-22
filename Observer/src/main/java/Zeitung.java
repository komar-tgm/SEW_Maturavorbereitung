public class Zeitung {
    private String name;
    private String head;
    private String text;

    public Zeitung(){
        this.name = "";
        this.head = "";
        this.text = "";
    }
    public Zeitung(String name, String head, String text) {
        this.name = name;
        this.head = head;
        this.text = text;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getHead() {
        return head;
    }

    public void setHead(String head) {
        this.head = head;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
}

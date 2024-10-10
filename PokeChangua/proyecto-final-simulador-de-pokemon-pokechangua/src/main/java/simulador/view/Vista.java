package simulador.view;

import java.util.Scanner;

public class Vista {
    private Scanner sc = new Scanner(System.in);
    
    public static void mostrarMensaje(String mensaje){
        System.out.println(mensaje);
    }
    
    public static String pedirString(){
    	Vista v = new Vista();
        return v.sc.nextLine();
    }
    
}
